# Accepted by submit_tests; explanations in testgen_report.json.

"""Test that the first occurrence of a duplicated value is returned."""
from solution import find_first_in_sorted as _case0_find_first_in_sorted

def test_found_first_of_duplicates():
    """
    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr = [3, 4, 5, 5, 5, 5, 6], x = 5
    Expected result: 2 — the first 5 is at index 2.
    Fault hypothesis: A binary search that does not check left neighbors may
      return any index among the duplicates (e.g., 3 or 4).
    """
    assert _case0_find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5) == 2

"""Test returning -1 when the target is absent."""
from solution import find_first_in_sorted as _case1_find_first_in_sorted

def test_not_found():
    """
    Contract quote: 'or -1 if x not in arr'
    Input domain: arr = [1, 2, 3, 4, 5], x = 6
    Expected result: -1 — 6 is outside the sorted range.
    Fault hypothesis: Implementation might return a wrong index or raise instead of -1.
    """
    assert _case1_find_first_in_sorted([1, 2, 3, 4, 5], 6) == -1

"""Test empty array input."""
from solution import find_first_in_sorted as _case2_find_first_in_sorted

def test_empty_array():
    """
    Contract quote: 'A sorted list of ints' — empty list is a valid sorted list.
    Input domain: arr = [], x = 1
    Expected result: -1 — nothing to find.
    Fault hypothesis: Accessing arr[mid] on empty array causes IndexError.
    """
    assert _case2_find_first_in_sorted([], 1) == -1

"""Test single-element array where the element matches."""
from solution import find_first_in_sorted as _case3_find_first_in_sorted

def test_single_element_found():
    """
    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr = [42], x = 42
    Expected result: 0 — the sole element matches.
    Fault hypothesis: Off-by-one may skip the single-element iteration.
    """
    assert _case3_find_first_in_sorted([42], 42) == 0

"""Test target at the very first position."""
from solution import find_first_in_sorted as _case4_find_first_in_sorted

def test_target_at_index_zero():
    """
    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr = [1, 2, 3, 4, 5], x = 1
    Expected result: 0 — target is the first element.
    Fault hypothesis: Guard `(mid == 0 or ...)` may fail to short-circuit correctly,
      causing arr[mid-1] access at mid==0.
    """
    assert _case4_find_first_in_sorted([1, 2, 3, 4, 5], 1) == 0

"""Test array where every element equals the target."""
from solution import find_first_in_sorted as _case5_find_first_in_sorted

def test_all_elements_same_as_target():
    """
    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr = [7, 7, 7, 7, 7], x = 7
    Expected result: 0 — all match, so the leftmost index is 0.
    Fault hypothesis: With all duplicates, search may converge to a middle index.
    """
    assert _case5_find_first_in_sorted([7, 7, 7, 7, 7], 7) == 0

"""Test target at the very last position."""
from solution import find_first_in_sorted as _case6_find_first_in_sorted

def test_target_at_last_index():
    """
    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr = [1, 2, 3, 4, 5], x = 5
    Expected result: 4 — target is the last element.
    Fault hypothesis: hi = len(arr) means upper bound is exclusive; off-by-one
      could prevent reaching the last element.
    """
    assert _case6_find_first_in_sorted([1, 2, 3, 4, 5], 5) == 4

"""Test array with negative integers."""
from solution import find_first_in_sorted as _case7_find_first_in_sorted

def test_negative_numbers():
    """
    Contract quote: 'A sorted list of ints' — includes negative integers.
    Input domain: arr = [-5, -3, -1, 0, 2, 4], x = -3
    Expected result: 1 — -3 is at index 1.
    Fault hypothesis: Comparison may mishandle negatives if there's an implicit
      assumption about positive-only inputs.
    """
    assert _case7_find_first_in_sorted([-5, -3, -1, 0, 2, 4], -3) == 1

"""Test duplicates but target absent."""
from solution import find_first_in_sorted as _case8_find_first_in_sorted

def test_duplicate_values_target_not_present():
    """
    Contract quote: 'or -1 if x not in arr'
    Input domain: arr = [5, 5, 5, 5], x = 3
    Expected result: -1 — 3 is not in the array.
    Fault hypothesis: With duplicate-heavy arrays, search might get stuck or
      return a spurious index near the duplicates.
    """
    assert _case8_find_first_in_sorted([5, 5, 5, 5], 3) == -1

"""Test two-element array where both equal target."""
from solution import find_first_in_sorted as _case9_find_first_in_sorted

def test_two_elements_both_match():
    """
    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr = [7, 7], x = 7
    Expected result: 0 — both match, lowest index is 0.
    Fault hypothesis: Small-array binary search may miscompute mid and skip index 0.
    """
    assert _case9_find_first_in_sorted([7, 7], 7) == 0

"""Test single-element array where element does not match."""
from solution import find_first_in_sorted as _case10_find_first_in_sorted

def test_single_element_not_found():
    """
    Contract quote: 'or -1 if x not in arr'
    Input domain: arr = [42], x = 99
    Expected result: -1 — the sole element does not match.
    Fault hypothesis: Might incorrectly return 0 due to boundary logic error.
    """
    assert _case10_find_first_in_sorted([42], 99) == -1

"""Test finding a value between blocks of duplicates."""
from solution import find_first_in_sorted as _case11_find_first_in_sorted

def test_target_between_duplicates():
    """
    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr = [1, 1, 3, 3, 3, 7, 7, 7, 7], x = 3
    Expected result: 2 — first 3 is at index 2.
    Fault hypothesis: Binary search may land in the middle of the 3-block and
      fail to narrow left past the preceding 1s.
    """
    assert _case11_find_first_in_sorted([1, 1, 3, 3, 3, 7, 7, 7, 7], 3) == 2
