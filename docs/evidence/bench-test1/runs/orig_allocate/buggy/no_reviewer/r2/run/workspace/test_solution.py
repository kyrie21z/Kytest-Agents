# Accepted by submit_tests; explanations in testgen_report.json.

"""Test P2: Unequal weights including a zero weight."""
from solution import allocate as _case0_allocate

def test_p2_unequal_with_zero_weight():
    """allocate(10, [3, 0, 7]) -> [3, 0, 7].
    Base allocation exactly matches total, leaving no remainder."""
    result = _case0_allocate(10, [3, 0, 7])
    assert result == [3, 0, 7]
    assert sum(result) == 10

"""Test P3: Zero total distributes nothing."""
from solution import allocate as _case1_allocate

def test_p3_zero_total():
    """allocate(0, [2, 3, 5]) -> [0, 0, 0].
    floor(0*w/S)=0 and remainder=0, so all shares are 0."""
    result = _case1_allocate(0, [2, 3, 5])
    assert result == [0, 0, 0]
    assert sum(result) == 0

"""Test P4: Single weight receives entire total."""
from solution import allocate as _case2_allocate

def test_p4_single_weight():
    """allocate(50, [10]) -> [50].
    With one entry, floor(50*10/10)=50, remainder=0."""
    result = _case2_allocate(50, [10])
    assert result == [50]
    assert len(result) == 1

"""Test P5: Multiple zero-weight entries receive exactly zero."""
from solution import allocate as _case3_allocate

def test_p5_multiple_zero_weights():
    """allocate(100, [0, 5, 0, 5]) -> [0, 50, 0, 50].
    Positive weights split total proportionally; zeros get 0."""
    result = _case3_allocate(100, [0, 5, 0, 5])
    assert result == [0, 50, 0, 50]
    assert result[0] == 0
    assert result[2] == 0
    assert sum(result) == 100

"""Test P7: Negative total raises ValueError."""
from solution import allocate as _case4_allocate
import pytest as _case4_pytest

def test_p7_negative_total():
    """allocate(-1, [1, 2]) raises ValueError.
    Spec explicitly states 'Raises ValueError if total is negative'."""
    with _case4_pytest.raises(ValueError):
        _case4_allocate(-1, [1, 2])

"""Test P8: Empty weights list raises ValueError."""
from solution import allocate as _case5_allocate
import pytest as _case5_pytest

def test_p8_empty_weights():
    """allocate(10, []) raises ValueError.
    Spec explicitly states 'Raises ValueError if ... weights is empty'."""
    with _case5_pytest.raises(ValueError):
        _case5_allocate(10, [])

"""Test P9: Negative weight raises ValueError."""
from solution import allocate as _case6_allocate
import pytest as _case6_pytest

def test_p9_negative_weight():
    """allocate(10, [1, -1]) raises ValueError.
    Spec explicitly states 'Raises ValueError if ... any weight is negative'."""
    with _case6_pytest.raises(ValueError):
        _case6_allocate(10, [1, -1])

"""Test P11: Result list length matches weights length."""
from solution import allocate as _case7_allocate

def test_p11_length_match():
    """allocate(99, [2, 3, 5]) -> [20, 30, 49].
    Length must equal len(weights)."""
    result = _case7_allocate(99, [2, 3, 5])
    assert len(result) == 3
    assert result == [20, 30, 49]
    assert sum(result) == 99

"""Test P12: Large total preserves sum invariant and proportionality."""
from solution import allocate as _case8_allocate

def test_p12_large_total():
    """allocate(10^18, [1, 2]) -> [333333333333333333, 666666666666666667].
    Verifies correct floor/mod arithmetic without overflow or rounding drift."""
    total = 10 ** 18
    result = _case8_allocate(total, [1, 2])
    assert result == [333333333333333333, 666666666666666667]
    assert sum(result) == total

"""Test P10: All-zero weights raises ValueError."""
from solution import allocate as _case9_allocate
import pytest as _case9_pytest

def test_p10_all_zero_weights():
    """allocate(10, [0, 0]) raises ValueError.
    Spec explicitly states 'Raises ValueError if ... all weights are zero'. Division by sum(weights)=0 would otherwise occur."""
    with _case9_pytest.raises(ValueError):
        _case9_allocate(10, [0, 0])

"""Extra: Verify return type is always a list of ints."""
from solution import allocate as _case10_allocate

def test_extra_return_type():
    """Result is always a list of integers."""
    result = _case10_allocate(7, [1, 2, 3])
    assert isinstance(result, list)
    assert all((isinstance(x, int) for x in result))

"""Extra: Sum invariant holds for any valid input."""
from solution import allocate as _case11_allocate

def test_extra_sum_invariant():
    """Sum of result always equals total."""
    for total in [0, 1, 7, 100, 1000]:
        for weights in [[1], [1, 1], [1, 2, 3], [0, 5, 5], [10]]:
            result = _case11_allocate(total, weights)
            assert sum(result) == total, f'total={total}, weights={weights}, sum={sum(result)}'

"""Extra: Weights with only one positive entry among zeros."""
from solution import allocate as _case12_allocate

def test_extra_one_positive_among_zeros():
    """allocate(10, [0, 0, 5, 0]) -> [0, 0, 10, 0]."""
    result = _case12_allocate(10, [0, 0, 5, 0])
    assert result == [0, 0, 10, 0]
    assert sum(result) == 10
