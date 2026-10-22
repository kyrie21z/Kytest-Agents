# Accepted by submit_tests; explanations in testgen_report.json.

from solution import factorial_sums as _case0_factorial_sums

def test_factorial_sums_empty_list():
    """Verify empty list returns ([], [])."""
    result = _case0_factorial_sums([])
    assert result == ([], [])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], list)
    assert isinstance(result[1], list)

from solution import factorial_sums as _case1_factorial_sums
import pytest as _case1_pytest

def test_factorial_sums_type_error_not_list():
    """Verify TypeError when input is not a list."""
    with _case1_pytest.raises(TypeError):
        _case1_factorial_sums((1, 2, 3))
    with _case1_pytest.raises(TypeError):
        _case1_factorial_sums('not a list')
    with _case1_pytest.raises(TypeError):
        _case1_factorial_sums(None)

from solution import factorial_sums as _case2_factorial_sums
import pytest as _case2_pytest

def test_factorial_sums_value_error_negative():
    """Verify ValueError when input contains negative numbers."""
    with _case2_pytest.raises(ValueError):
        _case2_factorial_sums([-1, 2, 3])
    with _case2_pytest.raises(ValueError):
        _case2_factorial_sums([0, -5])
