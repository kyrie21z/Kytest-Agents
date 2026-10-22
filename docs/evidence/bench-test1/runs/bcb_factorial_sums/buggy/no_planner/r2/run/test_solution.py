# Accepted by submit_tests; explanations in testgen_report.json.

# Accepted by submit_tests; explanations in testgen_report.json.

from solution import factorial_sums as _case0_factorial_sums

def test_empty_list():
    """Empty list should return two empty lists per the docstring."""
    result = _case0_factorial_sums([])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert result[0] == []
    assert result[1] == []

from solution import factorial_sums as _case1_factorial_sums
import pytest as _case1_pytest

def test_type_error_non_list():
    """Non-list inputs must raise TypeError as documented."""
    for bad_input in [None, 42, 'abc', (1, 2, 3), {1, 2}]:
        with _case1_pytest.raises(TypeError):
            _case1_factorial_sums(bad_input)

from solution import factorial_sums as _case2_factorial_sums
import pytest as _case2_pytest

def test_value_error_negative():
    """Negative numbers must raise ValueError as documented."""
    with _case2_pytest.raises(ValueError):
        _case2_factorial_sums([-1, 2, 3])
    with _case2_pytest.raises(ValueError):
        _case2_factorial_sums([0, 4])


from solution import factorial_sums as _newf81a384a0__case5_factorial_sums
import pytest as _newf81a384a0__case5_pytest

def test_non_integer_elements():
    """List with non-integer elements should raise TypeError."""
    with _newf81a384a0__case5_pytest.raises(TypeError):
        _newf81a384a0__case5_factorial_sums([1, 2.5])
