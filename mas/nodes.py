"""Workflow nodes and the transition table.

Each node is `fn(state, ctx) -> dict` of state updates. Control flow lives only
in TRANSITIONS; recovery after a node failure lives only in ON_ERROR.
"""
from __future__ import annotations

import ast
import json
import re
from pathlib import Path

from code_agent.assembly import AgentPolicy, create_agent
from code_agent.fault_feedback import FEEDBACK_OPERATORS
from code_agent.tools.factories import build_registry
from eval.metrics import measure_coverage, run_mutation_tests, run_pytest_on

from .spec import extract_spec

END = "END"
TESTS = "test_solution.py"
PLAN_REF = re.compile(r"^test_p(\d+)(?:_|$)", re.I)
CATEGORIES = ("normal", "boundary", "empty", "error", "state", "property")


# ---- helpers ---------------------------------------------------------------
def extract_json(text: str) -> dict:
    """Parse the first JSON object in a model reply (fences and prose allowed)."""
    text = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.M).strip()
    start = text.find("{")
    if start < 0:
        raise ValueError("no JSON object in reply")
    depth, in_str, esc = 0, False, False
    for i in range(start, len(text)):
        ch = text[i]
        if in_str:
            esc = (ch == "\\") and not esc
            if ch == '"' and not esc:
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch in "{}":
            depth += 1 if ch == "{" else -1
            if depth == 0:
                return json.loads(text[start:i + 1])
    raise ValueError("unterminated JSON object")


def json_call(ctx, role: str, system: str, user: str, check) -> dict:
    """Ask for JSON; on a malformed or invalid reply, say what was wrong and ask once more."""
    messages = [{"role": "system", "content": system}, {"role": "user", "content": user}]
    problem = ""
    for _ in range(2):
        reply = ctx.chat(role, messages)
        try:
            data = extract_json(reply)
            problem = check(data)
            if not problem:
                return data
        except (ValueError, json.JSONDecodeError) as exc:
            problem = str(exc)
        messages = messages + [{"role": "assistant", "content": reply},
                               {"role": "user", "content": f"Invalid reply ({problem}). Reply with only the JSON object."}]
    raise ValueError(f"{role}: no valid JSON after retry ({problem})")


def test_names(source: str) -> list:
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []
    return [n.name for n in tree.body if isinstance(n, ast.FunctionDef) and n.name.startswith("test")]


def plan_ids(name: str) -> list:
    m = PLAN_REF.match(name)
    return [f"P{int(m.group(1))}"] if m else []


# ---- Planner ---------------------------------------------------------------
PLANNER_PROMPT = """You are the test Planner in a team that writes unit tests.
You see only the public specification of a Python module: signatures and docstrings.
The implementation is hidden on purpose, because it may contain bugs.
Work out what the code is supposed to do and which inputs a caller could pass, then
write a test plan of 6-12 items. Each item names concrete inputs and the expected result
derived from the specification, with a rationale quoting or citing the specification.
Cover normal cases, boundaries, empty or degenerate inputs, documented errors, and,
for classes, call sequences and state invariants. If the specification does not decide
a behaviour, list it under "ambiguities" instead of guessing an expected value.
Reply with only JSON:
{"summary": "<what the code does>", "input_domain": "<valid inputs>",
 "items": [{"id": "P1", "category": "normal|boundary|empty|error|state|property",
            "behavior": "...", "input": "...", "expected": "...", "rationale": "...",
            "confidence": "high|medium|low"}],
 "ambiguities": ["..."]}"""


def _check_plan(data):
    items = data.get("items")
    if not isinstance(items, list) or not items:
        return "items must be a non-empty list"
    for n, item in enumerate(items, 1):
        missing = [k for k in ("behavior", "input", "expected") if not item.get(k)]
        if missing:
            return f"item {n} lacks {missing}"
    return ""


def planner(state, ctx):
    spec = extract_spec(state["source"])
    data = json_call(ctx, "planner", PLANNER_PROMPT, f"Specification:\n```python\n{spec}```", _check_plan)
    for n, item in enumerate(data["items"], 1):
        item["id"] = f"P{n}"  # renumber: test names cite these ids
        if item.get("category") not in CATEGORIES:
            item["category"] = "normal"
    data.setdefault("ambiguities", [])
    return {"spec": spec, "plan": data}


# ---- TestGen (the Homework 1 agent) ----------------------------------------
TASK = "Generate unit tests for solution.py in the current directory.\nWrite them to test_solution.py using pytest.\n"

