"""Kytest-Agents: Planner -> TestGen -> Verifier -> Reviewer test-generation workflow.

    python kytest.py path/to/module.py                 real model (settings from .env)
    python kytest.py --mock bug                        offline scenario (see mas/mock.py)
    python kytest.py module.py --no-planner            ablation: TestGen reads the code directly
    python kytest.py --resume runs/<id>                continue an interrupted run
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT))

from code_agent.assembly import build_llm  # noqa: E402
from code_agent.config import Settings  # noqa: E402
from mas.engine import Context, new_state, run  # noqa: E402
from mas.mock import SCENARIOS, Scenario  # noqa: E402


def real_context(run_dir: Path) -> Context:
    def settings_for(ws: Path) -> Settings:
        return Settings.from_env(workspace=ws, env_file=ROOT / ".env")
    settings = settings_for(run_dir / "workspace")
    settings.require_llm()
    client, _ = build_llm(settings)
    return Context(run_dir=run_dir, role_llm=lambda role: client, agent_llm=lambda n: client,
                   agent_settings=settings_for)


def mock_context(run_dir: Path, scenario: Scenario) -> Context:
    return Context(run_dir=run_dir, role_llm=scenario.role_llm, agent_llm=scenario.agent_llm,
                   agent_settings=lambda ws: Settings(workspace=ws, max_steps=4))


def summary(state, run_dir: Path) -> str:
    out = [f"status: {state['status']}   rounds: {state['round']}   path: {' -> '.join(state['history'])}"]
    if state["plan"]:
        out.append(f"plan: {len(state['plan']['items'])} items, {len(state['plan']['ambiguities'])} ambiguities")
    if state["verification"]:
        v = state["verification"][-1]
        mut = v.get("mutation") or {}
        out.append(f"tests: {v['tests']} accepted   coverage: {v.get('coverage')}   "
                   f"dev mutants killed: {mut.get('killed')}/{mut.get('total')}   "
                   f"plan cited: {(v.get('plan_coverage') or {}).get('ratio')}")
    for r in state["reviews"]:
        out.append(f"review r{r['round']}: {r['decision']}  " +
                   ", ".join(f"{v['test']}={v['judgement']}" for v in r["verdicts"]))
    if state["suspected_bugs"]:
        out.append(f"suspected bugs: {len(state['suspected_bugs'])} -> {run_dir / 'bug_report.md'}")
    for d in state["degraded"]:
        out.append(f"recovered: {d}")
    out.append("usage: " + json.dumps(state["usage"]))
    out.append(f"run dir: {run_dir}")
    return "\n".join(out)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target", nargs="?", help="Python module to test")
    ap.add_argument("--mock", choices=SCENARIOS, help="offline scripted scenario")
    ap.add_argument("--no-planner", action="store_true")
    ap.add_argument("--no-reviewer", action="store_true")
    ap.add_argument("--rounds", type=int, default=2, help="max TestGen rounds (revise loop cap)")
    ap.add_argument("--runs", type=Path, default=ROOT / "runs")
    ap.add_argument("--resume", type=Path, help="run directory to continue")
    ap.add_argument("--run-dir", type=Path, help="exact run directory to create (default: runs/<timestamp>)")
    a = ap.parse_args(argv)

    scenario = Scenario(a.mock) if a.mock else None
    if a.resume:
        run_dir = a.resume.resolve()
        state = json.loads((run_dir / "state.json").read_text(encoding="utf-8"))
        if state["next"] == "END":
            print(summary(state, run_dir))
            return 0
    else:
        target = Path(a.target) if a.target else (scenario.target if scenario else None)
        if target is None:
            ap.error("give a target module or --mock SCENARIO")
        run_dir = (a.runs / time.strftime("%Y%m%d-%H%M%S")).resolve()
        if a.mock:
            run_dir = run_dir.with_name(run_dir.name + "-" + a.mock)
        if a.run_dir:
            run_dir = a.run_dir.resolve()
        ws = run_dir / "workspace"
        ws.mkdir(parents=True)
        shutil.copyfile(target, ws / "solution.py")
        state = new_state((ws / "solution.py").read_text(encoding="utf-8"), ws,
                          planner=not a.no_planner, reviewer=not a.no_reviewer, max_rounds=a.rounds)
        state["target"] = str(target)
    ctx = mock_context(run_dir, scenario) if scenario else real_context(run_dir)
    state = run(state, ctx)
    print(summary(state, run_dir))
    return 0 if state["status"] in ("accepted", "completed", "forced") else 1


if __name__ == "__main__":
    raise SystemExit(main())
