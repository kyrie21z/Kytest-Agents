# Accepted by submit_tests; explanations in testgen_report.json.

from solution import find_first_in_sorted as _case0_find_first_in_sorted

def test_basic_first_occurrence():
    """Test finding the first occurrence of a value in a sorted array with duplicates."""
    result = _case0_find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5)
    assert result == 2

from solution import find_first_in_sorted as _case1_find_first_in_sorted

def test_element_not_present():
    """Test that -1 is returned when x is not in arr."""
    result = _case1_find_first_in_sorted([1, 2, 3, 4, 5], 6)
    assert result == -1
    result2 = _case1_find_first_in_sorted([1, 2, 3, 4, 5], 0)
    assert result2 == -1

from solution import find_first_in_sorted as _case2_find_first_in_sorted

def test_empty_array():
    """Test behavior with empty array input."""
    result = _case2_find_first_in_sorted([], 5)
    assert result == -1

from solution import find_first_in_sorted as _case3_find_first_in_sorted

def test_single_element_match():
    """Test finding the only element in a single-element array."""
    result = _case3_find_first_in_sorted([42], 42)
    assert result == 0

from solution import find_first_in_sorted as _case4_find_first_in_sorted

def test_all_same_elements():
    """Test when all elements in the array are identical."""
    result = _case4_find_first_in_sorted([7, 7, 7, 7, 7], 7)
    assert result == 0
    result2 = _case4_find_first_in_sorted([7, 7, 7, 7, 7], 7)
    assert isinstance(result2, int)

from solution import find_first_in_sorted as _case5_find_first_in_sorted

def test_negative_and_boundary_values():
    """Test with negative numbers and edge positions (first and last element)."""
    result1 = _case5_find_first_in_sorted([-5, -3, 0, 2, 8], -5)
    assert result1 == 0
    result2 = _case5_find_first_in_sorted([-5, -3, 0, 2, 8], 8)
    assert result2 == 4
    result3 = _case5_find_first_in_sorted([-5, -5, -5, 0, 2], -5)
    assert result3 == 0
