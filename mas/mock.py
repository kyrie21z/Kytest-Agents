"""Offline scenarios: scripted model replies that drive every workflow branch.

The scripts replace only the model. Test execution, coverage, mutation, state
and logs are real, so a scenario shows the actual control flow, not model quality.

  pass      plan -> tests pass -> reviewer accepts
  revise    one test is wrong -> reviewer: test_wrong, revise -> fixed -> accept
  bug       target has an off-by-one bug -> plan-derived test fails -> suspected_bug
  stubborn  reviewer never accepts -> round cap -> status forced
  flaky     planner model keeps failing -> recovered: continue without a plan
"""
from __future__ import annotations

import json
from pathlib import Path

from code_agent.errors import LLMError
from code_agent.llm import BaseLLM, LLMResponse, MockLLM, ToolCall

DEMO = Path(__file__).resolve().parent / "demo"
SCENARIOS = ("pass", "revise", "bug", "stubborn", "flaky")
QUOTE = "return -1 below low, 1 above high, and 0 inside the inclusive interval"

PLAN = {
    "summary": "Classify value relative to the inclusive interval [low, high].",
    "input_domain": "numbers with low <= high",
    "items": [
        {"category": "normal", "behavior": "value inside", "input": "classify(5, 1, 10)", "expected": "0",
         "rationale": "0 inside the interval", "confidence": "high"},
        {"category": "normal", "behavior": "value below low", "input": "classify(0, 1, 10)", "expected": "-1",
         "rationale": "-1 below low", "confidence": "high"},
        {"category": "normal", "behavior": "value above high", "input": "classify(11, 1, 10)", "expected": "1",
         "rationale": "1 above high", "confidence": "high"},
        {"category": "boundary", "behavior": "value equal to low is inside", "input": "classify(1, 1, 10)",
         "expected": "0", "rationale": "the interval is inclusive", "confidence": "high"},
        {"category": "boundary", "behavior": "value equal to high is inside", "input": "classify(10, 1, 10)",
         "expected": "0", "rationale": "the interval is inclusive", "confidence": "high"},
        {"category": "boundary", "behavior": "degenerate interval low == high", "input": "classify(3, 3, 3)",
         "expected": "0", "rationale": "low <= high allows equality", "confidence": "medium"},
    ],
    "ambiguities": ["Behaviour for low > high is not specified."],
}


def case(name, call, expected):
    return {"name": name, "code": f"from solution import classify\n\ndef {name}():\n    assert {call} == {expected}\n",
            "contract_quote": QUOTE, "input_domain": "low <= high",
            "oracle_reason": f"From the plan: {call} -> {expected}", "fault_hypothesis": "wrong side of a boundary"}


GOOD = [case("test_p1_inside", "classify(5, 1, 10)", 0), case("test_p2_below", "classify(0, 1, 10)", -1),
        case("test_p3_above", "classify(11, 1, 10)", 1), case("test_p4_low_inclusive", "classify(1, 1, 10)", 0),
        case("test_p5_high_inclusive", "classify(10, 1, 10)", 0), case("test_p6_degenerate", "classify(3, 3, 3)", 0)]


def submit(cases, final):
    return [LLMResponse(tool_calls=[ToolCall("m1", "submit_tests", json.dumps({"cases": cases}))],
                        usage={"prompt_tokens": 250, "completion_tokens": 50}),
            LLMResponse(content=final, usage={"prompt_tokens": 40, "completion_tokens": 10})]


def review(decision, verdicts=(), instructions=()):
    return LLMResponse(content=json.dumps({"verdicts": list(verdicts), "decision": decision,
                                           "instructions": list(instructions)}), usage={"total_tokens": 200})


class Scripted(BaseLLM):
    def __init__(self, replies):
        self.replies = list(replies)

    def chat(self, messages, tools=None):
        if not self.replies:
            raise LLMError("scripted replies exhausted")
        reply = self.replies.pop(0)
        if isinstance(reply, Exception):
            raise reply
        return reply


class Scenario:
    def __init__(self, name):
        if name not in SCENARIOS:
            raise ValueError(f"unknown scenario {name}; choose from {SCENARIOS}")
        self.name = name
        plan = LLMResponse(content="```json\n" + json.dumps(PLAN) + "\n```", usage={"total_tokens": 400})
        wrong = case("test_p2_below", "classify(0, 1, 10)", 1)  # contradicts the plan
        rounds = {
            "pass": [submit(GOOD, "Six plan-derived tests accepted.")],
            "revise": [submit([GOOD[0], wrong, *GOOD[2:]], "test_p2_below failed; left for the Reviewer."),
                       submit([case("test_p2_below_fixed", "classify(0, 1, 10)", -1)], "Fixed P2.")],
            "bug": [submit(GOOD, "test_p5 and test_p6 fail on solution.py; left for the Reviewer.")],
            "stubborn": [submit(GOOD[:3], "Three tests."), submit(GOOD[3:5], "Two more.")],
            "flaky": [submit(GOOD[:4], "Four tests without a plan.")],
        }[name]
        self.rounds = [MockLLM(responses=r) for r in rounds]
        reviews = {
            "pass": [review("accept")],
            "revise": [review("revise", [{"test": "test_p2_below", "judgement": "test_wrong",
                                          "reason": "Plan P2 and the docstring say -1 below low; the test expects 1."}],
                              ["Fix test_p2_below: classify(0, 1, 10) must be -1."]), review("accept")],
            "bug": [review("accept", [{"test": "test_p5_high_inclusive", "judgement": "suspected_bug",
                                       "reason": "The docstring says the interval is inclusive, so value == high "
                                                 "must give 0; the implementation returns 1."},
                                      {"test": "test_p6_degenerate", "judgement": "suspected_bug",
                                       "reason": "With low == high == value the value is inside the inclusive "
                                                 "interval, so 0 is required; the implementation returns 1."}])],
            "stubborn": [review("revise", instructions=["Cover P4-P6."]),
                         review("revise", instructions=["Cover P6."])],
            "flaky": [review("accept")],
        }[name]
        planner = [LLMError("HTTP 503"), LLMError("HTTP 503")] if name == "flaky" else [plan]
        self.roles = {"planner": Scripted(planner), "reviewer": Scripted(reviews)}

    @property
    def target(self) -> Path:
        return DEMO / ("classify_buggy.py" if self.name == "bug" else "classify.py")

    def role_llm(self, role):
        return self.roles[role]

    def agent_llm(self, round_no):
        return self.rounds[round_no - 1] if round_no <= len(self.rounds) else MockLLM(responses=[
            LLMResponse(content="No further tests.")])