PLAN_RULES = """
A Planner who saw only the specification (not the implementation) wrote this test plan:
{plan}

Implement the plan items as tests.
- Name each test after the item it implements: test_p<N>_<short>, e.g. test_p3_empty_list.
  Tests the plan missed are welcome; name them test_extra_<short>.
- Take expected values from the plan and the docstring. Do not obtain them by reading or
  running the implementation.
- If a test that follows the plan fails on solution.py, do not change its expected value to
  match the implementation. Leave it and mention it in your final answer: a Reviewer will
  decide whether the test or the code is wrong.
"""


def testgen_prompt(state):
    text = TASK
    if state.get("plan"):
        text += PLAN_RULES.format(plan=json.dumps(state["plan"]["items"], ensure_ascii=False, indent=1))
    if state["reviews"] and state["reviews"][-1]["decision"] == "revise":
        notes = "\n".join(f"- {i}" for i in state["reviews"][-1]["instructions"])
        text += ("\nThis is a revision. Accepted tests in test_solution.py are kept. "
                 "Submit only new or corrected tests, under new names. Reviewer instructions:\n" + notes + "\n")
    return text


def testgen(state, ctx):
    ws = Path(state["workspace"])
    settings = ctx.agent_settings(ws)
    policy = AgentPolicy.test_generation()
    registry = build_registry(settings, policy.tool_names)
    agent = create_agent(settings, policy, llm=ctx.agent_llm(state["round"] + 1), registry=registry,
                         on_event=ctx.agent_event)
    agent.state.add_user(testgen_prompt(state))
    agent.begin_task()
    result = agent.run()
    snap = registry.get("submit_tests").generation.snapshot()
    ctx.add_usage("testgen", agent.state.llm_calls, agent.state.usage.total_tokens)
    record = {
        "round": state["round"] + 1,
        "status": result.status,
        "accepted": [c["name"] for c in snap["accepted"]],
        "failed": [{"name": c["name"], "plan_ids": plan_ids(c["name"]), "code": c["code"],
                    "oracle_reason": c.get("oracle_reason", ""), "diagnostic": c["diagnostic"]}
                   for c in snap["failed"]],
        "attempts": len(snap["attempts"]),
        "turns": agent.state.turn_index,
        "final_text": (result.final_text or "")[-800:],
    }
    if not (ws / TESTS).exists() and not record["failed"]:
        raise RuntimeError(f"TestGen produced no tests (agent status {result.status}: {result.error})")
    return {"round": record["round"], "testgen": state["testgen"] + [record]}


# ---- Verifier (no LLM) -----------------------------------------------------
def verifier(state, ctx):
    ws = Path(state["workspace"])
    source = state["source"]
    tests = ws / TESTS
    names = test_names(tests.read_text(encoding="utf-8")) if tests.exists() else []
    report = {"round": state["round"], "tests": len(names)}
    if names:
        run = run_pytest_on(TESTS, ws)
        report["pytest"] = {"passed": run.passed, "failed": run.failed, "errors": run.errors,
                            "all_pass": run.all_pass}
        cov = measure_coverage(ws, "solution.py")
        report["coverage"] = cov.get("percent")
        try:
            files = json.loads((ws / ".coverage.json").read_text(encoding="utf-8"))["files"]
            report["missing_lines"] = next(iter(files.values()))["missing_lines"]
        except (OSError, ValueError, KeyError, StopIteration):
            report["missing_lines"] = []
        mut = run_mutation_tests(ws, source, TESTS, max_mutants=8, operators=FEEDBACK_OPERATORS)
        report["mutation"] = {"score": mut["score"], "killed": mut["killed"], "total": mut["total"],
                              "survivors": [{"line": m["line"], "description": m["description"]}
                                            for m in mut["survived"]][:5]}
    if state.get("plan"):
        cited = {i for n in names for i in plan_ids(n)}
        cited |= {i for f in state["testgen"][-1]["failed"] for i in f["plan_ids"]}
        cited |= {i for b in state["suspected_bugs"] for i in b["plan_ids"]}
        ids = [it["id"] for it in state["plan"]["items"]]
        report["plan_coverage"] = {"cited": sorted(cited & set(ids), key=lambda x: int(x[1:])),
                                   "missing": [i for i in ids if i not in cited],
                                   "ratio": len(cited & set(ids)) / len(ids)}
    return {"verification": state["verification"] + [report]}


