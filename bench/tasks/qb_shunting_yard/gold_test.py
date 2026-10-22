import pytest
from solution import shunting_yard

CASES = [[[[]], []], [[[30]], [30]], [[[10, '-', 5, '-', 2]], [10, 5, '-', 2, '-']], [[[34, '-', 12, '/', 5]], [34, 12, 5, '/', '-']], [[[4, '+', 9, '*', 9, '-', 10, '+', 13]], [4, 9, 9, '*', '+', 10, '-', 13, '+']], [[[7, '*', 43, '-', 7, '+', 13, '/', 7]], [7, 43, '*', 7, '-', 13, 7, '/', '+']]]


@pytest.mark.parametrize('args, expected', CASES)
def test_upstream(args, expected):
    assert shunting_yard(*args) == expected
