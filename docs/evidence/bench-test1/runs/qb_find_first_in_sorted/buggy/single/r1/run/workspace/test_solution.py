# Accepted by submit_tests; explanations in testgen_report.json.

"""Test the example from the docstring."""
from solution import find_first_in_sorted as _case0_find_first_in_sorted

def test_docstring_example():
    """
    Contract quote: 'The lowest index i such that arr[i] == x, or -1 if x not in arr'
    Input domain: arr = [3, 4, 5, 5, 5, 5, 6], x = 5
    Oracle: The first occurrence of 5 is at index 2.
    Fault hypothesis: Detects off-by-one errors or returning any index other than 2
      for duplicate-element searches.
    """
    result = _case0_find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5)
    assert result == 2

"""Test single element that matches."""
from solution import find_first_in_sorted as _case1_find_first_in_sorted

def test_single_element_match():
    """
    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr = [7], x = 7
    Oracle: Only element matches, first occurrence at index 0.
    Fault hypothesis: Detects returning -1 for a present single-element array.
    """
    result = _case1_find_first_in_sorted([7], 7)
    assert result == 0

"""Test array where all elements are the same."""
from solution import find_first_in_sorted as _case2_find_first_in_sorted

def test_all_same_elements():
    """
    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr = [5, 5, 5, 5], x = 5
    Oracle: All elements are 5, first occurrence at index 0.
    Fault hypothesis: Detects returning non-zero index for all-same arrays.
    """
    result = _case2_find_first_in_sorted([5, 5, 5, 5], 5)
    assert result == 0

"""Test two duplicates in the middle."""
from solution import find_first_in_sorted as _case3_find_first_in_sorted

def test_two_duplicates_middle():
    """
    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr = [1, 2, 2, 3, 4], x = 2
    Oracle: First occurrence of 2 is at index 1.
    Fault hypothesis: Detects returning index 2 instead of 1.
    """
    result = _case3_find_first_in_sorted([1, 2, 2, 3, 4], 2)
    assert result == 1

"""Test finding first and last elements of array."""
from solution import find_first_in_sorted as _case4_find_first_in_sorted

def test_first_and_last_elements():
    """
    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr = [1, 3, 5, 7, 9], x = 1 and x = 9
    Oracle: First element at index 0, last element at index 4.
    Fault hypothesis: Detects boundary failures missing endpoints.
    """
    from solution import find_first_in_sorted
    assert find_first_in_sorted([1, 3, 5, 7, 9], 1) == 0
    assert find_first_in_sorted([1, 3, 5, 7, 9], 9) == 4

"""Test that return value is always an integer."""
from solution import find_first_in_sorted as _case5_find_first_in_sorted

def test_return_type_is_int():
    """
    Contract quote: Output is 'The lowest index i ... or -1' — both are integers.
    Input domain: arr = [1, 2, 3], x = 2
    Oracle: Return value must be an int.
    Fault hypothesis: Detects incorrect return types (None, str, etc.).
    """
    result = _case5_find_first_in_sorted([1, 2, 3], 2)
    assert isinstance(result, int)

"""Test with negative values."""
from solution import find_first_in_sorted as _case6_find_first_in_sorted

def test_negative_values():
    """
    Contract quote: 'A sorted list of ints'
    Input domain: arr = [-5, -3, -1, 0, 2], x = -3
    Oracle: -3 is at index 1.
    Fault hypothesis: Detects incorrect handling of negative numbers.
    """
    result = _case6_find_first_in_sorted([-5, -3, -1, 0, 2], -3)
    assert result == 1

"""Test duplicates at the start of array."""
from solution import find_first_in_sorted as _case7_find_first_in_sorted

def test_three_duplicates_at_start():
    """
    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr = [3, 3, 3, 7, 9], x = 3
    Oracle: First occurrence of 3 is at index 0.
    Fault hypothesis: Detects returning index > 0 for duplicates at start.
    """
    result = _case7_find_first_in_sorted([3, 3, 3, 7, 9], 3)
    assert result == 0

"""Test with a larger even-sized sorted array."""
from solution import find_first_in_sorted as _case8_find_first_in_sorted

def test_large_even_sized_array():
    """
    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr = list(range(100)), x = 50
    Oracle: 50 is at index 50.
    Fault hypothesis: Detects off-by-one errors in larger arrays.
    """
    result = _case8_find_first_in_sorted(list(range(100)), 50)
    assert result == 50

"""Test finding element at a specific middle position."""
from solution import find_first_in_sorted as _case9_find_first_in_sorted

def test_value_at_index_3_of_7():
    """
    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr = [10, 20, 30, 40, 50, 60, 70], x = 40
    Oracle: 40 is at index 3.
    Fault hypothesis: Detects wrong index for middle-element searches.
    """
    result = _case9_find_first_in_sorted([10, 20, 30, 40, 50, 60, 70], 40)
    assert result == 3
