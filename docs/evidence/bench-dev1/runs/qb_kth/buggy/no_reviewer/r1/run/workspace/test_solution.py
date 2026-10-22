# Accepted by submit_tests; explanations in testgen_report.json.

from solution import kth as _case0_kth

def test_p1_median_distinct():
    """Docstring quote: "efficient equivalent to sorted(arr)[k]"

    Input domain: arr=[5, 2, 8, 1, 9], k=2
    Sorted arr is [1, 2, 5, 8, 9]; index 2 yields 5.
    Fault hypothesis: if the function skips or miscounts elements around
    the pivot, the returned value may differ from the true k-th order
    statistic."""
    result = _case0_kth([5, 2, 8, 1, 9], 2)
    assert result == 5

from solution import kth as _case1_kth

def test_p2_minimum_at_k0():
    """Docstring quote: "The kth-lowest element of arr (0-based)"

    Input domain: arr=[10, 20, 30], k=0
    Index 0 in a sorted sequence is the minimum, i.e. 10.
    Fault hypothesis: an off-by-one error could return the second-smallest
    element instead of the true minimum."""
    result = _case1_kth([10, 20, 30], 0)
    assert result == 10

from solution import kth as _case2_kth

def test_p4_single_element():
    """Docstring quote: precondition "0 <= k < len(arr)"

    Input domain: arr=[42], k=0
    Only valid k is 0; sorted([42])[0] = 42.
    Fault hypothesis: edge-case handling of length-1 lists could raise
    an IndexError or return a wrong value."""
    result = _case2_kth([42], 0)
    assert result == 42

from solution import kth as _case3_kth

def test_p5_duplicate_values():
    """Docstring quote: "efficient equivalent to sorted(arr)[k]"

    Input domain: arr=[3, 1, 2, 1, 3], k=1
    Sorted version is [1, 1, 2, 3, 3]; index 1 is 1.
    Fault hypothesis: duplicates handled via strict '<' and '>' partitions
    may cause incorrect counting (num_lessoreq) and lead to wrong branch
    selection."""
    result = _case3_kth([3, 1, 2, 1, 3], 1)
    assert result == 1

from solution import kth as _case4_kth

def test_p8_all_identical():
    """Docstring quote: "efficient equivalent to sorted(arr)[k]"

    Input domain: arr=[5, 5, 5], k=1
    Sorted arr remains [5, 5, 5]; any valid k returns 5.
    Fault hypothesis: when every element equals the pivot, both below
    and above are empty; the function should return the pivot directly.
    A bug could cause infinite recursion or an IndexError."""
    result = _case4_kth([5, 5, 5], 1)
    assert result == 5
