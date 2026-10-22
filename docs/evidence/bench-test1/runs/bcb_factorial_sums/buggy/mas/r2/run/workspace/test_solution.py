# Accepted by submit_tests; explanations in testgen_report.json.

import pytest as _case0_pytest
from solution import factorial_sums as _case0_factorial_sums

def test_p5_not_a_list():
    """P5: Reject inputs where the container is not a list.

    Contract quote: 'TypeError: If numbers is not a list of integers.'

    Input domain: numbers = None — not a list.

    Oracle reasoning: The function must raise TypeError for non-list inputs.

    Fault hypothesis: Implementation silently accepts non-list types or raises
    a different exception.
    """
    with _case0_pytest.raises(TypeError):
        _case0_factorial_sums(None)

import pytest as _case1_pytest
from solution import factorial_sums as _case1_factorial_sums

def test_p6_negative_integers():
    """P6: Reject inputs containing negative integers.

    Contract quote: 'ValueError: If input numbers are negative.'

    Input domain: numbers = [-2, 3] — contains a negative integer.

    Oracle reasoning: Negative integers are forbidden; ValueError must be raised.

    Fault hypothesis: Implementation ignores negative values or raises TypeError
    instead of ValueError.
    """
    with _case1_pytest.raises(ValueError):
        _case1_factorial_sums([-2, 3])
