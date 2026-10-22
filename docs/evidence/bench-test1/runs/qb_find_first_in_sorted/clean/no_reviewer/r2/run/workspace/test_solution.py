# Accepted by submit_tests; explanations in testgen_report.json.

"""Test P1: Element found at the first position."""
from solution import find_first_in_sorted as _case0_find_first_in_sorted

def test_p1_first_position():
    """Element found at the first position.
    Spec: 'lowest index i such that arr[i] == x'. Index 0 is the first position.
    Input domain: arr=[1,2,3], x=1 (sorted list of ints, value present at index 0).
    Expected: 0. Fault hypothesis: Returns non-zero index or -1 when element is at start."""
    assert _case0_find_first_in_sorted([1, 2, 3], 1) == 0

"""Test P3: Element found in the middle."""
from solution import find_first_in_sorted as _case1_find_first_in_sorted

def test_p3_middle_position():
    """Element found in the middle.
    Spec: 'lowest index i such that arr[i] == x'. Index 1 is the middle position.
    Input domain: arr=[1,2,3], x=2 (sorted list of ints, value present at middle).
    Expected: 1. Fault hypothesis: Returns wrong index for middle elements."""
    assert _case1_find_first_in_sorted([1, 2, 3], 2) == 1

"""Test P4: Empty list input."""
from solution import find_first_in_sorted as _case2_find_first_in_sorted

def test_p4_empty_list():
    """Empty list input.
    Spec: '-1 if x not in arr'. Empty list contains no elements.
    Input domain: arr=[], x=5 (empty sorted list).
    Expected: -1. Fault hypothesis: Raises IndexError or returns non-negative value."""
    assert _case2_find_first_in_sorted([], 5) == -1

"""Test P5: Multiple duplicates, returns first index."""
from solution import find_first_in_sorted as _case3_find_first_in_sorted

def test_p5_duplicates_returns_first():
    """Multiple duplicates, returns first index.
    Spec: 'lowest index i such that arr[i] == x'. First occurrence is at index 0.
    Input domain: arr=[5,5,5,5], x=5 (all identical values in sorted list).
    Expected: 0. Fault hypothesis: Returns a later duplicate index instead of first."""
    assert _case3_find_first_in_sorted([5, 5, 5, 5], 5) == 0

"""Test P6: Value not present in list."""
from solution import find_first_in_sorted as _case4_find_first_in_sorted

def test_p6_not_present():
    """Value not present in list.
    Spec: '-1 if x not in arr'. Value 2 is not in the list.
    Input domain: arr=[1,3,5], x=2 (sorted list with gaps, target absent).
    Expected: -1. Fault hypothesis: Returns a valid index when value is absent."""
    assert _case4_find_first_in_sorted([1, 3, 5], 2) == -1

"""Test P2: Element found at the last position."""
from solution import find_first_in_sorted as _case5_find_first_in_sorted

def test_p2_last_position():
    """Element found at the last position.
    Spec: 'lowest index i such that arr[i] == x'. Index 2 is the last position.
    Input domain: arr=[1,2,3], x=3 (sorted list of ints, value present at last index).
    Expected: 2. Fault hypothesis: Returns wrong index when element is at end."""
    assert _case5_find_first_in_sorted([1, 2, 3], 3) == 2

"""Test P7: Single element list, value matches."""
from solution import find_first_in_sorted as _case6_find_first_in_sorted

def test_p7_single_element_match():
    """Single element list, value matches.
    Spec: 'lowest index i such that arr[i] == x'. Index 0 matches.
    Input domain: arr=[10], x=10 (single-element list, exact match).
    Expected: 0. Fault hypothesis: Returns -1 for single-element match."""
    assert _case6_find_first_in_sorted([10], 10) == 0

"""Test P8: Single element list, value does not match."""
from solution import find_first_in_sorted as _case7_find_first_in_sorted

