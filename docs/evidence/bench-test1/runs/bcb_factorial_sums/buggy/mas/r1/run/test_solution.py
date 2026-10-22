# Accepted by submit_tests; explanations in testgen_report.json.

from solution import factorial_sums as _case0_factorial_sums
import pytest as _case0_pytest

def test_p5_negative_integers():
    """Rejects input containing negative integers."""
    with _case0_pytest.raises(ValueError):
        _case0_factorial_sums([-1, 2])

from solution import factorial_sums as _case1_factorial_sums
import pytest as _case1_pytest

def test_p6_non_list_input():
    """Rejects non-list input types."""
    with _case1_pytest.raises(TypeError):
        _case1_factorial_sums('invalid_string')
