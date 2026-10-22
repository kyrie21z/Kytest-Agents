# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

from solution import find_first_in_sorted

def test_p3_not_present():
    """Target not present in array."""
    # Contract quote: 'or -1 if x not in arr'
    result = find_first_in_sorted([1, 2, 3], 4)
    assert result == -1

from solution import find_first_in_sorted

def test_p4_empty_list():
    """Empty input array."""
    # Contract quote: 'or -1 if x not in arr'; empty list has no elements, so x not in arr
    result = find_first_in_sorted([], 1)
    assert result == -1

from solution import find_first_in_sorted

def test_p6_single_no_match():
    """Single element array, does not match target."""
    # Contract quote: 'or -1 if x not in arr'
    result = find_first_in_sorted([5], 3)
    assert result == -1

from solution import find_first_in_sorted

def test_p7_target_smaller():
    """Target smaller than all elements."""
    # Contract quote: 'or -1 if x not in arr'
    result = find_first_in_sorted([2, 3, 4], 1)
    assert result == -1

from solution import find_first_in_sorted

def test_p8_target_larger():
    """Target larger than all elements."""
    # Contract quote: 'or -1 if x not in arr'
    result = find_first_in_sorted([2, 3, 4], 5)
    assert result == -1
