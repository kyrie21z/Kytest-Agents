# Accepted by submit_tests; explanations in testgen_report.json.

from solution import allocate as _case0_allocate

def test_zero_weight_entry():
    """Entries with weight 0 always receive 0, even if total > 0."""
    result = _case0_allocate(10, [3, 0, 7])
    assert result == [3, 0, 7]

from solution import allocate as _case1_allocate

def test_single_weight():
    """With one weight, the entire total goes to that entry."""
    result = _case1_allocate(10, [5])
    assert result == [10]
    assert isinstance(result, list)
    assert len(result) == 1

from solution import allocate as _case2_allocate

def test_total_is_zero():
    """When total is 0, every entry receives 0 regardless of weights."""
    result = _case2_allocate(0, [1, 2, 3])
    assert result == [0, 0, 0]
    assert sum(result) == 0

from solution import allocate as _case3_allocate

def test_remainder_distribution_order():
    """Larger fractional remainder gets priority; ties broken by lower index."""
    result = _case3_allocate(1, [1, 2])
    assert result == [0, 1]
    assert sum(result) == 1

from solution import allocate as _case4_allocate
import pytest as _case4_pytest

def test_value_errors():
    """Invalid inputs must raise ValueError per contract."""
    with _case4_pytest.raises(ValueError):
        _case4_allocate(-1, [1, 2])
    with _case4_pytest.raises(ValueError):
        _case4_allocate(10, [])
    with _case4_pytest.raises(ValueError):
        _case4_allocate(10, [1, -1])
    with _case4_pytest.raises(ValueError):
        _case4_allocate(10, [0, 0])

from solution import allocate as _case5_allocate

def test_basic_equal_weights():
    """Verify the docstring example: equal weights split total with remainder to lowest index."""
    result = _case5_allocate(100, [1, 1, 1])
    assert result == [34, 33, 33]

from solution import allocate as _case6_allocate

def test_large_remainder_distribution():
    """When leftover > number of positive-weight entries, every positive entry gets +1 and remaining leftovers cycle."""
    result = _case6_allocate(7, [1, 1, 1])
    assert result == [3, 2, 2]
    assert sum(result) == 7

from solution import allocate as _case7_allocate

def test_sum_equals_total():
    """The returned list must always sum exactly to total."""
    for total, weights in [(100, [1, 2, 3]), (50, [10, 20, 30]), (1, [1, 1, 1, 1]), (1000, [1, 1, 1, 1, 1]), (13, [4, 6, 3])]:
        result = _case7_allocate(total, weights)
        assert isinstance(result, list)
        assert len(result) == len(weights)
        assert all((isinstance(x, int) for x in result)), f'Non-int in result: {result}'
        assert sum(result) == total, f'Sum {sum(result)} != total {total}'

from solution import allocate as _case8_allocate

def test_non_negative_shares():
    """All share values must be non-negative integers."""
    result = _case8_allocate(100, [5, 3, 2])
    assert all((x >= 0 for x in result)), f'Negative share found: {result}'
    assert all((isinstance(x, int) for x in result))
    assert all((x <= 100 for x in result))

from solution import allocate as _case9_allocate

def test_tie_breaking_by_index():
    """When multiple entries have identical remainders, lower index wins."""
    result = _case9_allocate(5, [2, 2, 2])
    assert result == [2, 2, 1]
    assert sum(result) == 5
