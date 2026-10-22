# Accepted by submit_tests; explanations in testgen_report.json.

import pytest as _case0_pytest
from solution import factorial_sums as _case0_factorial_sums

def test_p5_non_list_input():
    """Non-list input raises TypeError.
    Docstring quote: 'Raises: TypeError: If numbers is not a list of integers.'
    Input domain: numbers = "not_a_list"
    Oracle: Raises TypeError.
    Faulty: No exception raised or wrong exception type."""
    with _case0_pytest.raises(TypeError):
        _case0_factorial_sums('not_a_list')

import pytest as _case1_pytest
from solution import factorial_sums as _case1_factorial_sums

def test_p6_list_with_non_integers():
    """List containing non-integers raises TypeError.
    Docstring quote: 'Raises: TypeError: If numbers is not a list of integers.'
    Input domain: numbers = [1, 2.5, 3]
    Oracle: Raises TypeError.
    Faulty: No exception raised or wrong exception type."""
    with _case1_pytest.raises(TypeError):
        _case1_factorial_sums([1, 2.5, 3])
