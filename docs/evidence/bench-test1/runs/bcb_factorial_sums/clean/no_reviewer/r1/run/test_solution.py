# Accepted by submit_tests; explanations in testgen_report.json.

import pytest as _case0_pytest
from solution import factorial_sums as _case0_factorial_sums

def test_p5_non_list_input():
    """P5: Rejects non-list input with TypeError.
    
    Contract quote: 'TypeError: If numbers is not a list of integers.'
    
    Input domain: (1, 2, 3) — a tuple, not a list.
    
    Oracle reasoning:
      - The contract mandates TypeError when the argument is not a list.
      Expected: raises TypeError.
    
    Fault hypothesis: An implementation might silently accept tuples or other iterables.
    """
    with _case0_pytest.raises(TypeError):
        _case0_factorial_sums((1, 2, 3))

import pytest as _case1_pytest
from solution import factorial_sums as _case1_factorial_sums

def test_p7_negative_numbers():
    """P7: Rejects list containing negative numbers with ValueError.
    
    Contract quote: 'ValueError: If input numbers are negative.'
    
    Input domain: [-2, 0, 1] — contains a negative integer.
    
    Oracle reasoning:
      - The contract mandates ValueError for negative inputs.
      Expected: raises ValueError.
    
    Fault hypothesis: An implementation might compute factorial of negatives or skip negative values.
    """
    with _case1_pytest.raises(ValueError):
        _case1_factorial_sums([-2, 0, 1])
