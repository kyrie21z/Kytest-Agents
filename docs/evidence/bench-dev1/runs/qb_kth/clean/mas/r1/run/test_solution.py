# Accepted by submit_tests; explanations in testgen_report.json.

from solution import kth as _case0_kth

def test_p1_typical_unsorted():
    """P1: Returns correct kth smallest for typical unsorted list.
    Input: arr=[3, 1, 4, 1, 5, 9], k=2.
    sorted([3,1,4,1,5,9]) = [1,1,3,4,5,9]; index 2 is 3."""
    result = _case0_kth([3, 1, 4, 1, 5, 9], 2)
    assert result == 3

from solution import kth as _case1_kth

def test_p5_duplicate_values():
    """P5: Correctly ranks duplicate values as distinct positions.
    Input: arr=[5, 5, 5, 1, 1], k=3.
    sorted([5,5,5,1,1]) = [1,1,5,5,5]; index 3 is 5."""
    result = _case1_kth([5, 5, 5, 1, 1], 3)
    assert result == 5

from solution import kth as _case2_kth

def test_p2_lower_k_bound():
    """P2: Returns minimum element at lower k bound (k=0).
    Input: arr=[10, 20, 30], k=0.
    sorted([10,20,30])[0] = 10."""
    result = _case2_kth([10, 20, 30], 0)
    assert result == 10

from solution import kth as _case3_kth

def test_p3_upper_k_bound():
    """P3: Returns maximum element at upper k bound (k=len(arr)-1).
    Input: arr=[7, 2, 9], k=2.
    sorted([7,2,9])[2] = 9."""
    result = _case3_kth([7, 2, 9], 2)
    assert result == 9

from solution import kth as _case4_kth

def test_p4_single_element():
    """P4: Handles single-element list.
    Input: arr=[42], k=0.
    sorted([42])[0] = 42."""
    result = _case4_kth([42], 0)
    assert result == 42

from solution import kth as _case5_kth

def test_p6_negative_integers():
    """P6: Correctly orders and selects negative integers.
    Input: arr=[-5, 10, -2, 0, 3], k=1.
    sorted([-5,10,-2,0,3]) = [-5,-2,0,3,10]; index 1 is -2."""
    result = _case5_kth([-5, 10, -2, 0, 3], 1)
    assert result == -2

from solution import kth as _case6_kth

def test_p7_permutation_invariant():
    """P7: Invariant holds regardless of initial order.
    Input: arr=[9, 7, 5, 3, 1], k=2.
    sorted([9,7,5,3,1]) = [1,3,5,7,9]; index 2 is 5."""
    result = _case6_kth([9, 7, 5, 3, 1], 2)
    assert result == 5

from solution import kth as _case7_kth

def test_p8_uniform_values():
    """P8: Degenerate case with uniform values.
    Input: arr=[4, 4, 4, 4], k=2.
    sorted([4,4,4,4])[2] = 4."""
    result = _case7_kth([4, 4, 4, 4], 2)
    assert result == 4

from solution import kth as _case8_kth

def test_extra_two_elements():
    """Extra: Two-element list at both bounds.
    Input: arr=[5, 3], k=0 and k=1.
    sorted([5,3]) = [3,5]; indices 0 and 1 give 3 and 5."""
    assert _case8_kth([5, 3], 0) == 3
    assert _case8_kth([5, 3], 1) == 5

from solution import kth as _case9_kth

def test_extra_large_k():
    """Extra: Large k near upper bound with many elements.
    Input: arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=9.
    sorted(...)[9] = 10."""
    result = _case9_kth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9)
    assert result == 10
