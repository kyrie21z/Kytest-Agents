"""Run workflow configurations over benchmark tasks, in parallel and resumably.

    python bench/run.py --split dev --configs mas single --name dev1 --jobs 4

Two conditions per task:
  clean   the target is the correct reference implementation
  buggy   the target is the task's primary bug variant (oracle-contamination probe)
Each job gets results/bench/<name>/<task>/<condition>/<config>/r<k>/ containing
input/solution.py (the only file the workflow sees) and run/ (the workflow's
run directory). Finished jobs are skipped, so a rerun only fills the gaps.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from bench.lib import load_tasks  # noqa: E402

CONFIGS = {"mas": [], "no_planner": ["--no-planner"], "no_reviewer": ["--no-reviewer"],
           "single": ["--no-planner", "--no-reviewer"]}
CONDITIONS = ("clean", "buggy")
JOB_TIMEOUT = 1800


def finished(run_dir: Path) -> bool:
    try:
        return json.loads((run_dir / "state.json").read_text())["next"] == "END"
    except (OSError, ValueError, KeyError):
        return False


def run_job(task, condition, config, rep, out: Path, python: str) -> dict:
    job = out / task.id / condition / config / f"r{rep}"
    run_dir = job / "run"
    if finished(run_dir):
        return {"job": str(job), "skipped": True}
    if (run_dir / "state.json").exists():  # an interrupted attempt: resume it rather than start over
        cmd = [python, str(ROOT / "kytest.py"), "--resume", str(run_dir)]
    else:
        shutil.rmtree(run_dir, ignore_errors=True)  # died before the first checkpoint
        (job / "input").mkdir(parents=True, exist_ok=True)
        source = task.solution if condition == "clean" else task.primary_bug
        (job / "input" / "solution.py").write_text(source, encoding="utf-8")
        cmd = [python, str(ROOT / "kytest.py"), str(job / "input" / "solution.py"),
               "--run-dir", str(run_dir), *CONFIGS[config]]
    started = time.time()
    try:
        proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=JOB_TIMEOUT)
        log = proc.stdout + proc.stderr
        code = proc.returncode
    except subprocess.TimeoutExpired:
        log, code = "job timeout", -1
    job.mkdir(parents=True, exist_ok=True)
    (job / "stdout.txt").write_text(log, encoding="utf-8")
    return {"job": str(job), "code": code, "seconds": round(time.time() - started)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--name", required=True, help="results/bench/<name>")
    ap.add_argument("--split", choices=("dev", "test"))
    ap.add_argument("--tasks", nargs="*")
    ap.add_argument("--configs", nargs="*", default=list(CONFIGS), choices=list(CONFIGS))
    ap.add_argument("--conditions", nargs="*", default=list(CONDITIONS), choices=CONDITIONS)
    ap.add_argument("--reps", type=int, default=1)
    ap.add_argument("--jobs", type=int, default=4)
    a = ap.parse_args()
    out = ROOT / "results" / "bench" / a.name
    tasks = load_tasks(a.split, a.tasks)
    plan = [(t, c, cfg, r) for r in range(1, a.reps + 1) for t in tasks for c in a.conditions for cfg in a.configs]
    print(f"{len(plan)} jobs -> {out}", flush=True)
    with ThreadPoolExecutor(a.jobs) as pool:
        futures = [pool.submit(run_job, *job, out, sys.executable) for job in plan]
        for i, f in enumerate(as_completed(futures), 1):
            print(f"[{i}/{len(plan)}] {json.dumps(f.result())}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
