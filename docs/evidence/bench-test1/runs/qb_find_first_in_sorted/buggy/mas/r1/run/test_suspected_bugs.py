# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

from solution import find_first_in_sorted

def test_p5_empty_list():
    """Search in an empty list.
    
    Spec states to return '-1 if x not in arr'; an empty list contains
    no elements to match.
    """
    result = find_first_in_sorted([], 5)
    assert result == -1

from solution import find_first_in_sorted

def test_p6_target_absent():
    """Target absent between existing elements.
    
    Spec states to return '-1 if x not in arr'; 4 is not present in the
    sorted sequence [1, 3, 5, 7].
    """
    result = find_first_in_sorted([1, 3, 5, 7], 4)
    assert result == -1

from solution import find_first_in_sorted

def test_p8_single_element_no_match():
    """Single-element list without match.
    
    Degenerate boundary case; x is not in arr, so the spec dictates
    returning -1.
    """
    result = find_first_in_sorted([42], 99)
    assert result == -1
