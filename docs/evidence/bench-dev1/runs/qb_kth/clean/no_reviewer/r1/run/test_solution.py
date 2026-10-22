# Accepted by submit_tests; explanations in testgen_report.json.

"""P1: Returns the correct k-th smallest element for a standard unsorted list.

Contract quote: "This is an efficient equivalent to sorted(arr)[k]."
Input domain: arr=[4,1,7,3,9], k=2 satisfies 0 <= k < len(arr).
Expected: sorted([4,1,7,3,9]) = [1,3,4,7,9]; index 2 yields 4.
Faulty behavior detected: returning any value other than 4.
"""
from solution import kth as _case0_kth

def test_p1_standard_unsorted():
    assert _case0_kth([4, 1, 7, 3, 9], 2) == 4

"""P2: Returns the minimum element when k=0.

Contract quote: "The kth-lowest element of arr (0-based)".
Input domain: arr=[10,5,8], k=0 satisfies 0 <= k < len(arr).
Expected: min([10,5,8]) = 5.
Faulty behavior detected: returning 8 or 10 instead of 5.
"""
from solution import kth as _case1_kth

def test_p2_min_element():
    assert _case1_kth([10, 5, 8], 0) == 5

"""P3: Returns the maximum element when k=len(arr)-1.

Contract quote: "The kth-lowest element of arr (0-based)".
Input domain: arr=[10,5,8], k=2 satisfies 0 <= k < len(arr).
Expected: sorted([10,5,8]) = [5,8,10]; index 2 yields 10.
Faulty behavior detected: returning 5 or 8 instead of 10.
"""
from solution import kth as _case2_kth

def test_p3_max_element():
    assert _case2_kth([10, 5, 8], 2) == 10

"""P4: Handles a single-element list correctly.

Contract quote: precondition 0 <= k < len(arr).
Input domain: arr=[42], k=0 is valid (0 <= 0 < 1).
Expected: only element is 42, so result must be 42.
Faulty behavior detected: raising an exception or returning anything != 42.
"""
from solution import kth as _case3_kth

def test_p4_single_element():
    assert _case3_kth([42], 0) == 42

"""P5: Correctly resolves duplicates according to sort order.

Contract quote: "efficient equivalent to sorted(arr)[k]".
Input domain: arr=[3,3,1,3], k=1 satisfies 0 <= k < 4.
Expected: sorted([3,3,1,3]) = [1,3,3,3]; index 1 yields 3.
Faulty behavior detected: returning 1 (confusing duplicate handling).
"""
from solution import kth as _case4_kth

def test_p5_duplicates():
    assert _case4_kth([3, 3, 1, 3], 1) == 3

"""P6: Correctly handles negative integers.

Contract quote: "A list of ints" / "equivalent to sorted(arr)[k]".
Input domain: arr=[-2,-5,0,3], k=2 satisfies 0 <= k < 4.
Expected: sorted([-2,-5,0,3]) = [-5,-2,0,3]; index 2 yields 0.
Faulty behavior detected: mishandling sign comparison.
"""
from solution import kth as _case5_kth

def test_p6_negative_integers():
    assert _case5_kth([-2, -5, 0, 3], 2) == 0

"""P7: Works on pre-sorted input.

Contract quote: "efficient equivalent to sorted(arr)[k]" — no ordering assumption.
Input domain: arr=[1,2,3,4], k=3 satisfies 0 <= k < 4.
Expected: sorted([1,2,3,4]) = [1,2,3,4]; index 3 yields 4.
Faulty behavior detected: treating presorted as degenerate.
"""
from solution import kth as _case6_kth

def test_p7_presorted():
    assert _case6_kth([1, 2, 3, 4], 3) == 4

"""P8: Works on reverse-sorted input.

Contract quote: no ordering assumption; must work for any permutation.
Input domain: arr=[4,3,2,1], k=0 satisfies 0 <= k < 4.
Expected: sorted([4,3,2,1]) = [1,2,3,4]; index 0 yields 1.
Faulty behavior detected: worst-case partition failure.
"""
from solution import kth as _case7_kth

def test_p8_reversesorted():
    assert _case7_kth([4, 3, 2, 1], 0) == 1

"""P9: Handles minimal valid list length greater than one.

Contract quote: precondition 0 <= k < len(arr).
Input domain: arr=[9,1], k=1 satisfies 0 <= k < 2.
Expected: sorted([9,1]) = [1,9]; index 1 yields 9.
Faulty behavior detected: returning 1 instead of 9.
"""
from solution import kth as _case8_kth

def test_p9_minimal_length():
    assert _case8_kth([9, 1], 1) == 9

"""Extra: All elements identical — every k must return that value.

Contract quote: "efficient equivalent to sorted(arr)[k]".
Input domain: arr=[5,5,5,5], k=2 satisfies 0 <= k < 4.
Expected: sorted([5,5,5,5]) = [5,5,5,5]; index 2 yields 5.
Faulty behavior detected: failing when pivot equals all elements.
"""
from solution import kth as _case9_kth

def test_extra_all_same_values():
    assert _case9_kth([5, 5, 5, 5], 2) == 5

"""Extra: Mixed signs with duplicates — stress partition boundaries.

Contract quote: "efficient equivalent to sorted(arr)[k]".
Input domain: arr=[-1,2,-1,0,2], k=3 satisfies 0 <= k < 5.
Expected: sorted([-1,2,-1,0,2]) = [-1,-1,0,2,2]; index 3 yields 2.
Faulty behavior detected: incorrect handling of duplicates across sign boundary.
"""
from solution import kth as _case10_kth

def test_extra_mixed_signs_and_duplicates():
    assert _case10_kth([-1, 2, -1, 0, 2], 3) == 2

"""Extra: Verify the return type is int (not a list or None).

Contract quote: "Output: The kth-lowest element of arr (0-based)" — implies a scalar.
Input domain: arr=[10,20], k=0.
Expected: isinstance(result, int) and result == 10.
Faulty behavior detected: returning a list, tuple, or None.
"""
from solution import kth as _case11_kth

def test_extra_return_type():
    result = _case11_kth([10, 20], 0)
    assert isinstance(result, int)
    assert result == 10
