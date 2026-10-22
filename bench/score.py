"""Score finished benchmark jobs against the hidden assets.

    python bench/score.py --name dev1

Per job (all measured by running the produced tests, never by trusting the agents):
  clean  condition: tests, bug kill rate over the bug variants the specification
         decides (kill_rate_all also counts the undecided ones), false-positive
         rate over legal alternatives, false bug reports (suspected tests on a
         correct target).
  buggy  condition: reported (a suspected-bug test passes on the reference and
         fails on the planted bug), false reports, fossilized (accepted tests
         that fail on the reference, i.e. the bug became an expected value).
Writes scores.jsonl and summary.md next to the jobs.
"""
from __future__ import annotations

import argparse
import json
import random
import statistics
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from bench.lib import load_tasks, run_pytest  # noqa: E402

SUITE, SUSPECTED = "test_solution.py", "test_suspected_bugs.py"


def _read(path: Path) -> str | None:
    return path.read_text(encoding="utf-8") if path.exists() else None


def _per_test(source: str, file: str, code: str) -> dict:
    run = run_pytest(source, {file: code})
    return {key.split("::", 1)[1]: ok for key, ok in run.outcomes.items()}, run


def score_job(task, condition: str, job: Path) -> dict:
    state = json.loads((job / "run" / "state.json").read_text(encoding="utf-8"))
    suite, suspected = _read(job / "run" / SUITE), _read(job / "run" / SUSPECTED)
    log = [json.loads(line) for line in (job / "run" / "log.jsonl").read_text().splitlines() if line.strip()]
    usage = state.get("usage") or {}
    row = {"task": task.id, "tier": task.meta["tier"], "split": task.meta["split"], "condition": condition,
           "config": job.parent.name, "rep": job.name, "status": state["status"], "rounds": state["round"],
           "seconds": round(log[-1]["t"] - log[0]["t"]) if log else None,
           "tokens": sum(u.get("tokens", 0) for u in usage.values()),
           "calls": sum(u.get("calls", 0) for u in usage.values())}
    ref_suite, _ = _per_test(task.solution, SUITE, suite) if suite else ({}, None)
    row["tests"] = len(ref_suite)
    row["tests_failing_on_reference"] = sum(not ok for ok in ref_suite.values())
    ref_sus, _ = _per_test(task.solution, SUSPECTED, suspected) if suspected else ({}, None)
    row["suspected"] = len(ref_sus)
    if condition == "clean":
        bugs, alts = task.bugs(), task.alts()
        killed = {n: suite is not None and run_pytest(src, {SUITE: suite}).any_fail for n, src in bugs.items()}
        flagged = {n: suite is not None and run_pytest(src, {SUITE: suite}).any_fail for n, src in alts.items()}
        decided = [n for n in bugs if task.meta["bugs"][n].get("spec_decided", True)]
        row.update(kill_rate=sum(killed[n] for n in decided) / len(decided),
                   kill_rate_all=sum(killed.values()) / len(bugs), killed=[n for n, k in killed.items() if k],
                   fp_rate=sum(flagged.values()) / len(alts), false_positive_alts=[n for n, f in flagged.items() if f],
                   false_bug_reports=sum(not ok for ok in ref_sus.values()))
    else:
        bug_sus, _ = _per_test(task.primary_bug, SUSPECTED, suspected) if suspected else ({}, None)
        true = [n for n, ok in ref_sus.items() if ok and bug_sus.get(n) is False]
        row.update(reported=bool(true), true_reports=len(true), false_reports=len(ref_sus) - len(true),
                   fossilized=row["tests_failing_on_reference"] > 0)
    return row


def mean_ci(values, n_boot=2000, seed=0):
    values = [float(v) for v in values if v is not None]
    if not values:
        return None, None, None
    rng = random.Random(seed)
    boots = sorted(statistics.fmean(rng.choices(values, k=len(values))) for _ in range(n_boot))
    return statistics.fmean(values), boots[int(0.025 * n_boot)], boots[int(0.975 * n_boot) - 1]


def fmt(values, pct=True):
    m, lo, hi = mean_ci(values)
    if m is None:
        return "–"
    f = (lambda x: f"{100 * x:.0f}%") if pct else (lambda x: f"{x:.1f}")
    return f"{f(m)} [{f(lo)}, {f(hi)}]"


def summarise(rows) -> str:
    by = defaultdict(list)
    for r in rows:
        by[(r["condition"], r["config"])].append(r)
    configs = sorted({r["config"] for r in rows}, key=["mas", "no_planner", "no_reviewer", "single"].index)
    out = [f"# Benchmark summary ({len(rows)} jobs)", "",
           "Means over jobs with bootstrap 95% intervals (resampling jobs). Small samples: descriptive only.", "",
           "## Clean target (reference implementation)", "",
           "| config | jobs | tests | bug kill rate | false-positive rate (legal alts) | false bug reports |",
           "|---|---|---|---|---|---|"]
    for c in configs:
        rs = by[("clean", c)]
        if rs:
            out.append(f"| {c} | {len(rs)} | {fmt([r['tests'] for r in rs], False)} | {fmt([r['kill_rate'] for r in rs])} | "
                       f"{fmt([r['fp_rate'] for r in rs])} | {fmt([r['false_bug_reports'] for r in rs], False)} |")
    out += ["", "## Buggy target (primary bug planted; oracle-contamination probe)", "",
            "| config | jobs | bug reported | fossilized (bug baked into accepted tests) | false reports |",
            "|---|---|---|---|---|"]
    for c in configs:
        rs = by[("buggy", c)]
        if rs:
            out.append(f"| {c} | {len(rs)} | {fmt([r['reported'] for r in rs])} | {fmt([r['fossilized'] for r in rs])} | "
                       f"{fmt([r['false_reports'] for r in rs], False)} |")
    out += ["", "## Cost per job", "", "| config | seconds | tokens | LLM calls (roles) |", "|---|---|---|---|"]
    for c in configs:
        rs = [r for r in rows if r["config"] == c]
        out.append(f"| {c} | {fmt([r['seconds'] for r in rs], False)} | {fmt([r['tokens'] for r in rs], False)} | "
                   f"{fmt([r['calls'] for r in rs], False)} |")
    out += ["", "## Per task", "", "| task | tier | condition | config | status | tests | kill | fp | reported | fossilized |",
            "|---|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda r: (r["task"], r["condition"], r["config"], r["rep"])):
        out.append(f"| {r['task']} | {r['tier']} | {r['condition']} | {r['config']} | {r['status']} | {r['tests']} | "
                   f"{r.get('kill_rate', '') if r['condition'] == 'clean' else ''} | {r.get('fp_rate', '')} | "
                   f"{r.get('reported', '')} | {r.get('fossilized', '')} |")
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    a = ap.parse_args()
    out = ROOT / "results" / "bench" / a.name
    tasks = {t.id: t for t in load_tasks()}
    rows = []
    for state in sorted(out.glob("*/*/*/r*/run/state.json")):
        job = state.parent.parent
        task, condition = job.parts[-4], job.parts[-3]
        if json.loads(state.read_text()).get("next") != "END":
            print("unfinished:", job)
            continue
        rows.append(score_job(tasks[task], condition, job))
        print(json.dumps(rows[-1]), flush=True)
    (out / "scores.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")
    (out / "summary.md").write_text(summarise(rows), encoding="utf-8")
    print(out / "summary.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
