# Accepted by submit_tests; explanations in testgen_report.json.

# Accepted by submit_tests; explanations in testgen_report.json.

from solution import factorial_sums as _case0_factorial_sums

def test_empty_list():
    """Verify that an empty list returns two empty lists as specified.
    Contract: 'If an empty list is given, the function returns empty lists.'"""
    result = _case0_factorial_sums([])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert result[0] == []
    assert result[1] == []

from solution import factorial_sums as _case1_factorial_sums
import pytest as _case1_pytest

def test_type_error_non_list():
    """Verify TypeError is raised when input is not a list.
    Contract: 'TypeError: If numbers is not a list of integers.'"""
    with _case1_pytest.raises(TypeError):
        _case1_factorial_sums((1, 2, 3))
    with _case1_pytest.raises(TypeError):
        _case1_factorial_sums('not a list')
    with _case1_pytest.raises(TypeError):
        _case1_factorial_sums(None)


import pytest as _new668526c80__case5_pytest
from solution import factorial_sums as _new668526c80__case5_factorial_sums

def test_non_integer_elements():
    """Verify TypeError is raised when list contains non-integer elements.
    Contract: 'TypeError: If numbers is not a list of integers.'"""
    with _new668526c80__case5_pytest.raises(TypeError):
        _new668526c80__case5_factorial_sums([1.5])
    with _new668526c80__case5_pytest.raises(TypeError):
        _new668526c80__case5_factorial_sums(['a'])
    with _new668526c80__case5_pytest.raises(TypeError):
        _new668526c80__case5_factorial_sums([1, 2.0])

import pytest as _new668526c81__case4_pytest
from solution import factorial_sums as _new668526c81__case4_factorial_sums

def test_negative_numbers_v2():
    """Verify ValueError is raised when input contains negative numbers."""
    with _new668526c81__case4_pytest.raises(ValueError):
        _new668526c81__case4_factorial_sums([-1])
    with _new668526c81__case4_pytest.raises(ValueError):
        _new668526c81__case4_factorial_sums([1, -5, 3])
