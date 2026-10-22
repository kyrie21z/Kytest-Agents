# Accepted by submit_tests; explanations in testgen_report.json.

from solution import find_first_in_sorted as _case0_find_first_in_sorted

def test_docstring_example():
    """Test the exact example from the docstring."""
    result = _case0_find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5)
    assert result == 2

from solution import find_first_in_sorted as _case1_find_first_in_sorted

def test_first_of_duplicates():
    """Find first occurrence when value appears multiple times consecutively."""
    result = _case1_find_first_in_sorted([1, 2, 2, 2, 3], 2)
    assert result == 1

from solution import find_first_in_sorted as _case2_find_first_in_sorted

def test_single_element_found():
    """Single-element array where the element matches."""
    result = _case2_find_first_in_sorted([5], 5)
    assert result == 0

from solution import find_first_in_sorted as _case3_find_first_in_sorted

def test_last_element_found():
    """Find value at the last index of a sorted array."""
    result = _case3_find_first_in_sorted([1, 2, 3], 3)
    assert result == 2

from solution import find_first_in_sorted as _case4_find_first_in_sorted

def test_two_elements_both_found():
    """Two-element array, find each element."""
    assert _case4_find_first_in_sorted([1, 2], 1) == 0
    assert _case4_find_first_in_sorted([1, 2], 2) == 1

from solution import find_first_in_sorted as _case5_find_first_in_sorted

def test_all_same_elements():
    """All elements are identical; first occurrence should be index 0."""
    result = _case5_find_first_in_sorted([7, 7, 7, 7], 7)
    assert result == 0

from solution import find_first_in_sorted as _case6_find_first_in_sorted

def test_negative_numbers():
    """Search in array with negative values."""
    result = _case6_find_first_in_sorted([-5, -3, 0, 3, 5], -3)
    assert result == 1

from solution import find_first_in_sorted as _case7_find_first_in_sorted

def test_return_type_int():
    """Verify return type is always int."""
    result = _case7_find_first_in_sorted([1, 2, 3], 2)
    assert isinstance(result, int)

from solution import find_first_in_sorted as _case8_find_first_in_sorted

def test_large_duplicate_block():
    """Large block of duplicates; verify first index is correct."""
    arr = [4] + [5] * 50
    result = _case8_find_first_in_sorted(arr, 5)
    assert result == 1
