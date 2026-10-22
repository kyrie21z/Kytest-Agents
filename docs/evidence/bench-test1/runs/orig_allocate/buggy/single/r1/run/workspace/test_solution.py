# Accepted by submit_tests; explanations in testgen_report.json.

import pytest as _case0_pytest
from solution import allocate as _case0_allocate

def test_zero_weight_entry():
    """>>> allocate(10, [3, 0, 7])
     [3, 0, 7]"""
    result = _case0_allocate(10, [3, 0, 7])
    assert result == [3, 0, 7], 'Weight-0 entry must receive exactly 0'
    assert result[1] == 0, 'Contract: entries with weight 0 always receive 0'

import pytest as _case1_pytest
from solution import allocate as _case1_allocate

def test_shares_sum_to_total():
    """The result is a new list of ints, one per weight, summing to total."""
    for total, weights in [(100, [1, 2, 3]), (7, [10, 20, 30]), (13, [4, 4, 4]), (50, [1, 0, 1]), (1, [1, 1])]:
        result = _case1_allocate(total, weights)
        assert sum(result) == total, f'Shares {result} for total={total} must sum to total'

import pytest as _case2_pytest
from solution import allocate as _case2_allocate

def test_negative_total_raises():
    """Raises ValueError if total is negative."""
    with _case2_pytest.raises(ValueError, match='invalid allocation request'):
        _case2_allocate(-1, [1, 2, 3])

import pytest as _case3_pytest
from solution import allocate as _case3_allocate

def test_empty_weights_raises():
    """Raises ValueError if weights is empty."""
    with _case3_pytest.raises(ValueError, match='invalid allocation request'):
        _case3_allocate(10, [])

import pytest as _case4_pytest
from solution import allocate as _case4_allocate

def test_single_weight_receives_all():
    """When there is only one weight, that entry receives the entire total."""
    result = _case4_allocate(42, [7])
    assert result == [42], 'Single weight must receive the full total'
    assert isinstance(result, list), 'Return type must be a list'
    assert len(result) == 1, 'One weight produces one share'

import pytest as _case5_pytest
from solution import allocate as _case5_allocate

def test_total_zero_all_zeros():
    """When total is 0, every entry receives 0 regardless of weights."""
    result = _case5_allocate(0, [5, 3, 2])
    assert result == [0, 0, 0], 'Total=0 means every share is 0'
    assert sum(result) == 0, 'Shares must sum to total'
