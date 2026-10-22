# Accepted by submit_tests; explanations in testgen_report.json.

import pytest as _case0_pytest
from solution import factorial_sums as _case0_factorial_sums

def test_p6_non_list_input():
    """Raise TypeError for non-list input."""
    with _case0_pytest.raises(TypeError):
        _case0_factorial_sums('123')

import pytest as _case1_pytest
from solution import factorial_sums as _case1_factorial_sums

def test_p2_empty_list():
    """Handle empty input list."""
    result = _case1_factorial_sums([])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert result[0] == []
    assert result[1] == []

import pytest as _case2_pytest
from solution import factorial_sums as _case2_factorial_sums

def test_p7_negative_integers():
    """Raise ValueError for negative integers."""
    with _case2_pytest.raises(ValueError):
        _case2_factorial_sums([-5, 1])

import pytest as _case3_pytest
from solution import factorial_sums as _case3_factorial_sums

def test_p8_non_integer_in_list():
    """Raise TypeError for list containing non-integers."""
    with _case3_pytest.raises(TypeError):
        _case3_factorial_sums([1, 2.5])

import pytest as _case4_pytest
from solution import factorial_sums as _case4_factorial_sums

def test_p9_return_type_structure():
    """Verify return value structure matches docstring signature."""
    result = _case4_factorial_sums([1, 2])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], list)
    assert isinstance(result[1], list)
    assert len(result[0]) == 2
    assert len(result[1]) == 2
    assert isinstance(result[1][0], tuple)
