"""Hidden checks added by Kytest-Agents for docstring promises the upstream tests skip.

Docstring example: task_func([0, 4]) -> [25, 25]; "Raises: TypeError: If numbers is not a list of integers."
"""
import pytest
from solution import factorial_sums


def test_zero_is_allowed():
    sums, perms = factorial_sums([0, 4])
    assert sums == [25, 25]
    assert sorted(perms) == [(0, 4), (4, 0)]


@pytest.mark.parametrize("bad", [[1.2, 1, 4], [1, "a", 4], "a", 1])
def test_non_integer_input_raises_type_error(bad):
    with pytest.raises(TypeError):
        factorial_sums(bad)
