# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

"""P1: uniform weights, total not evenly divisible."""
import pytest
from solution import allocate
def test_p1_uniform_weights():
    result = allocate(100, [1, 1, 1])
    assert result == [34, 33, 33]
    assert sum(result) == 100

"""P4: tie-breaking rule – lower index wins."""
import pytest
from solution import allocate
def test_p4_tie_breaking():
    result = allocate(5, [1, 1])
    assert result == [3, 2]
    assert sum(result) == 5

"""P1: Returns equal-ish distribution when weights are uniform and total is not evenly divisible by count."""
import pytest as _case0_pytest
from solution import allocate as _case0_allocate

def test_p1_uniform_weights():
    result = _case0_allocate(100, [1, 1, 1])
    assert result == [34, 33, 33]
    assert sum(result) == 100

"""P4: Applies tie-breaking rule when multiple entries share the largest fractional remainder."""
import pytest as _case1_pytest
from solution import allocate as _case1_allocate

def test_p4_tie_breaking():
    result = _case1_allocate(5, [1, 1])
    assert result == [3, 2]
    assert sum(result) == 5
