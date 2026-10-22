"""Build benchmark task skeletons from downloaded upstream benchmarks.

    python bench/import_sources.py --quixbugs DIR --classeval FILE --bigcodebench FILE

Writes bench/tasks/<id>/{solution.py, gold_test.py} plus, for QuixBugs, the
upstream human-written bug as bugs/upstream.py. Hand-written bugs, alternative
implementations and meta.json live next to them and are never overwritten.
Inputs are read as data only (json / ast); nothing from them is executed.
"""
from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path

TASKS = Path(__file__).resolve().parent / "tasks"

QUIXBUGS = ["to_base", "kth", "lis", "get_factors", "shunting_yard", "find_first_in_sorted"]
CLASSEVAL = {"ClassEval_75": "ce_shopping_cart", "ClassEval_8": "ce_bank_account",
             "ClassEval_95": "ce_warehouse", "ClassEval_94": "ce_vending_machine"}
# Upstream entry point is the generic `task_func`; a descriptive name reads like real code.
BIGCODEBENCH = {"BigCodeBench/928": ("bcb_bigram_counts", "bigram_counts"),
                "BigCodeBench/854": ("bcb_factorial_sums", "factorial_sums")}


def _with_docstring(fn: ast.FunctionDef, doc: str) -> ast.FunctionDef:
    body = fn.body
    if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) \
            and isinstance(body[0].value.value, str):
        body = body[1:]
    fn.body = [ast.Expr(ast.Constant(doc))] + body
    return fn


def _write(task: str, files: dict) -> None:
    root = TASKS / task
    for name, text in files.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text.rstrip("\n") + "\n", encoding="utf-8")
    print("wrote", task, sorted(files))


def quixbugs(repo: Path) -> None:
    for name in QUIXBUGS:
        buggy = ast.parse((repo / "python_programs" / f"{name}.py").read_text())
        doc = next(n.value.value for n in buggy.body if isinstance(n, ast.Expr)
                   and isinstance(n.value, ast.Constant) and isinstance(n.value.value, str))
        doc = "\n" + "\n".join(("    " + line).rstrip() for line in doc.strip("\n").splitlines()) + "\n    "
        correct = ast.parse((repo / "correct_python_programs" / f"{name}.py").read_text())

        def module(tree):
            imports = [n for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom))]
            fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name)
            return ast.unparse(ast.Module(imports + [_with_docstring(fn, doc)], [])) + "\n"

        cases = [json.loads(line) for line in (repo / "json_testcases" / f"{name}.json").read_text().splitlines() if line.strip()]
        gold = (f"import pytest\nfrom solution import {name}\n\nCASES = {cases!r}\n\n\n"
                f"@pytest.mark.parametrize('args, expected', CASES)\n"
                f"def test_upstream(args, expected):\n    assert {name}(*args) == expected\n")
        _write(f"qb_{name}", {"solution.py": module(correct), "bugs/upstream.py": module(buggy), "gold_test.py": gold})


def classeval(data: Path) -> None:
    tasks = {t["task_id"]: t for t in json.loads(data.read_text())}
    for tid, task in CLASSEVAL.items():
        t = tasks[tid]
        skeleton = next(n for n in ast.parse(t["skeleton"]).body if isinstance(n, ast.ClassDef))
        solution_tree = ast.parse(t["solution_code"])
        solution = next(n for n in solution_tree.body if isinstance(n, ast.ClassDef))
        docs = {n.name: ast.get_docstring(n, clean=False) for n in skeleton.body if isinstance(n, ast.FunctionDef)}
        for fn in solution.body:
            if isinstance(fn, ast.FunctionDef) and docs.get(fn.name):
                _with_docstring(fn, docs[fn.name])
        solution.body.insert(0, ast.Expr(ast.Constant(ast.get_docstring(skeleton, clean=False))))
        imports = [n for n in solution_tree.body if isinstance(n, (ast.Import, ast.ImportFrom))]
        source = ast.unparse(ast.Module(imports + [solution], [])) + "\n"
        gold = f"from solution import {t['class_name']}\n" + t["test"]
        _write(task, {"solution.py": source, "gold_test.py": gold})


def bigcodebench(data: Path) -> None:
    rows = {r["task_id"]: r for r in json.loads(data.read_text())}
    for tid, (task, entry) in BIGCODEBENCH.items():
        r = rows[tid]
        source = (r["complete_prompt"].rstrip("\n") + "\n" + r["canonical_solution"]).replace("task_func", entry)
        ast.parse(source)
        gold = f"from solution import {entry}\n" + r["test"].replace("task_func", entry)
        _write(task, {"solution.py": source, "gold_test.py": gold})


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quixbugs", type=Path, required=True, help="QuixBugs checkout")
    ap.add_argument("--classeval", type=Path, required=True, help="ClassEval_data.json")
    ap.add_argument("--bigcodebench", type=Path, required=True, help="bigcodebench-hard rows as JSON")
    a = ap.parse_args()
    quixbugs(a.quixbugs)
    classeval(a.classeval)
    bigcodebench(a.bigcodebench)


if __name__ == "__main__":
    main()
