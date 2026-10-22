# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

from solution import find_first_in_sorted

def test_not_found_returns_minus_one():
    """When x is not in arr, contract says return -1."""
    # Contract: 'or -1 if x not in arr'
    result = find_first_in_sorted([1, 2, 3], 4)
    assert result == -1

from solution import find_first_in_sorted

def test_not_found_small_value():
    """When x is smaller than all elements, contract says return -1."""
    # Contract: 'or -1 if x not in arr'
    result = find_first_in_sorted([2, 3, 4], 1)
    assert result == -1

from solution import find_first_in_sorted

def test_single_element_not_found():
    """Single-element array where the element does not match."""
    # Contract: 'or -1 if x not in arr'
    result = find_first_in_sorted([5], 3)
    assert result == -1
