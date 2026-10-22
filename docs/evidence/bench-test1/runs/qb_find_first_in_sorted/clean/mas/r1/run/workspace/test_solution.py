# Accepted by submit_tests; explanations in testgen_report.json.

from solution import find_first_in_sorted as _case0_find_first_in_sorted

def test_p1_middle_duplicates():
    """Find first occurrence in middle with surrounding duplicates."""
    assert _case0_find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5) == 2

from solution import find_first_in_sorted as _case1_find_first_in_sorted

def test_p2_beginning():
    """Find element at the beginning of the list."""
    assert _case1_find_first_in_sorted([1, 2, 3], 1) == 0

from solution import find_first_in_sorted as _case2_find_first_in_sorted

def test_p3_end():
    """Find element at the end of the list."""
    assert _case2_find_first_in_sorted([1, 2, 3], 3) == 2

from solution import find_first_in_sorted as _case3_find_first_in_sorted

def test_p4_not_present():
    """Target value not present in list."""
    assert _case3_find_first_in_sorted([1, 2, 3], 4) == -1

from solution import find_first_in_sorted as _case4_find_first_in_sorted

def test_p5_empty():
    """Empty input list."""
    assert _case4_find_first_in_sorted([], 5) == -1

from solution import find_first_in_sorted as _case5_find_first_in_sorted

def test_p6_all_identical():
    """All elements are identical duplicates."""
    assert _case5_find_first_in_sorted([7, 7, 7, 7], 7) == 0

from solution import find_first_in_sorted as _case6_find_first_in_sorted

def test_p7_smaller_than_all():
    """Target value smaller than all elements."""
    assert _case6_find_first_in_sorted([10, 20, 30], 5) == -1

from solution import find_first_in_sorted as _case7_find_first_in_sorted

def test_p8_larger_than_all():
    """Target value larger than all elements."""
    assert _case7_find_first_in_sorted([10, 20, 30], 40) == -1
