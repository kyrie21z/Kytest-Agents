# Accepted by submit_tests; explanations in testgen_report.json.

def test_lis_single_element():
    from solution import lis
    result = lis([42])
    assert result == 1

def test_lis_already_sorted():
    from solution import lis
    result = lis([1, 2, 3, 4, 5])
    assert result == 5

def test_lis_reverse_sorted():
    from solution import lis
    result = lis([5, 4, 3, 2, 1])
    assert result == 1

def test_lis_two_elements_increasing():
    from solution import lis
    result = lis([1, 3])
    assert result == 2
    result2 = lis([3, 1])
    assert result2 == 1

def test_lis_empty():
    from solution import lis
    result = lis([])
    assert result == 0

def test_lis_example_from_docstring():
    from solution import lis
    result = lis([4, 1, 5, 3, 7, 6, 2])
    assert result == 3

def test_lis_negative_values():
    from solution import lis
    result = lis([-5, -3, -1, -4, -2])
    assert result == 3

def test_lis_large_strictly_increasing():
    from solution import lis
    n = 100
    arr = list(range(n))
    result = lis(arr)
    assert result == n

def test_lis_all_same():
    from solution import lis
    result = lis([2, 2, 2])
    assert result == 1

def test_lis_alternating():
    from solution import lis
    result = lis([1, 3, 2, 4, 3, 5])
    assert result == 4

def test_lis_three_elements():
    from solution import lis
    assert lis([3, 2, 1]) == 1
    assert lis([2, 1, 3]) == 2
    assert lis([1, 3, 2]) == 2

def test_lis_worst_case_alternating():
    from solution import lis
    result = lis([1, 5, 2, 6, 3, 7, 4, 8])
    assert result == 5

def test_lis_increasing_then_drop():
    from solution import lis
    result = lis([1, 2, 3, 4, 5, 1, 2, 3])
    assert result == 5

def test_lis_single_large_value():
    from solution import lis
    result = lis([999999999])
    assert result == 1
    assert isinstance(result, int)