def test_p8_single_element_no_match():
    """Single element list, value does not match.
    Spec: '-1 if x not in arr'. Value 5 is not in the list.
    Input domain: arr=[10], x=5 (single-element list, no match).
    Expected: -1. Fault hypothesis: Returns 0 when value doesn't match."""
    assert _case7_find_first_in_sorted([10], 5) == -1

"""Test P9: Negative integers."""
from solution import find_first_in_sorted as _case8_find_first_in_sorted

def test_p9_negative_integers():
    """Negative integers.
    Spec: 'sorted list of ints'. Negative integers are valid inputs.
    Input domain: arr=[-5,-2,0], x=-2 (sorted list with negatives, target present).
    Expected: 1. Fault hypothesis: Fails on negative integer comparisons."""
    assert _case8_find_first_in_sorted([-5, -2, 0], -2) == 1

"""Test P10: Large sorted list with gaps."""
from solution import find_first_in_sorted as _case9_find_first_in_sorted

def test_p10_large_gaps_absent():
    """Large sorted list with gaps.
    Spec: '-1 if x not in arr'. Value 15 is not present.
    Input domain: arr=[1,10,20,30], x=15 (sparse sorted list, target absent).
    Expected: -1. Fault hypothesis: Returns wrong index due to gap handling bug."""
    assert _case9_find_first_in_sorted([1, 10, 20, 30], 15) == -1

"""Extra: Docstring example verification."""
from solution import find_first_in_sorted as _case10_find_first_in_sorted

def test_extra_docstring_example():
    """Docstring example: find_first_in_sorted([3,4,5,5,5,5,6], 5) -> 2.
    Input domain: arr=[3,4,5,5,5,5,6], x=5 (multiple duplicates, first 5 at index 2).
    Expected: 2. Fault hypothesis: Returns index 3,4,or 5 instead of first occurrence at 2."""
    assert _case10_find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5) == 2

"""Extra: Return type check."""
from solution import find_first_in_sorted as _case11_find_first_in_sorted

def test_extra_return_type():
    """Return type is always int.
    Contract: Output is an int (index or -1).
    Input domain: Various valid inputs including empty, single, and multi-element lists.
    Expected: Return value is always an instance of int.
    Fault hypothesis: Detects unexpected return types like None, float, or string."""
    for arr, x in [([], 1), ([1], 1), ([1], 2), ([1, 2, 3], 2), ([5, 5, 5], 5)]:
        result = _case11_find_first_in_sorted(arr, x)
        assert isinstance(result, int), f'Expected int, got {type(result)}'

"""Extra: Two-element list, both present and absent cases."""
from solution import find_first_in_sorted as _case12_find_first_in_sorted

def test_extra_two_elements():
    """Two-element sorted list with various search targets.
    Input domain: Small sorted lists of length 2.
    Expected: Correct index for present value, -1 for absent.
    Fault hypothesis: Off-by-one errors in small arrays."""
    assert _case12_find_first_in_sorted([1, 2], 1) == 0
    assert _case12_find_first_in_sorted([1, 2], 2) == 1
    assert _case12_find_first_in_sorted([1, 2], 0) == -1
    assert _case12_find_first_in_sorted([1, 2], 3) == -1

"""Extra: All elements same value, search for different value."""
from solution import find_first_in_sorted as _case13_find_first_in_sorted

def test_extra_all_same_value_absent():
    """All elements identical, target absent.
    Input domain: arr=[7,7,7,7,7], x=3 (all identical, target absent).
    Expected: -1. Fault hypothesis: Returns some index due to binary search misstep."""
    assert _case13_find_first_in_sorted([7, 7, 7, 7, 7], 3) == -1

"""Extra: Search for value between two adjacent elements."""
from solution import find_first_in_sorted as _case14_find_first_in_sorted

def test_extra_boundary_between_values():
    """Search for value strictly between two adjacent elements.
    Input domain: arr=[1,3], x=2 (value lies strictly between arr[0] and arr[1]).
    Expected: -1. Fault hypothesis: Returns 0 or 1 incorrectly."""
    assert _case14_find_first_in_sorted([1, 3], 2) == -1
