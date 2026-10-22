# Accepted by submit_tests; explanations in testgen_report.json.

from solution import kth as _case0_kth

def test_kth_boundary_first_and_last():
    """
    'The kth-lowest element of arr (0-based)'

    Boundary checks: k=0 should yield the minimum, k=len-1 the maximum.
    Input domain: arr=[5,3,1,4,2], k=0 and k=4.
    Expected: min=1, max=5.
    Fault hypothesis: if the recursion shifts incorrectly, the extremes
    may not be found at the boundaries.
    """
    assert _case0_kth([5, 3, 1, 4, 2], 0) == 1
    assert _case0_kth([5, 3, 1, 4, 2], 4) == 5

from solution import kth as _case1_kth

def test_kth_single_element():
    """
    'The kth-lowest element of arr (0-based)'

    Edge case: single-element array, k=0.
    Input domain: arr=[42], k=0.
    Expected: 42.
    Fault hypothesis: accessing arr[0] on a degenerate list could fail
    or return wrong value if base case is mishandled.
    """
    assert _case1_kth([42], 0) == 42

from solution import kth as _case2_kth

def test_kth_all_same_elements():
    """
    'The kth-lowest element of arr (0-based)'

    Duplicate-heavy case: all elements identical. Every element equals
    the pivot, so below=[] and above=[], num_less=0, num_lessoreq=len.
    Any valid k falls in the else branch returning pivot.
    Input domain: arr=[7,7,7,7], k=0 and k=3.
    Expected: 7 for both.
    Fault hypothesis: if duplicate handling were broken, one might get
    an infinite recursion or IndexError.
    """
    assert _case2_kth([7, 7, 7, 7], 0) == 7
    assert _case2_kth([7, 7, 7, 7], 3) == 7
