# Accepted by submit_tests; explanations in testgen_report.json.

"""Test that an empty list returns ([], [])."""
from solution import factorial_sums as _case0_factorial_sums

def test_empty_list():
    '''Quote: "If an empty list is given, the function returns empty lists."'''
    result = _case0_factorial_sums([])
    assert result == ([], [])
    assert isinstance(result[0], list)
    assert isinstance(result[1], list)

"""Test that non-list inputs raise TypeError."""
import pytest as _case1_pytest
from solution import factorial_sums as _case1_factorial_sums

def test_non_list_raises_type_error():
    '''Quote: "TypeError: If numbers is not a list of integers."'''
    with _case1_pytest.raises(TypeError):
        _case1_factorial_sums((1, 2, 3))

"""Test that negative numbers raise ValueError."""
import pytest as _case2_pytest
from solution import factorial_sums as _case2_factorial_sums

def test_negative_raises_value_error():
    '''Quote: "ValueError: If input numbers are negative."'''
    with _case2_pytest.raises(ValueError):
        _case2_factorial_sums([1, -1, 3])
