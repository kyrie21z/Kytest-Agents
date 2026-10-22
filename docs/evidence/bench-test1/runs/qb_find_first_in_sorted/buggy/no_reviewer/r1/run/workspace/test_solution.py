# Accepted by submit_tests; explanations in testgen_report.json.

from solution import find_first_in_sorted as _case0_find_first_in_sorted

def test_p1_middle_duplicates():
    """Find first occurrence in middle with duplicates.

    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr=[3, 4, 5, 5, 5, 5, 6], x=5
    Expected result: 2, matching the docstring example.
    Fault hypothesis: Implementation returns a later duplicate index (e.g., 3, 4, or 5)
                      instead of the first occurrence.
    """
    assert _case0_find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5) == 2

from solution import find_first_in_sorted as _case1_find_first_in_sorted

def test_p2_start():
    """Find element at the start of the list.

    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr=[1, 2, 3, 4], x=1
    Expected result: 0, the first position.
    Fault hypothesis: Implementation skips index 0 or returns a wrong index.
    """
    assert _case1_find_first_in_sorted([1, 2, 3, 4], 1) == 0

from solution import find_first_in_sorted as _case2_find_first_in_sorted

def test_p3_end():
    """Find element at the end of the list.

    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr=[1, 2, 3, 4], x=4
    Expected result: 3, the last position.
    Fault hypothesis: Implementation misses the last element due to off-by-one in hi bound.
    """
    assert _case2_find_first_in_sorted([1, 2, 3, 4], 4) == 3

from solution import find_first_in_sorted as _case3_find_first_in_sorted

def test_p7_all_identical():
    """All elements are identical duplicates.

    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr=[7, 7, 7, 7], x=7
    Expected result: 0, the first position among many duplicates.
    Fault hypothesis: Implementation returns a non-zero index among the duplicates.
    """
    assert _case3_find_first_in_sorted([7, 7, 7, 7], 7) == 0

from solution import find_first_in_sorted as _case4_find_first_in_sorted

def test_extra_single_present():
    """Single-element list where target is present.

    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr=[42], x=42
    Expected result: 0, the only index.
    Fault hypothesis: Implementation returns -1 incorrectly for a present element.
    """
    assert _case4_find_first_in_sorted([42], 42) == 0

from solution import find_first_in_sorted as _case5_find_first_in_sorted

def test_extra_negative_numbers():
    """Sorted list with negative numbers.

    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr=[-5, -3, 0, 3, 7], x=-3
    Expected result: 1.
    Fault hypothesis: Implementation mishandles negative values in comparisons.
    """
    assert _case5_find_first_in_sorted([-5, -3, 0, 3, 7], -3) == 1

from solution import find_first_in_sorted as _case6_find_first_in_sorted

def test_extra_two_elements_found():
    """Two-element list, target is the first element.

    Contract quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr=[1, 5], x=1
    Expected result: 0.
    Fault hypothesis: Off-by-one causes the search to skip the first element.
    """
    assert _case6_find_first_in_sorted([1, 5], 1) == 0
