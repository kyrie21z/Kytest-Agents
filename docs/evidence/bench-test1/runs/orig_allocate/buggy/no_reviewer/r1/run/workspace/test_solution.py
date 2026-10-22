# Accepted by submit_tests; explanations in testgen_report.json.

"""Test P2: Proportional split with zero-weight entry."""
import pytest as _case0_pytest
from solution import allocate as _case0_allocate

def test_p2_zero_weight_entry():
    """allocate(10, [3, 0, 7]) == [3, 0, 7].

    Docstring example. Spec explicitly states: 'Entries with weight 0
    always receive 0.'
    """
    result = _case0_allocate(10, [3, 0, 7])
    assert result == [3, 0, 7]
    assert result[1] == 0

"""Test P3: Minimum valid total."""
import pytest as _case1_pytest
from solution import allocate as _case1_allocate

def test_p3_minimum_total():
    """allocate(0, [2, 3]) == [0, 0].

    Spec allows 'non-negative integer total'. With total=0, floor(0*w/S)=0
    and remainder=0, yielding all zeros.
    """
    result = _case1_allocate(0, [2, 3])
    assert result == [0, 0]
    assert sum(result) == 0

"""Test P7: Negative total triggers ValueError."""
import pytest as _case2_pytest
from solution import allocate as _case2_allocate

def test_p7_negative_total():
    """allocate(-5, [1, 2]) raises ValueError.

    Spec explicitly states: 'Raises ValueError if total is negative'.
    """
    with _case2_pytest.raises(ValueError):
        _case2_allocate(-5, [1, 2])

"""Test P11: Multi-step remainder distribution."""
import pytest as _case3_pytest
from solution import allocate as _case3_allocate

def test_p11_multi_step_remainder():
    """allocate(10, [1, 2, 3]) == [2, 3, 5].

    Sums to 6. Base floors: [1, 3, 5]. Remainder=1. Fractional mods:
    [4, 2, 0]. Largest remainder belongs to index 0, which receives the
    extra unit. Spec: 'units left over are then handed out one each to
    the entries with the largest fractional remainder'.
    """
    result = _case3_allocate(10, [1, 2, 3])
    assert result == [2, 3, 5]
    assert sum(result) == 10

"""Test P4: Single positive weight."""
import pytest as _case4_pytest
from solution import allocate as _case4_allocate

def test_p4_single_positive_weight():
    """allocate(50, [1]) == [50].

    Spec requires 'at least one positive entry'. With only one entry, it
    must consume the entire total to satisfy proportionality and sum constraint.
    """
    result = _case4_allocate(50, [1])
    assert result == [50]
    assert len(result) == 1

"""Test P6: Sum invariant across multiple weights."""
import pytest as _case5_pytest
from solution import allocate as _case5_allocate

def test_p6_sum_invariant():
    """allocate(100, [1, 2, 3, 4, 5]) produces a list of 5 ints summing to 100.

    Spec guarantees: 'The result is a new list of ints, one per weight,
    summing to total.'
    """
    result = _case5_allocate(100, [1, 2, 3, 4, 5])
    assert len(result) == 5
    assert sum(result) == 100
    assert all((isinstance(x, int) for x in result))

"""Test P8: Empty weights list triggers ValueError."""
import pytest as _case6_pytest
from solution import allocate as _case6_allocate

def test_p8_empty_weights():
    """allocate(10, []) raises ValueError.

    Spec explicitly states: 'Raises ValueError if ... weights is empty'.
    """
    with _case6_pytest.raises(ValueError):
        _case6_allocate(10, [])

"""Test P9: Negative weight triggers ValueError."""
import pytest as _case7_pytest
from solution import allocate as _case7_allocate

def test_p9_negative_weight():
    """allocate(10, [1, -2, 3]) raises ValueError.

    Spec explicitly states: 'Raises ValueError if ... any weight is negative'.
    """
    with _case7_pytest.raises(ValueError):
        _case7_allocate(10, [1, -2, 3])

"""Test P10: All-zero weights triggers ValueError."""
import pytest as _case8_pytest
from solution import allocate as _case8_allocate

def test_p10_all_zero_weights():
    """allocate(10, [0, 0, 0]) raises ValueError.

    Spec explicitly states: 'Raises ValueError if ... all weights are zero.'
    Also violates precondition requiring 'at least one positive entry'.
    """
    with _case8_pytest.raises(ValueError):
        _case8_allocate(10, [0, 0, 0])

"""Test P12: Zero-weight isolation in mixed list."""
import pytest as _case9_pytest
from solution import allocate as _case9_allocate

def test_p12_zero_weight_isolation():
    """allocate(100, [0, 5, 0, 5]) == [0, 50, 0, 50].

    Confirms zero-weight entries strictly receive 0 regardless of position,
    while non-zero entries split proportionally. Spec: 'Entries with weight 0
    always receive 0.'
    """
    result = _case9_allocate(100, [0, 5, 0, 5])
    assert result == [0, 50, 0, 50]
    assert result[0] == 0
    assert result[2] == 0
