# Accepted by submit_tests; explanations in testgen_report.json.

import pytest as _case0_pytest
from solution import factorial_sums as _case0_factorial_sums

def test_p3_empty_list():
    """Returns empty collections for an empty input list."""
    result = _case0_factorial_sums([])
    assert result == ([], [])

import pytest as _case1_pytest
from solution import factorial_sums as _case1_factorial_sums

def test_p6_not_a_list():
    """Raises TypeError when input is not a list."""
    with _case1_pytest.raises(TypeError):
        _case1_factorial_sums((1, 2, 3))

import pytest as _case2_pytest
from solution import factorial_sums as _case2_factorial_sums

def test_p5_negative_values():
    """Raises ValueError when negative integers are present."""
    with _case2_pytest.raises(ValueError):
        _case2_factorial_sums([-5, 10])
