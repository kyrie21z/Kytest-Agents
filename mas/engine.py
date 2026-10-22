"""State-machine runner: one shared state, checkpointed after every node.

runs/<id>/
  state.json   full shared state, rewritten after every node (resume point)
  log.jsonl    one line per event (node start/end, errors, agent tool calls)
  workspace/   solution.py and the accepted test_solution.py
  plan.json, test_suspected_bugs.py, bug_report.md   written at the end
"""
from __future__ import annotations

import json
import shutil
import time
import traceback
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Dict

from code_agent.testgen import isolate_aliases

from .nodes import END, NODES, ON_ERROR, TESTS, TRANSITIONS

ATTEMPTS_PER_NODE = 2


def new_state(source: str, workspace: Path, *, planner=True, reviewer=True, max_rounds=2) -> Dict[str, Any]:
    return {
        "status": "running", "next": "START", "round": 0,
        "config": {"planner": planner, "reviewer": reviewer, "max_rounds": max_rounds},
        "source": source, "workspace": str(workspace),
        "spec": None, "plan": None,
        "testgen": [], "verification": [], "reviews": [], "suspected_bugs": [],
        "history": [], "errors": [], "degraded": [], "usage": {},
    }


@dataclass
class Context:
    """What nodes may use besides the state. Real and mock runs differ only here."""
    run_dir: Path
    role_llm: Callable[[str], Any]             # role -> BaseLLM for planner/reviewer
    agent_llm: Callable[[int], Any]            # round -> BaseLLM for the TestGen agent
    agent_settings: Callable[[Path], Any]      # workspace -> Settings
    usage: Dict[str, Dict[str, int]] = field(default_factory=dict)

    def log(self, event: str, **data):
        line = {"t": round(time.time(), 3), "event": event, **data}
        with open(self.run_dir / "log.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps(line, ensure_ascii=False, default=str) + "\n")

    def add_usage(self, role, calls, tokens):
        u = self.usage.setdefault(role, {"calls": 0, "tokens": 0})
        u["calls"] += calls
        u["tokens"] += tokens

    def chat(self, role: str, messages) -> str:
        reply = self.role_llm(role).chat(messages)
        self.add_usage(role, 1, int((reply.usage or {}).get("total_tokens") or 0))
        self.log("llm_reply", role=role, chars=len(reply.content))
        return reply.content

    def agent_event(self, event):
        if event.type == "tool_call_end":
            self.log("agent_tool", tool=event.name, error=event.is_error, content=event.content[:300])
        elif event.type in ("run_end", "error"):
            self.log("agent_" + event.type, **{k: v for k, v in vars(event).items() if k != "type"})


def save(state, run_dir: Path):
    tmp = run_dir / "state.json.tmp"
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp.replace(run_dir / "state.json")


def run(state, ctx: Context) -> Dict[str, Any]:
    if state["next"] == "START":
        state["next"] = TRANSITIONS["START"](state)
        ctx.log("start", next=state["next"], config=state["config"])
        save(state, ctx.run_dir)  # visible (and resumable) before the first node finishes
    ctx.usage = state["usage"]
    while state["next"] != END:
        node = state["next"]
        for attempt in range(1, ATTEMPTS_PER_NODE + 1):
            ctx.log("node_start", node=node, round=state["round"], attempt=attempt)
            started = time.time()
            try:
                update = NODES[node](state, ctx)
            except Exception as exc:  # noqa: BLE001 - every failure is recorded and routed
                state["errors"].append({"node": node, "attempt": attempt, "round": state["round"],
                                        "error": f"{type(exc).__name__}: {exc}",
                                        "trace": traceback.format_exc(limit=4)})
                ctx.log("node_error", node=node, attempt=attempt, error=str(exc)[:300])
                save(state, ctx.run_dir)
                continue
            state.update(update)
            state["history"].append(node)
            state["next"] = TRANSITIONS[node](state)
            ctx.log("node_end", node=node, seconds=round(time.time() - started, 2), next=state["next"])
            break
        else:
            state["history"].append(node + "!")
            state["next"] = ON_ERROR[node](state)
            ctx.log("recovered", node=node, next=state["next"], status=state["status"])
        save(state, ctx.run_dir)
    write_artifacts(state, ctx.run_dir)
    save(state, ctx.run_dir)
    ctx.log("end", status=state["status"], rounds=state["round"])
    return state


def write_artifacts(state, run_dir: Path):
    ws = Path(state["workspace"])
    if state["plan"]:
        (run_dir / "plan.json").write_text(json.dumps(state["plan"], ensure_ascii=False, indent=1), encoding="utf-8")
    if (ws / TESTS).exists():
        shutil.copyfile(ws / TESTS, run_dir / TESTS)
    bugs = state["suspected_bugs"]
    if not bugs:
        return
    (run_dir / "test_suspected_bugs.py").write_text(
        "# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.\n\n"
        + "\n\n".join(isolate_aliases(b["code"], f"_bug{i}") for i, b in enumerate(bugs)) + "\n",
        encoding="utf-8")
    lines = ["# Suspected implementation bugs", ""]
    plan = {i["id"]: i for i in (state["plan"] or {}).get("items", [])}
    for b in bugs:
        lines += [f"## {b['name']}", ""]
        for pid in b["plan_ids"]:
            if pid in plan:
                lines += [f"- Plan {pid}: {plan[pid]['behavior']} — input `{plan[pid]['input']}`, "
                          f"expected `{plan[pid]['expected']}`"]
        lines += [f"- Reviewer: {b['reason']}", "", "```", b["diagnostic"][-600:].strip(), "```", ""]
    (run_dir / "bug_report.md").write_text("\n".join(lines), encoding="utf-8")
