# Accepted by submit_tests; explanations in testgen_report.json.

from solution import find_first_in_sorted as _case0_find_first_in_sorted

def test_p1_single_occurrence():
    """Find target with single occurrence.
    
    Spec states output is 'The lowest index i such that arr[i] == x'.
    Index 1 is the unique match.
    """
    result = _case0_find_first_in_sorted([10, 20, 30], 20)
    assert result == 1

from solution import find_first_in_sorted as _case1_find_first_in_sorted

def test_p2_first_among_duplicates():
    """Find first occurrence among duplicates.
    
    Directly matches the provided docstring example demonstrating
    duplicate handling: find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5) -> 2.
    """
    result = _case1_find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5)
    assert result == 2

from solution import find_first_in_sorted as _case2_find_first_in_sorted

def test_p3_target_at_start():
    """Target located at the start of the list.
    
    Spec requires returning the 'lowest index i'; when the first element
    matches, index 0 is correct.
    """
    result = _case2_find_first_in_sorted([1, 2, 3], 1)
    assert result == 0

from solution import find_first_in_sorted as _case3_find_first_in_sorted

def test_p4_target_at_end():
    """Target located at the end of the list.
    
    Spec requires returning the 'lowest index i'; when the last element
    matches, its index is returned.
    """
    result = _case3_find_first_in_sorted([1, 2, 3], 3)
    assert result == 2

from solution import find_first_in_sorted as _case4_find_first_in_sorted

def test_p7_single_element_match():
    """Single-element list with match.
    
    Degenerate boundary case; the only valid index is 0, satisfying
    the 'lowest index' requirement.
    """
    result = _case4_find_first_in_sorted([42], 42)
    assert result == 0

from solution import find_first_in_sorted as _case5_find_first_in_sorted

def test_p9_negative_integers():
    """Handle negative integers.
    
    Spec specifies 'list of ints'; negative values are valid integers
    and should resolve to their correct index.
    """
    result = _case5_find_first_in_sorted([-10, -5, 0, 5], -5)
    assert result == 1

from solution import find_first_in_sorted as _case6_find_first_in_sorted

def test_p10_all_identical():
    """All elements identical.
    
    Spec requires the 'lowest index i'; when every element matches,
    index 0 is the mathematical minimum.
    """
    result = _case6_find_first_in_sorted([7, 7, 7, 7], 7)
    assert result == 0
