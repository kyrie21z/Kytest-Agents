# Accepted by submit_tests; explanations in testgen_report.json.

"""P2: zero-weight entries receive zero."""
import pytest as _case0_pytest
from solution import allocate as _case0_allocate

def test_p2_zero_weight_entry():
    result = _case0_allocate(10, [3, 0, 7])
    assert result == [3, 0, 7]
    assert sum(result) == 10

"""P3: minimum allowed total (zero)."""
import pytest as _case1_pytest
from solution import allocate as _case1_allocate

def test_p3_total_zero():
    result = _case1_allocate(0, [2, 3])
    assert result == [0, 0]
    assert sum(result) == 0

"""P6: negative total raises ValueError."""
import pytest as _case2_pytest
from solution import allocate as _case2_allocate

def test_p6_negative_total():
    with _case2_pytest.raises(ValueError):
        _case2_allocate(-5, [1, 2])

"""P5: result sums exactly to input total."""
import pytest as _case3_pytest
from solution import allocate as _case3_allocate

def test_p5_sum_equals_total():
    result = _case3_allocate(10, [1, 2, 3])
    assert result == [2, 3, 5]
    assert sum(result) == 10

"""P7: empty weight list raises ValueError."""
import pytest as _case4_pytest
from solution import allocate as _case4_allocate

def test_p7_empty_weights():
    with _case4_pytest.raises(ValueError):
        _case4_allocate(10, [])

"""P8: all-zero weights raises ValueError."""
import pytest as _case5_pytest
from solution import allocate as _case5_allocate

def test_p8_all_zero_weights():
    with _case5_pytest.raises(ValueError):
        _case5_allocate(10, [0, 0])

"""P9: negative weight raises ValueError."""
import pytest as _case6_pytest
from solution import allocate as _case6_allocate

def test_p9_negative_weight():
    with _case6_pytest.raises(ValueError):
        _case6_allocate(10, [1, -1])

"""P10: single-element weight list."""
import pytest as _case7_pytest
from solution import allocate as _case7_allocate

def test_p10_single_weight():
    result = _case7_allocate(42, [7])
    assert result == [42]
    assert sum(result) == 42

"""Extra: result must be a list of integers."""
import pytest as _case8_pytest
from solution import allocate as _case8_allocate

def test_extra_return_type():
    result = _case8_allocate(100, [1, 1, 1])
    assert isinstance(result, list)
    assert all((isinstance(v, int) for v in result))

"""Extra: larger proportional allocation."""
import pytest as _case9_pytest
from solution import allocate as _case9_allocate

def test_extra_larger_proportional():
    result = _case9_allocate(100, [1, 2, 3])
    assert result == [17, 33, 50]
    assert sum(result) == 100

"""Extra: many zeros with one positive weight."""
import pytest as _case10_pytest
from solution import allocate as _case10_allocate

def test_extra_many_zeros():
    result = _case10_allocate(100, [0, 0, 5, 0])
    assert result == [0, 0, 100, 0]
    assert sum(result) == 100

"""Extra: total equals number of leftover units boundary."""
import pytest as _case11_pytest
from solution import allocate as _case11_allocate

def test_extra_leftover_boundary():
    result = _case11_allocate(3, [1, 1, 1])
    assert result == [1, 1, 1]
    assert sum(result) == 3
