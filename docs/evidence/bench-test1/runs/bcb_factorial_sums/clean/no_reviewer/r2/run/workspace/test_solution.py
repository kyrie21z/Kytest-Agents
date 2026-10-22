# Accepted by submit_tests; explanations in testgen_report.json.

from solution import factorial_sums as _case0_factorial_sums
import pytest as _case0_pytest

def test_p5_non_list_input():
    """P5: Rejects non-list input.
    Contract: 'Raises: TypeError: If numbers is not a list of integers.'"""
    with _case0_pytest.raises(TypeError):
        _case0_factorial_sums('123')

from solution import factorial_sums as _case1_factorial_sums
import pytest as _case1_pytest

def test_p6_non_integers():
    """P6: Rejects list containing non-integers.
    Contract: 'Raises: TypeError: If numbers is not a list of integers.'"""
    with _case1_pytest.raises(TypeError):
        _case1_factorial_sums([1, '2', 3])

from solution import factorial_sums as _case2_factorial_sums
import pytest as _case2_pytest

def test_p7_negative_numbers():
    """P7: Rejects negative numbers.
    Contract: Raises ValueError if input numbers are negative."""
    with _case2_pytest.raises(ValueError):
        _case2_factorial_sums([-1, 2])
