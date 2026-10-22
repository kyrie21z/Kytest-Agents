# Accepted by submit_tests; explanations in testgen_report.json.

"""Test P1: Basic proportional split with equal weights and uneven division."""
import pytest as _case0_pytest
from solution import allocate as _case0_allocate

def test_p1_basic_equal_weights():
    result = _case0_allocate(100, [1, 1, 1])
    assert result == [34, 33, 33]
    assert isinstance(result, list)
    assert all((isinstance(x, int) for x in result))

"""Test P3: Total is zero – all shares must be zero."""
import pytest as _case1_pytest
from solution import allocate as _case1_allocate

def test_p3_total_zero():
    result = _case1_allocate(0, [2, 3, 5])
    assert result == [0, 0, 0]
    assert sum(result) == 0
    assert len(result) == 3

"""Test P6: Negative total raises ValueError."""
import pytest as _case2_pytest
from solution import allocate as _case2_allocate

def test_p6_negative_total():
    with _case2_pytest.raises(ValueError):
        _case2_allocate(-5, [1, 2])

"""Test P10: Zero-weight entries strictly receive zero regardless of total."""
import pytest as _case3_pytest
from solution import allocate as _case3_allocate

def test_p10_zero_weight_entries():
    result = _case3_allocate(100, [0, 50, 0, 50])
    assert result == [0, 50, 0, 50]
    assert result[0] == 0
    assert result[2] == 0
    assert sum(result) == 100

"""Test P5: Tie-breaking among multiple equal remainders gives extras to lower indices."""
import pytest as _case4_pytest
from solution import allocate as _case4_allocate

def test_p5_tie_breaking():
    result = _case4_allocate(10, [1, 1, 1, 1])
    assert result == [3, 3, 2, 2]
    assert sum(result) == 10

"""Test P12: Uneven distribution with distinct fractional remainders."""
import pytest as _case5_pytest
from solution import allocate as _case5_allocate

def test_p12_distinct_remainders():
    result = _case5_allocate(13, [1, 2, 3])
    assert result == [2, 4, 7]
    assert sum(result) == 13

"""Test P2: Proportional split with exact division and zero weights."""
import pytest as _case6_pytest
from solution import allocate as _case6_allocate

def test_p2_exact_division_zero_weight():
    result = _case6_allocate(10, [3, 0, 7])
    assert result == [3, 0, 7]
    assert sum(result) == 10
    assert len(result) == 3

"""Test P4: Single positive weight receives entire total."""
import pytest as _case7_pytest
from solution import allocate as _case7_allocate

def test_p4_single_weight():
    result = _case7_allocate(42, [1])
    assert result == [42]
    assert len(result) == 1
    assert isinstance(result, list)

"""Test P11: Result list sums exactly to total with distinct remainders."""
import pytest as _case8_pytest
from solution import allocate as _case8_allocate

def test_p11_sum_equals_total():
    result = _case8_allocate(7, [2, 3, 5])
    assert result == [1, 2, 4]
    assert sum(result) == 7
    assert all((isinstance(x, int) for x in result))

"""Test P7: Empty weights list raises ValueError."""
import pytest as _case9_pytest
from solution import allocate as _case9_allocate

def test_p7_empty_weights():
    with _case9_pytest.raises(ValueError):
        _case9_allocate(10, [])

"""Test P8: Negative weight entry raises ValueError."""
import pytest as _case10_pytest
from solution import allocate as _case10_allocate

def test_p8_negative_weight():
    with _case10_pytest.raises(ValueError):
        _case10_allocate(10, [2, -1, 3])

"""Test P9: All weights are zero raises ValueError."""
import pytest as _case11_pytest
from solution import allocate as _case11_allocate

def test_p9_all_zero_weights():
    with _case11_pytest.raises(ValueError):
        _case11_allocate(10, [0, 0, 0])
