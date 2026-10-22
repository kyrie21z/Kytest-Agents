# Accepted by submit_tests; explanations in testgen_report.json.

from solution import find_first_in_sorted as _case0_find_first_in_sorted

def test_p1_middle():
    result = _case0_find_first_in_sorted([10, 20, 30, 40, 50], 30)
    assert result == 2

from solution import find_first_in_sorted as _case1_find_first_in_sorted

def test_p2_beginning():
    result = _case1_find_first_in_sorted([10, 20, 30], 10)
    assert result == 0

from solution import find_first_in_sorted as _case2_find_first_in_sorted

def test_p3_end():
    result = _case2_find_first_in_sorted([10, 20, 30], 30)
    assert result == 2

from solution import find_first_in_sorted as _case3_find_first_in_sorted

def test_p5_duplicates():
    result = _case3_find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5)
    assert result == 2

from solution import find_first_in_sorted as _case4_find_first_in_sorted

def test_p8_single_match():
    result = _case4_find_first_in_sorted([7], 7)
    assert result == 0

from solution import find_first_in_sorted as _case5_find_first_in_sorted

def test_extra_negative_values():
    result = _case5_find_first_in_sorted([-5, -3, 0, 3, 5], -3)
    assert result == 1

from solution import find_first_in_sorted as _case6_find_first_in_sorted

def test_extra_all_same():
    result = _case6_find_first_in_sorted([5, 5, 5, 5], 5)
    assert result == 0

from solution import find_first_in_sorted as _case7_find_first_in_sorted

def test_extra_large_gap():
    result = _case7_find_first_in_sorted([1, 100, 200, 300, 400], 100)
    assert result == 1
    result2 = _case7_find_first_in_sorted([1, 100, 200, 300, 400], 300)
    assert result2 == 3

from solution import find_first_in_sorted as _case8_find_first_in_sorted

def test_extra_three_dupes_at_start():
    result = _case8_find_first_in_sorted([5, 5, 5, 10, 20], 5)
    assert result == 0

from solution import find_first_in_sorted as _case9_find_first_in_sorted

def test_extra_three_dupes_at_end():
    result = _case9_find_first_in_sorted([1, 2, 7, 7, 7], 7)
    assert result == 2
