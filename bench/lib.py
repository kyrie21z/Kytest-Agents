"""Benchmark tasks: loading, variant materialisation and isolated pytest runs.

A task directory holds the public target (solution.py) and hidden assets that
only the evaluator sees: gold_test.py (+ optional gold_extra_test.py), bug
variants and legal alternative implementations described in meta.json.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List

TASKS = Path(__file__).resolve().parent / "tasks"
PYTEST_TIMEOUT = 30


def apply_patch(source: str, patch: List[List[str]], label: str) -> str:
    for old, new in patch:
        count = source.count(old)
        if count != 1:
            raise ValueError(f"{label}: patch anchor occurs {count} times: {old[:60]!r}")
        source = source.replace(old, new)
    return source


@dataclass
class Task:
    root: Path
    meta: Dict

    @property
    def id(self) -> str:
        return self.meta["id"]

    @property
    def solution(self) -> str:
        return (self.root / "solution.py").read_text(encoding="utf-8")

    def gold(self) -> Dict[str, str]:
        files = {"test_gold.py": (self.root / "gold_test.py").read_text(encoding="utf-8")}
        extra = self.root / "gold_extra_test.py"
        if extra.exists():
            files["test_gold_extra.py"] = extra.read_text(encoding="utf-8")
        return files

    def _variant(self, spec: Dict, label: str) -> str:
        if "file" in spec:
            return (self.root / spec["file"]).read_text(encoding="utf-8")
        return apply_patch(self.solution, spec["patch"], label)

    def bugs(self) -> Dict[str, str]:
        return {name: self._variant(spec, f"{self.id}/bug/{name}") for name, spec in self.meta["bugs"].items()}

    def alts(self) -> Dict[str, str]:
        return {name: self._variant(spec, f"{self.id}/alt/{name}") for name, spec in self.meta["alts"].items()}

    @property
    def primary_bug(self) -> str:
        return self.bugs()[self.meta["primary_bug"]]


def load_tasks(split: str | None = None, ids: List[str] | None = None) -> List[Task]:
    tasks = [Task(d, json.loads((d / "meta.json").read_text(encoding="utf-8")))
             for d in sorted(TASKS.iterdir()) if (d / "meta.json").exists()]
    if split:
        tasks = [t for t in tasks if t.meta["split"] == split]
    if ids:
        tasks = [t for t in tasks if t.id in ids]
    return tasks


@dataclass
class PytestRun:
    passed: int
    failed: int
    errors: int
    timed_out: bool
    output: str
    outcomes: Dict[str, bool] = field(default_factory=dict)  # "file::test[param]" -> passed

    @property
    def all_pass(self) -> bool:
        return not self.timed_out and self.failed == 0 and self.errors == 0 and self.passed > 0

    @property
    def any_fail(self) -> bool:
        return self.timed_out or self.failed > 0 or self.errors > 0


def run_pytest(solution: str, tests: Dict[str, str], python: str = sys.executable,
               timeout: int = PYTEST_TIMEOUT, select: str | None = None) -> PytestRun:
    """Run test files against one implementation in a fresh directory."""
    with tempfile.TemporaryDirectory(prefix="kbench-") as tmp:
        root = Path(tmp)
        (root / "solution.py").write_text(solution, encoding="utf-8")
        for name, text in tests.items():
            (root / name).write_text(text, encoding="utf-8")
        cmd = [python, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--tb=line",
               "--junitxml=report.xml", "-o", "junit_family=xunit1", *tests]
        if select:  # one exact node id, e.g. "test_x.py::test_name"
            cmd = cmd[:-len(tests)] + [select]
        try:
            proc = subprocess.run(cmd, cwd=root, capture_output=True, text=True, timeout=timeout)
        except subprocess.TimeoutExpired as exc:
            return PytestRun(0, 0, 0, True, str(exc.stdout or "")[-1500:])
        out = proc.stdout + proc.stderr
        outcomes = {}
        if (root / "report.xml").exists():
            for case in ET.parse(root / "report.xml").iter("testcase"):
                key = f"{case.get('file') or case.get('classname')}::{case.get('name')}"
                outcomes[key] = not any(child.tag in ("failure", "error") for child in case)
        def count(word):
            m = re.search(rf"(\d+) {word}", out.splitlines()[-1] if out.strip() else "")
            return int(m.group(1)) if m else 0
        errors = count("error")
        if proc.returncode not in (0, 1) and not errors:
            errors = 1  # collection/usage errors: nothing ran
        return PytestRun(count("passed"), count("failed"), errors, False, out[-1500:], outcomes)
