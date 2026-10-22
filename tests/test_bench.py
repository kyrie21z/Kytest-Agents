"""Benchmark plumbing: asset validity and scoring, checked offline with known answers."""
import json

import pytest

from bench.lib import apply_patch, load_tasks
from bench.score import score_job
from bench.validate import check


def task(tid):
    return load_tasks(ids=[tid])[0]


def fake_job(tmp_path, condition, config="mas", suite=None, suspected=None):
    job = tmp_path / "t" / condition / config / "r1"
    run = job / "run"
    run.mkdir(parents=True)
    (run / "state.json").write_text(json.dumps({"status": "accepted", "round": 1, "next": "END",
                                                "usage": {"planner": {"calls": 1, "tokens": 10}}}))
    (run / "log.jsonl").write_text('{"t": 0}\n{"t": 5}\n')
    if suite:
        (run / "test_solution.py").write_text(suite)
    if suspected:
        (run / "test_suspected_bugs.py").write_text(suspected)
    return job


def test_split_is_five_dev_and_nine_frozen_test_tasks():
    tasks = load_tasks()
    assert len(tasks) == 14
    assert sum(t.meta["split"] == "dev" for t in tasks) == 5


@pytest.mark.parametrize("tid", ["qb_get_factors", "orig_allocate"])
def test_assets_are_valid(tid):
    assert check(task(tid)) == []


def test_patch_anchor_must_be_unique():
    with pytest.raises(ValueError, match="2 times"):
        apply_patch("x = 1\nx = 1\n", [["x = 1", "x = 2"]], "demo")


def test_gold_suite_on_clean_target_kills_every_bug_without_false_positives(tmp_path):
    t = task("qb_get_factors")
    row = score_job(t, "clean", fake_job(tmp_path, "clean", suite=(t.root / "gold_test.py").read_text()))
    assert (row["kill_rate"], row["fp_rate"], row["false_bug_reports"]) == (1.0, 0.0, 0)
    assert row["tests"] > 5 and row["tokens"] == 10 and row["seconds"] == 5


def test_over_specified_suite_is_a_false_positive_on_the_legal_alternative(tmp_path):
    over = "from solution import get_factors\ndef test_zero():\n    assert get_factors(0) == [0]\n"
    row = score_job(task("qb_get_factors"), "clean", fake_job(tmp_path, "clean", suite=over))
    assert row["fp_rate"] == 1.0


def test_buggy_target_report_and_fossil_are_measured_against_the_reference(tmp_path):
    # Upstream bug: get_factors(101) returns [] instead of [101].
    correct = "from solution import get_factors\ndef test_prime():\n    assert get_factors(101) == [101]\n"
    fossil = "from solution import get_factors\ndef test_prime_fossil():\n    assert get_factors(101) == []\n"
    wrong_report = "from solution import get_factors\ndef test_bad():\n    assert get_factors(4) == [4]\n"
    row = score_job(task("qb_get_factors"), "buggy",
                    fake_job(tmp_path, "buggy", suite=fossil, suspected=correct + "\n" + wrong_report))
    assert (row["reported"], row["true_reports"], row["false_reports"], row["fossilized"]) == (True, 1, 1, True)


def test_a_test_that_hangs_on_the_bug_counts_as_detecting_it(tmp_path):
    # Upstream find_first_in_sorted bug loops forever when x is below every element.
    hang = "from solution import find_first_in_sorted\ndef test_below():\n    assert find_first_in_sorted([3, 4], 1) == -1\n"
    ok = "from solution import find_first_in_sorted\ndef test_hit():\n    assert find_first_in_sorted([3, 4, 4], 4) == 1\n"
    row = score_job(task("qb_find_first_in_sorted"), "buggy", fake_job(tmp_path, "buggy", suite=ok, suspected=hang))
    assert (row["reported"], row["true_reports"], row["false_reports"]) == (True, 1, 0)
