# Accepted by submit_tests; explanations in testgen_report.json.

import solution as _case0_solution

def test_kth_single_element():
    """Single element list should return that element for k=0."""
    assert _case0_solution.kth([42], 0) == 42

import solution as _case1_solution

def test_kth_reverse_sorted():
    """Reverse-sorted array tests worst-case pivot selection."""
    arr = [5, 4, 3, 2, 1]
    for k in range(len(arr)):
        assert _case1_solution.kth(arr, k) == sorted(arr)[k]

import solution as _case2_solution

def test_kth_all_identical():
    """All identical elements: below and above are both empty."""
    assert _case2_solution.kth([7, 7, 7, 7], 0) == 7
    assert _case2_solution.kth([7, 7, 7, 7], 2) == 7
    assert _case2_solution.kth([7, 7, 7, 7], 3) == 7

import solution as _case3_solution

def test_kth_minimum_element():
    """k=0 should always return the minimum regardless of pivot choice."""
    assert _case3_solution.kth([9, 8, 7, 6, 5, 4, 3, 2, 1], 0) == 1
    assert _case3_solution.kth([100, 200, 50], 0) == 50
    assert _case3_solution.kth([-5, -3, -10, 0], 0) == -10

import solution as _case4_solution

def test_kth_descending_max_first():
    """Descending array: first element is max, so 'above' is always empty."""
    arr = [9, 7, 5, 3, 1]
    expected = sorted(arr)
    assert _case4_solution.kth(arr, 0) == expected[0]
    assert _case4_solution.kth(arr, 2) == expected[2]
    assert _case4_solution.kth(arr, 4) == expected[4]

import solution as _case5_solution

def test_kth_strictly_descending_full():
    """Strictly descending array: first element always max, above always empty."""
    arr = list(range(10, 0, -1))
    expected = sorted(arr)
    for k in range(len(arr)):
        assert _case5_solution.kth(arr, k) == expected[k]

import solution as _case6_solution

def test_kth_two_elements_k0():
    """Two-element descending: k=0 finds minimum."""
    assert _case6_solution.kth([3, 1], 0) == 1

import solution as _case7_solution

def test_kth_large_descending_mid():
    """Large descending array, mid-range k values."""
    arr = list(range(20, 0, -1))
    expected = sorted(arr)
    assert _case7_solution.kth(arr, 9) == expected[9]
    assert _case7_solution.kth(arr, 15) == expected[15]
    assert _case7_solution.kth(arr, 19) == expected[19]

import solution as _case8_solution

def test_kth_three_element_descending():
    """Three-element descending: exhaustively check all k."""
    arr = [3, 2, 1]
    expected = sorted(arr)
    for k in range(len(arr)):
        assert _case8_solution.kth(arr, k) == expected[k]

import solution as _case9_solution

def test_kth_return_type_check():
    """Verify return type is int for various valid inputs."""
    r1 = _case9_solution.kth([5, 3, 1], 1)
    assert isinstance(r1, int)
    assert r1 == 3
    r2 = _case9_solution.kth([42], 0)
    assert isinstance(r2, int)
    assert r2 == 42

import solution as _case10_solution

def test_kth_five_element_descending():
    """Five-element descending: exhaustively verify all positions."""
    arr = [5, 4, 3, 2, 1]
    expected = sorted(arr)
    for k in range(len(arr)):
        assert _case10_solution.kth(arr, k) == expected[k]

import solution as _case11_solution

def test_kth_ten_element_descending():
    """Ten-element descending: exhaustive check all k values."""
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    expected = sorted(arr)
    for k in range(len(arr)):
        assert _case11_solution.kth(arr, k) == expected[k]

import solution as _case12_solution

def test_kth_single_element_type():
    """Single element: verify return type and value."""
    result = _case12_solution.kth([99], 0)
    assert isinstance(result, int)
    assert result == 99
