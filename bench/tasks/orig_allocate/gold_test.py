import pytest
from solution import allocate


@pytest.mark.parametrize("total, weights, expected", [
    (100, [1, 1, 1], [34, 33, 33]),
    (10, [3, 0, 7], [3, 0, 7]),
    (0, [1, 2], [0, 0]),
    (7, [5], [7]),
    (5, [1, 1, 1, 1], [2, 1, 1, 1]),
    (10, [1, 2, 3, 4], [1, 2, 3, 4]),
    (11, [1, 2, 3, 4], [1, 2, 3, 5]),
    (3, [0, 0, 2, 1], [0, 0, 2, 1]),
    (1, [0, 1, 1], [0, 1, 0]),
    (10**20 + 1, [1, 1], [5 * 10**19 + 1, 5 * 10**19]),
    (2, [1, 1, 1], [1, 1, 0]),
    (5, [1, 2, 3], [1, 2, 2]),
    (10**17, [1, 2], [33333333333333333, 66666666666666667]),
])
def test_examples(total, weights, expected):
    assert allocate(total, weights) == expected


def test_sum_and_proportion_on_many_inputs():
    for total in range(0, 40):
        for weights in ([1, 2], [3, 0, 5], [2, 2, 2, 1], [9, 1, 1]):
            shares = allocate(total, weights)
            assert sum(shares) == total
            for s, w in zip(shares, weights):
                exact = total * w / sum(weights)
                assert exact - 1 < s < exact + 1


def test_input_list_is_not_modified():
    weights = [1, 2, 3]
    allocate(10, weights)
    assert weights == [1, 2, 3]


@pytest.mark.parametrize("total, weights", [(-1, [1]), (5, []), (5, [1, -1]), (5, [0, 0])])
def test_invalid(total, weights):
    with pytest.raises(ValueError):
        allocate(total, weights)
