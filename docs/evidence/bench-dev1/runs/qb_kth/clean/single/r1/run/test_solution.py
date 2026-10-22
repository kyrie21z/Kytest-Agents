# Accepted by submit_tests; explanations in testgen_report.json.

def test_kth_basic():
    from solution import kth
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    expected_sorted = sorted(arr)
    for k in range(len(arr)):
        assert kth(arr, k) == expected_sorted[k]

def test_kth_single_element():
    from solution import kth
    assert kth([42], 0) == 42

def test_kth_all_same_elements():
    from solution import kth
    arr = [7, 7, 7, 7, 7]
    for k in range(len(arr)):
        assert kth(arr, k) == 7

def test_kth_min_max():
    from solution import kth
    arr = [10, -3, 7, 0, 5, -1, 8]
    assert kth(arr, 0) == min(arr)
    assert kth(arr, len(arr) - 1) == max(arr)

def test_kth_two_elements():
    from solution import kth
    assert kth([5, 3], 0) == 3
    assert kth([5, 3], 1) == 5
    assert kth([1, 9], 0) == 1
    assert kth([1, 9], 1) == 9

def test_kth_return_type():
    from solution import kth
    result = kth([100, 200, 300], 1)
    assert isinstance(result, int)
    result2 = kth([-5, 0, 5], 0)
    assert isinstance(result2, int)
