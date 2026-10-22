# Accepted by submit_tests; explanations in testgen_report.json.

from solution import lis as _case0_lis

def test_empty_array():
    """Empty input should yield LIS length 0."""
    assert _case0_lis([]) == 0

from solution import lis as _case1_lis

def test_single_element():
    """A single-element array has LIS length 1."""
    assert _case1_lis([42]) == 1

from solution import lis as _case2_lis

def test_sorted_array():
    """A fully sorted array has LIS equal to its length."""
    assert _case2_lis([1, 2, 3, 4, 5]) == 5

from solution import lis as _case3_lis

def test_reverse_sorted():
    """A reverse-sorted array has LIS length 1."""
    assert _case3_lis([5, 4, 3, 2, 1]) == 1

from solution import lis as _case4_lis

def test_complex_lis():
    """Classic LIS problem: [10,9,2,5,3,7,101,18]."""
    assert _case4_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
