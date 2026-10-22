"""Check every task's hidden assets before any agent sees the benchmark.

    python bench/validate.py [--task ID ...]

A task is valid when the gold tests pass on the reference and on every legal
alternative, fail on every bug variant, and each variant really differs.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from bench.lib import load_tasks, run_pytest  # noqa: E402


def check(task) -> list:
    problems, gold = [], task.gold()
    ref = run_pytest(task.solution, gold)
    if not ref.all_pass:
        problems.append(f"gold fails on reference:\n{ref.output}")
    for kind, variants, want_pass in (("alt", task.alts, True), ("bug", task.bugs, False)):
        try:
            items = variants()
        except ValueError as exc:
            problems.append(str(exc))
            continue
        for name, source in items.items():
            if source == task.solution:
                problems.append(f"{kind} {name} is identical to the reference")
                continue
            r = run_pytest(source, gold)
            if want_pass and not r.all_pass:
                problems.append(f"alt {name} fails gold (not a legal alternative):\n{r.output}")
            if not want_pass and not r.any_fail:
                problems.append(f"bug {name} survives gold (needs gold_extra_test.py)")
    if task.meta["primary_bug"] not in task.meta["bugs"]:
        problems.append("primary_bug not among bugs")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", nargs="*")
    a = ap.parse_args()
    bad = 0
    for task in load_tasks(ids=a.task):
        problems = check(task)
        bad += bool(problems)
        print(f"{'OK  ' if not problems else 'FAIL'} {task.id} [{task.meta['tier']}/{task.meta['split']}] "
              f"bugs={len(task.meta['bugs'])} alts={len(task.meta['alts'])}")
        for p in problems:
            print("     - " + p.replace("\n", "\n       "))
    print(f"{bad} invalid task(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
