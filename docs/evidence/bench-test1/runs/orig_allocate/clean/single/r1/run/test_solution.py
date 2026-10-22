# Accepted by submit_tests; explanations in testgen_report.json.

from solution import allocate as _case0_allocate

def test_single_weight():
    """With a single weight, the entire total goes to that one entry."""
    result = _case0_allocate(42, [5])
    assert result == [42]
    assert isinstance(result, list)
    assert len(result) == 1

from solution import allocate as _case1_allocate

def test_total_zero():
    """When total is 0, every entry should receive 0."""
    result = _case1_allocate(0, [1, 2, 3])
    assert result == [0, 0, 0]
    assert sum(result) == 0

from solution import allocate as _case2_allocate

def test_tie_breaking():
    """Ties in fractional remainder go to the lower index entry."""
    result = _case2_allocate(1, [1, 1])
    assert result == [1, 0]
    result2 = _case2_allocate(10, [2, 2, 2, 2])
    assert result2 == [3, 3, 2, 2]
    assert sum(result2) == 10

from solution import allocate as _case3_allocate
import pytest as _case3_pytest

def test_value_errors():
    """ValueError must be raised for invalid inputs per the contract."""
    with _case3_pytest.raises(ValueError):
        _case3_allocate(-1, [1, 2])
    with _case3_pytest.raises(ValueError):
        _case3_allocate(10, [])
    with _case3_pytest.raises(ValueError):
        _case3_allocate(10, [1, -1, 2])
    with _case3_pytest.raises(ValueError):
        _case3_allocate(10, [0, 0, 0])

from solution import allocate as _case4_allocate

def test_basic_docstring():
    """Verify the primary docstring example: split 100 among three equal weights."""
    result = _case4_allocate(100, [1, 1, 1])
    assert result == [34, 33, 33]

from solution import allocate as _case5_allocate

def test_zero_weight_entry():
    """Entries with weight 0 must always receive 0 regardless of total."""
    result = _case5_allocate(10, [3, 0, 7])
    assert result == [3, 0, 7]
    assert result[1] == 0
