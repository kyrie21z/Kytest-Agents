# Accepted by submit_tests; explanations in testgen_report.json.

from solution import allocate as _case0_allocate

def test_zero_weight_entry():
    """Entries with weight 0 must always receive 0."""
    result = _case0_allocate(10, [3, 0, 7])
    assert result == [3, 0, 7]
    assert result[1] == 0
    assert sum(result) == 10

from solution import allocate as _case1_allocate

def test_sum_preservation():
    """The sum of returned shares must always equal total."""
    for total, weights in [(0, [5]), (1, [1, 1]), (7, [2, 2, 3]), (100, [1, 1, 1]), (50, [10, 20, 30, 40]), (13, [3, 0, 7])]:
        result = _case1_allocate(total, weights)
        assert len(result) == len(weights)
        assert sum(result) == total, f'sum={sum(result)} != total={total} for {weights}'

from solution import allocate as _case2_allocate
import pytest as _case2_pytest

def test_valueerror_invalid_inputs():
    """Invalid inputs must raise ValueError."""
    with _case2_pytest.raises(ValueError):
        _case2_allocate(-1, [1, 2])
    with _case2_pytest.raises(ValueError):
        _case2_allocate(10, [])
    with _case2_pytest.raises(ValueError):
        _case2_allocate(10, [1, -1, 2])
    with _case2_pytest.raises(ValueError):
        _case2_allocate(10, [0, 0, 0])

from solution import allocate as _case3_allocate

def test_tie_breaking_by_index():
    """When remainders tie, the lower-index entry should receive the extra unit."""
    result = _case3_allocate(10, [1, 1, 1])
    assert result == [4, 3, 3], f'Expected [4,3,3] got {result}'
    assert result[0] > result[1]
    assert result[1] == result[2]

from solution import allocate as _case4_allocate

def test_basic_equal_weights():
    """Verify the doctest example: three equal weights split 100."""
    result = _case4_allocate(100, [1, 1, 1])
    assert result == [34, 33, 33]
    assert isinstance(result, list)
    assert all((isinstance(x, int) for x in result))

from solution import allocate as _case5_allocate

def test_single_weight():
    """With a single weight, the entire total goes to that entry."""
    result = _case5_allocate(42, [1])
    assert result == [42]
    assert isinstance(result, list)
    assert len(result) == 1
    result2 = _case5_allocate(100, [5])
    assert result2 == [100]
