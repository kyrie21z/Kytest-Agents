# Accepted by submit_tests; explanations in testgen_report.json.

import pytest as _case0_pytest
from solution import allocate as _case0_allocate

def test_zero_weight_entry():
    """Test that entries with weight 0 always receive 0."""
    result = _case0_allocate(10, [3, 0, 7])
    assert result == [3, 0, 7]

import pytest as _case1_pytest
from solution import allocate as _case1_allocate

def test_negative_total_raises_value_error():
    """Test that a negative total raises ValueError."""
    with _case1_pytest.raises(ValueError):
        _case1_allocate(-1, [1, 2, 3])

import pytest as _case2_pytest
from solution import allocate as _case2_allocate

def test_empty_weights_raises_value_error():
    """Test that an empty weights list raises ValueError."""
    with _case2_pytest.raises(ValueError):
        _case2_allocate(10, [])

import pytest as _case3_pytest
from solution import allocate as _case3_allocate

def test_all_zero_weights_raises_value_error():
    """Test that all-zero weights raise ValueError."""
    with _case3_pytest.raises(ValueError):
        _case3_allocate(10, [0, 0, 0])

import pytest as _case4_pytest
from solution import allocate as _case4_allocate

def test_sum_equals_total():
    """Test that the sum of shares always equals total across multiple inputs."""
    for total, weights in [(100, [1, 1, 1]), (10, [3, 0, 7]), (7, [2, 3, 5]), (1, [1, 2, 3]), (0, [5, 3, 2]), (13, [4, 4, 4])]:
        result = _case4_allocate(total, weights)
        assert sum(result) == total

import pytest as _case5_pytest
from solution import allocate as _case5_allocate

def test_equal_weights_docstring():
    """Test the first docstring example: equal weights split total as evenly as possible."""
    result = _case5_allocate(100, [1, 1, 1])
    assert result == [33, 33, 34]
