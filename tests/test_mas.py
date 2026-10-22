"""Workflow tests: every branch runs offline through the real engine, tools and measurements."""
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import kytest  # noqa: E402
from mas import nodes  # noqa: E402
from mas.spec import extract_spec  # noqa: E402


def run_mock(tmp_path, scenario, *extra):
    assert kytest.main(["--mock", scenario, "--runs", str(tmp_path), *extra]) in (0, 1)
    run_dir = next(tmp_path.iterdir())
    return json.loads((run_dir / "state.json").read_text()), run_dir


def test_spec_hides_bodies_and_keeps_contracts():
    source = '''"""Module doc."""
import math
SECRET = 42

def f(x: int) -> int:
    """Return x squared."""
    return x * x

class Box:
    """A box."""
    size = 3
    def __init__(self, n):
        self.n = n
    def get(self):
        """Return n."""
        return self.n
'''
    spec = extract_spec(source)
    assert "Return x squared." in spec and "def get(self)" in spec and "import math" in spec
    for leaked in ("x * x", "self.n = n", "SECRET", "size = 3"):
        assert leaked not in spec


def test_pass_scenario_follows_the_main_path(tmp_path):
    state, run_dir = run_mock(tmp_path, "pass")
    assert state["status"] == "accepted"
    assert state["history"] == ["planner", "testgen", "verifier", "reviewer"]
    v = state["verification"][-1]
    assert v["tests"] == 6 and v["pytest"]["all_pass"] and v["plan_coverage"]["ratio"] == 1.0
    assert (run_dir / "test_solution.py").exists() and (run_dir / "plan.json").exists()
    events = [json.loads(line)["event"] for line in (run_dir / "log.jsonl").read_text().splitlines()]
    assert events[0] == "start" and events[-1] == "end" and "agent_tool" in events


def test_revise_loop_fixes_a_wrong_test(tmp_path):
    state, _ = run_mock(tmp_path, "revise")
    assert state["status"] == "accepted" and state["round"] == 2
    assert [r["decision"] for r in state["reviews"]] == ["revise", "accept"]
    assert state["reviews"][0]["verdicts"][0]["judgement"] == "test_wrong"
    assert "Fix test_p2_below" in nodes.testgen_prompt({**state, "reviews": state["reviews"][:1]})
    assert not state["suspected_bugs"]


def test_bug_scenario_reports_the_implementation_bug(tmp_path):
    state, run_dir = run_mock(tmp_path, "bug")
    assert {b["name"] for b in state["suspected_bugs"]} == {"test_p5_high_inclusive", "test_p6_degenerate"}
    assert all(b["plan_ids"] for b in state["suspected_bugs"])
    report = (run_dir / "bug_report.md").read_text()
    assert "Plan P5" in report and "assert 1 == 0" in report
    # The accepted suite still passes on the buggy code; the bug tests are kept apart.
    assert state["verification"][-1]["pytest"]["all_pass"]
    assert "test_p5_high_inclusive" not in (run_dir / "test_solution.py").read_text()


def test_round_cap_forces_the_end(tmp_path):
    state, _ = run_mock(tmp_path, "stubborn")
    assert state["status"] == "forced" and state["round"] == 2
    assert [r["decision"] for r in state["reviews"]] == ["revise", "revise"]


def test_planner_failure_is_recovered_without_a_plan(tmp_path):
    state, _ = run_mock(tmp_path, "flaky")
    assert state["status"] == "accepted" and state["plan"] is None
    assert state["history"][0] == "planner!" and len(state["errors"]) == 2
    assert state["degraded"] == ["planner: continuing without a plan"]


def test_ablations_change_the_path(tmp_path):
    state, _ = run_mock(tmp_path / "a", "pass", "--no-planner")
    assert state["history"][0] == "testgen" and "A Planner" not in nodes.testgen_prompt(state)
    state, _ = run_mock(tmp_path / "b", "pass", "--no-reviewer")
    assert state["history"] == ["planner", "testgen", "verifier"] and state["status"] == "completed"


def test_resume_continues_from_the_checkpoint(tmp_path):
    state, run_dir = run_mock(tmp_path, "pass")
    # Rewind the checkpoint to just before the reviewer, as if the process had died there.
    state.update(next="reviewer", status="running", reviews=[], history=state["history"][:3])
    (run_dir / "state.json").write_text(json.dumps(state))
    assert kytest.main(["--mock", "pass", "--resume", str(run_dir)]) == 0
    resumed = json.loads((run_dir / "state.json").read_text())
    assert resumed["status"] == "accepted" and resumed["history"] == ["planner", "testgen", "verifier", "reviewer"]


@pytest.mark.parametrize("reply, ok", [
    ('```json\n{"a": "}"}\n```', True),
    ("Sure! {\"a\": 1} done", True),
    ("no json here", False),
])
def test_extract_json(reply, ok):
    if ok:
        assert isinstance(nodes.extract_json(reply), dict)
    else:
        with pytest.raises(ValueError):
            nodes.extract_json(reply)
