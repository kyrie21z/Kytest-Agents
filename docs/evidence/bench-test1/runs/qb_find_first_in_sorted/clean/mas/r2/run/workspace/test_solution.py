# Accepted by submit_tests; explanations in testgen_report.json.

"""Test P1: Returns index of unique target."""
from solution import find_first_in_sorted as _case0_find_first_in_sorted

def test_p1_unique_target():
    """P1: Returns index of unique target.
    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr=[1, 3, 5, 7], x=3 — sorted list, target present once.
    Expected: 1 because arr[1] == 3 and it is the only occurrence.
    Fault hypothesis: detects off-by-one errors (e.g. returning 0 or 2).
    """
    assert _case0_find_first_in_sorted([1, 3, 5, 7], 3) == 1

"""Test P2: Returns first index among duplicates."""
from solution import find_first_in_sorted as _case1_find_first_in_sorted

def test_p2_first_index_among_duplicates():
    """P2: Returns first index among duplicates.
    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr=[3, 4, 5, 5, 5, 5, 6], x=5 — sorted list with repeated target.
    Expected: 2 because arr[2]==5 and indices 3,4,5 also hold 5; we want the lowest.
    Fault hypothesis: detects returning a later duplicate index instead of the first.
    """
    assert _case1_find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5) == 2

"""Test P3: Target located at the start of the list."""
from solution import find_first_in_sorted as _case2_find_first_in_sorted

def test_p3_target_at_start():
    """P3: Target located at the start of the list.
    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr=[10, 20, 30], x=10 — target is the very first element.
    Expected: 0 because arr[0] == 10.
    Fault hypothesis: detects skipping the first element (e.g. returning -1 or 1).
    """
    assert _case2_find_first_in_sorted([10, 20, 30], 10) == 0

"""Test P4: Target located at the end of the list."""
from solution import find_first_in_sorted as _case3_find_first_in_sorted

def test_p4_target_at_end():
    """P4: Target located at the end of the list.
    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr=[10, 20, 30], x=30 — target is the last element.
    Expected: 2 because arr[2] == 30 and len(arr)-1 == 2.
    Fault hypothesis: detects boundary error where hi=len(arr) causes out-of-range or missed last element.
    """
    assert _case3_find_first_in_sorted([10, 20, 30], 30) == 2

"""Test P5: Handles empty input list."""
from solution import find_first_in_sorted as _case4_find_first_in_sorted

def test_p5_empty_list():
    """P5: Handles empty input list.
    Contract quote: '-1 if x not in arr'
    Input domain: arr=[], x=5 — empty list, no elements can match.
    Expected: -1 because x cannot be in an empty list.
    Fault hypothesis: detects IndexError from accessing arr[mid] when len(arr)==0.
    """
    assert _case4_find_first_in_sorted([], 5) == -1

"""Test P6: Target not present in list."""
from solution import find_first_in_sorted as _case5_find_first_in_sorted

def test_p6_target_not_present():
    """P6: Target not present in list.
    Contract quote: '-1 if x not in arr'
    Input domain: arr=[1, 3, 5], x=4 — sorted list, 4 falls between 3 and 5.
    Expected: -1 because 4 is not in the list.
    Fault hypothesis: detects returning a wrong index due to incorrect mid calculation.
    """
    assert _case5_find_first_in_sorted([1, 3, 5], 4) == -1

"""Test P7: Single-element list with matching target."""
from solution import find_first_in_sorted as _case6_find_first_in_sorted

def test_p7_single_element_matching():
    """P7: Single-element list with matching target.
    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr=[42], x=42 — degenerate sorted list, one element equals x.
    Expected: 0 because arr[0] == 42.
    Fault hypothesis: detects failure on minimal non-empty input.
    """
    assert _case6_find_first_in_sorted([42], 42) == 0

"""Test P8: Single-element list with non-matching target."""
from solution import find_first_in_sorted as _case7_find_first_in_sorted

def test_p8_single_element_non_matching():
    """P8: Single-element list with non-matching target.
    Contract quote: '-1 if x not in arr'
    Input domain: arr=[42], x=99 — degenerate sorted list, element != x.
    Expected: -1 because 99 is not in the list.
    Fault hypothesis: detects returning 0 incorrectly when the single element doesn't match.
    """
    assert _case7_find_first_in_sorted([42], 99) == -1

"""Extra: Works with negative integers in a sorted list."""
from solution import find_first_in_sorted as _case8_find_first_in_sorted

def test_extra_negative_values():
    """Extra: Works with negative integers in a sorted list.
    Contract quote: 'A sorted list of ints' / 'The lowest index i such that arr[i] == x'
    Input domain: arr=[-5, -3, 0, 2, 7], x=-3 — sorted list with negatives.
    Expected: 1 because arr[1] == -3.
    Fault hypothesis: detects sign-related bugs in comparison logic.
    """
    assert _case8_find_first_in_sorted([-5, -3, 0, 2, 7], -3) == 1

"""Extra: All elements are the same value, target matches."""
from solution import find_first_in_sorted as _case9_find_first_in_sorted

def test_extra_all_same_elements():
    """Extra: All elements are the same value, target matches.
    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr=[7, 7, 7, 7], x=7 — every element equals x.
    Expected: 0 because the lowest index with arr[i]==7 is 0.
    Fault hypothesis: detects binary search failing to converge to index 0 when all values are equal.
    """
    assert _case9_find_first_in_sorted([7, 7, 7, 7], 7) == 0

"""Extra: Return type is always int."""
from solution import find_first_in_sorted as _case10_find_first_in_sorted

def test_extra_return_type_check():
    """Extra: Return type is always int.
    Contract quote: Output is an index (int) or -1 (int).
    Input domain: Various inputs including edge cases.
    Expected: return value is always an instance of int.
    Fault hypothesis: detects unexpected return types (e.g. None, float).
    """
    result = _case10_find_first_in_sorted([1, 2, 3], 2)
    assert isinstance(result, int)
    result = _case10_find_first_in_sorted([], 1)
    assert isinstance(result, int)
