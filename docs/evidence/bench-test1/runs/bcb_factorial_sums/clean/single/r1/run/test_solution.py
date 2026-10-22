# Accepted by submit_tests; explanations in testgen_report.json.

"""Test empty list returns empty lists."""
from solution import factorial_sums as _case0_factorial_sums

def test_empty_list():
    """Contract: [] → returns ([], []).
    Detects: returning None or raising on empty input."""
    result = _case0_factorial_sums([])
    assert result == ([], [])

"""Test TypeError when passing non-list."""
import pytest as _case1_pytest
from solution import factorial_sums as _case1_factorial_sums

def test_type_error_on_non_list():
    """Contract: TypeError if numbers is not a list.
    Detects: silently accepting tuples/strings instead of raising."""
    with _case1_pytest.raises(TypeError):
        _case1_factorial_sums((1, 2))

"""Test ValueError when negative number provided."""
import pytest as _case2_pytest
from solution import factorial_sums as _case2_factorial_sums

def test_value_error_on_negative():
    """Contract: ValueError if any number < 0.
    Detects: computing factorial of negative numbers silently."""
    with _case2_pytest.raises(ValueError):
        _case2_factorial_sums([1, -1, 3])