# ---- Reviewer --------------------------------------------------------------
REVIEWER_PROMPT = """You are the test Reviewer. Tests were written from a specification-only plan,
then run against the implementation. Your jobs:
1. For every failing test decide, from the specification and plan (not from what the
   implementation happens to do):
   "test_wrong"    - the test's input or expected value contradicts the specification;
   "suspected_bug" - the test follows the specification and the implementation violates it.
2. Decide "accept" if the suite is adequate, or "revise" with concrete instructions:
   fix each test_wrong test, cover missing plan items, and add specification-valid tests
   that would catch the listed surviving faults. Do not ask to change a suspected_bug test.
Reply with only JSON:
{"verdicts": [{"test": "<name>", "judgement": "test_wrong|suspected_bug", "reason": "..."}],
 "decision": "accept|revise", "instructions": ["..."]}"""


def _check_review(failed_names):
    def check(data):
        if data.get("decision") not in ("accept", "revise"):
            return "decision must be accept or revise"
        judged = {v.get("test") for v in data.get("verdicts", []) if v.get("judgement") in ("test_wrong", "suspected_bug")}
        if failed_names - judged:
            return f"missing a verdict for {sorted(failed_names - judged)}"
        if data["decision"] == "revise" and not data.get("instructions"):
            return "revise needs instructions"
        return ""
    return check


def reviewer(state, ctx):
    tg, ver = state["testgen"][-1], state["verification"][-1]
    failed = {f["name"]: f for f in tg["failed"]}
    parts = [f"Specification:\n```python\n{state.get('spec') or extract_spec(state['source'])}```",
             f"Implementation under test:\n```python\n{state['source']}```"]
    if state.get("plan"):
        parts.append("Plan:\n" + json.dumps(state["plan"], ensure_ascii=False, indent=1))
    parts.append("Accepted tests (pass on the implementation): " + (", ".join(tg["accepted"]) or "none"))
    for f in failed.values():
        parts.append(f"Failing test {f['name']} (plan {f['plan_ids'] or '-'}):\n```python\n{f['code']}```\n"
                     f"Oracle reason given: {f['oracle_reason']}\nFailure:\n{f['diagnostic'][-700:]}")
    parts.append("Verifier report:\n" + json.dumps({k: ver.get(k) for k in
                 ("tests", "pytest", "coverage", "missing_lines", "mutation", "plan_coverage")}, ensure_ascii=False))
    data = json_call(ctx, "reviewer", REVIEWER_PROMPT, "\n\n".join(parts), _check_review(set(failed)))
    verdicts = [v for v in data.get("verdicts", []) if v.get("test") in failed]
    bugs = [{**failed[v["test"]], "reason": v.get("reason", ""), "round": state["round"]}
            for v in verdicts if v["judgement"] == "suspected_bug"]
    review = {"round": state["round"], "decision": data["decision"], "verdicts": verdicts,
              "instructions": data.get("instructions", [])}
    return {"reviews": state["reviews"] + [review], "suspected_bugs": state["suspected_bugs"] + bugs}


NODES = {"planner": planner, "testgen": testgen, "verifier": verifier, "reviewer": reviewer}


# ---- Transition table: the whole control flow lives here --------------------
def start(state):
    return "planner" if state["config"]["planner"] else "testgen"


def after_verifier(state):
    if state["config"]["reviewer"]:
        return "reviewer"
    state["status"] = "completed" if state["verification"][-1]["tests"] else "failed"
    return END


def after_reviewer(state):
    if state["reviews"][-1]["decision"] == "accept":
        state["status"] = "accepted"
        return END
    if state["round"] >= state["config"]["max_rounds"]:
        state["status"] = "forced"  # round cap reached: keep the last suite, flagged
        return END
    return "testgen"


TRANSITIONS = {
    "START": start,
    "planner": lambda s: "testgen",
    "testgen": lambda s: "verifier",
    "verifier": after_verifier,
    "reviewer": after_reviewer,
}


# ---- Recovery after a node has failed twice --------------------------------
def _planner_failed(state):
    state["degraded"].append("planner: continuing without a plan")
    return "testgen"


def _testgen_failed(state):
    if state["testgen"]:  # an earlier round left a suite: verify and stop there
        state["status"] = "forced"
        state["degraded"].append("testgen: kept the previous round's suite")
        return END
    state["status"] = "failed"
    return END


def _reviewer_failed(state):
    state["status"] = "forced"
    state["degraded"].append("reviewer: unreviewed suite shipped")
    return END


def _fatal(state):
    state["status"] = "failed"
    return END


ON_ERROR = {"planner": _planner_failed, "testgen": _testgen_failed,
            "verifier": _fatal, "reviewer": _reviewer_failed}
