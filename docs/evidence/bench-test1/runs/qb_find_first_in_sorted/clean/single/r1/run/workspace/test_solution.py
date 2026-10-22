# Accepted by submit_tests; explanations in testgen_report.json.

from solution import find_first_in_sorted as _case0_find_first_in_sorted

def test_docstring_example():
    """Quote: '>>> find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5)' -> 2

    Input domain: sorted list with multiple duplicates of target value.
    Expected: index 2, the first occurrence of 5.
    Fault hypothesis: returning any index > 2 (e.g. 3, 4, or 5) would
    indicate the function fails to locate the *first* duplicate.
    """
    assert _case0_find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5) == 2

from solution import find_first_in_sorted as _case1_find_first_in_sorted

def test_empty_array():
    """Quote: 'or -1 if x not in arr' — an empty array contains nothing.

    Input domain: empty list.
    Expected: -1.
    Fault hypothesis: accessing arr[0] or miscomputing indices on an
    empty list could raise IndexError or return a bogus index.
    """
    assert _case1_find_first_in_sorted([], 5) == -1

from solution import find_first_in_sorted as _case2_find_first_in_sorted

def test_single_element_match():
    """Quote: 'The lowest index i such that arr[i] == x'

    Input domain: single-element list where that element equals x.
    Expected: 0.
    Fault hypothesis: off-by-one errors could return -1 or 1.
    """
    assert _case2_find_first_in_sorted([42], 42) == 0

from solution import find_first_in_sorted as _case3_find_first_in_sorted

def test_all_same_elements():
    """Quote: 'The lowest index i such that arr[i] == x'

    Input domain: list where every element equals x.
    Expected: 0 (the very first index).
    Fault hypothesis: the function might return len(arr)-1 or any
    other index instead of the first one.
    """
    assert _case3_find_first_in_sorted([7, 7, 7, 7, 7], 7) == 0

from solution import find_first_in_sorted as _case4_find_first_in_sorted

def test_element_not_present():
    """Quote: 'or -1 if x not in arr'

    Input domain: sorted list where x does not appear.
    Expected: -1.
    Fault hypothesis: returning a valid index instead of -1 means the
    function incorrectly claims the value was found.
    """
    assert _case4_find_first_in_sorted([1, 2, 3, 4, 5], 6) == -1

from solution import find_first_in_sorted as _case5_find_first_in_sorted

def test_negative_numbers():
    """Quote: 'A sorted list of ints' — negatives are valid ints.

    Input domain: sorted list containing negative integers.
    Expected: index 1 for value -3.
    Fault hypothesis: sign handling bugs could produce wrong comparisons.
    """
    assert _case5_find_first_in_sorted([-5, -3, 0, 2, 4], -3) == 1
