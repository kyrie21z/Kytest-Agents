# Accepted by submit_tests; explanations in testgen_report.json.

def test_k_equals_zero_minimum():
    from solution import kth
    assert kth([3, 1, 4, 1, 5, 9, 2, 6], 0) == 1

def test_k_equals_len_minus_1_maximum():
    from solution import kth
    assert kth([3, 1, 4, 1, 5, 9, 2, 6], 7) == 9

def test_all_same_elements():
    from solution import kth
    assert kth([5, 5, 5, 5, 5], 2) == 5

def test_negative_numbers():
    from solution import kth
    assert kth([-3, -1, -4, -1, -5, -9, -2, -6], 3) == -4

def test_two_elements():
    from solution import kth
    assert kth([7, 3], 0) == 3
    assert kth([7, 3], 1) == 7

def test_already_sorted():
    from solution import kth
    assert kth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4) == 5
    assert kth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9) == 10

def test_reverse_sorted():
    from solution import kth
    assert kth([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0) == 1
    assert kth([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 5) == 6

def test_with_zeros():
    from solution import kth
    assert kth([0, -1, 0, 1, -2], 0) == -2
    assert kth([0, -1, 0, 1, -2], 2) == 0
    assert kth([0, -1, 0, 1, -2], 4) == 1
