# Accepted by submit_tests; explanations in testgen_report.json.

from solution import find_first_in_sorted as _case0_find_first_in_sorted

def test_p1_find_unique():
    """Find unique existing element."""
    result = _case0_find_first_in_sorted([1, 2, 3], 2)
    assert result == 1

from solution import find_first_in_sorted as _case1_find_first_in_sorted

def test_p2_first_of_duplicates():
    """Find first occurrence among duplicates."""
    result = _case1_find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5)
    assert result == 2

from solution import find_first_in_sorted as _case2_find_first_in_sorted

def test_p5_single_match():
    """Single element array, matches target."""
    result = _case2_find_first_in_sorted([5], 5)
    assert result == 0

from solution import find_first_in_sorted as _case3_find_first_in_sorted

def test_p9_all_identical():
    """All elements identical and match target."""
    result = _case3_find_first_in_sorted([5, 5, 5], 5)
    assert result == 0

from solution import find_first_in_sorted as _case4_find_first_in_sorted

def test_extra_negative_numbers():
    """Sorted array with negative numbers."""
    result = _case4_find_first_in_sorted([-5, -3, 0, 2, 4], -3)
    assert result == 1

from solution import find_first_in_sorted as _case5_find_first_in_sorted

def test_extra_two_elements():
    """Array with exactly two elements, target is first."""
    result = _case5_find_first_in_sorted([1, 3], 1)
    assert result == 0

from solution import find_first_in_sorted as _case6_find_first_in_sorted

def test_extra_two_elements_last():
    """Array with exactly two elements, target is second."""
    result = _case6_find_first_in_sorted([1, 3], 3)
    assert result == 1

from solution import find_first_in_sorted as _case7_find_first_in_sorted

def test_extra_return_type():
    """Verify return type is always int."""
    r1 = _case7_find_first_in_sorted([1, 2, 3], 2)
    r2 = _case7_find_first_in_sorted([1, 2, 3], 1)
    assert isinstance(r1, int), f'Expected int, got {type(r1)}'
    assert isinstance(r2, int), f'Expected int, got {type(r2)}'
