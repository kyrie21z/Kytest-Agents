# Accepted by submit_tests; explanations in testgen_report.json.

"""P1 – Equal weights distribute total almost evenly, remainder to first index."""
from solution import allocate as _case0_allocate

def test_p1_equal_weights_remainder_first():
    """allocate(100, [1, 1, 1]) -> [34, 33, 33].

    Docstring example. sum(weights)=3, floors=[33,33,33], remainder=1 goes
    to index 0 due to tie-breaking rule (lower index wins).
    """
    result = _case0_allocate(100, [1, 1, 1])
    assert result == [34, 33, 33]

"""P2 – Zero-weight entries stay zero in proportional allocation."""
from solution import allocate as _case1_allocate

def test_p2_zero_weight_stays_zero():
    """allocate(10, [3, 0, 7]) -> [3, 0, 7].

    Spec: 'Entries with weight 0 always receive 0.' sum=10, floors=[3,0,7],
    leftover=0 so no redistribution needed.
    """
    result = _case1_allocate(10, [3, 0, 7])
    assert result == [3, 0, 7]

"""P3 – Zero total distributes nothing regardless of weights."""
from solution import allocate as _case2_allocate

def test_p3_zero_total():
    """allocate(0, [2, 3, 5]) -> [0, 0, 0].

    floor(0 * w / sum) = 0 for every w; leftover = 0 - 0 = 0.
    """
    result = _case2_allocate(0, [2, 3, 5])
    assert result == [0, 0, 0]

"""P4 – Single weight receives entire total."""
from solution import allocate as _case3_allocate

def test_p4_single_weight():
    """allocate(10, [5]) -> [10].

    Boundary case len(weights)==1. floor(10*5/5)=10, leftover=0.
    """
    result = _case3_allocate(10, [5])
    assert result == [10]

"""P5 – Result list always sums exactly to total."""
from solution import allocate as _case4_allocate

def test_p5_sum_equals_total():
    """allocate(7, [2, 3, 5]) -> [1, 2, 4]; sum(result) == 7.

    Calculation: floors=[1,2,3], remainders=[4,1,5], leftover=1.
    Largest remainder is at index 2, so it gets +1. Sum must equal total.
    """
    result = _case4_allocate(7, [2, 3, 5])
    assert result == [1, 2, 4]
    assert sum(result) == 7

"""P6 – Negative total raises ValueError."""
from solution import allocate as _case5_allocate
import pytest as _case5_pytest

def test_p6_negative_total():
    """allocate(-5, [1, 2]) raises ValueError.

    Spec: 'Raises ValueError if total is negative'.
    """
    with _case5_pytest.raises(ValueError):
        _case5_allocate(-5, [1, 2])

"""P7 – Empty weights list raises ValueError."""
from solution import allocate as _case6_allocate
import pytest as _case6_pytest

def test_p7_empty_weights():
    """allocate(10, []) raises ValueError.

    Spec: 'Raises ValueError if weights is empty'.
    """
    with _case6_pytest.raises(ValueError):
        _case6_allocate(10, [])

"""P8 – Negative weight raises ValueError."""
from solution import allocate as _case7_allocate
import pytest as _case7_pytest

def test_p8_negative_weight():
    """allocate(10, [1, -2, 3]) raises ValueError.

    Spec: 'Raises ValueError if any weight is negative'.
    """
    with _case7_pytest.raises(ValueError):
        _case7_allocate(10, [1, -2, 3])

"""P9 – All-zero weights raises ValueError."""
from solution import allocate as _case8_allocate
import pytest as _case8_pytest

def test_p9_all_zero_weights():
    """allocate(10, [0, 0, 0]) raises ValueError.

    Spec: 'Raises ValueError if all weights are zero' (division by zero).
    """
    with _case8_pytest.raises(ValueError):
        _case8_allocate(10, [0, 0, 0])

"""P10 – Tie-breaking rule favors lower indices when remainders are equal."""
from solution import allocate as _case9_allocate

def test_p10_tie_breaking_lower_index():
    """allocate(5, [1, 1, 1]) -> [2, 2, 1].

    Floors=[1,1,1], remainders=[2,2,2], leftover=2.
    Ties go to lower index, so indices 0 and 1 each get +1.
    """
    result = _case9_allocate(5, [1, 1, 1])
    assert result == [2, 2, 1]

"""P11 – Zero-weight entries strictly receive zero even with large total."""
from solution import allocate as _case10_allocate

def test_p11_zero_weight_large_total():
    """allocate(10, [0, 5, 0]) -> [0, 10, 0].

    Spec: 'Entries with weight 0 always receive 0.'
    """
    result = _case10_allocate(10, [0, 5, 0])
    assert result == [0, 10, 0]

"""P12 – Total smaller than positive weights gives one unit to lowest index."""
from solution import allocate as _case11_allocate

def test_p12_total_smaller_than_positive_weights():
    """allocate(1, [1, 1, 1, 1, 1]) -> [1, 0, 0, 0, 0].

    Floors all 0, remainders all 1/5, leftover=1. Tie breaks to index 0.
    """
    result = _case11_allocate(1, [1, 1, 1, 1, 1])
    assert result == [1, 0, 0, 0, 0]

"""Extra – Return type is a list of ints."""
from solution import allocate as _case12_allocate

def test_extra_return_type():
    """Result is a list of integers matching weights length."""
    result = _case12_allocate(100, [1, 1, 1])
    assert isinstance(result, list)
    assert len(result) == 3
    assert all((isinstance(v, int) for v in result))

"""Extra – Large total with varied weights preserves proportionality."""
from solution import allocate as _case13_allocate

def test_extra_large_varied_weights():
    """allocate(1000, [1, 2, 3, 4]) -> shares summing to 1000."""
    result = _case13_allocate(1000, [1, 2, 3, 4])
    assert sum(result) == 1000
    assert all((v >= 0 for v in result))

"""Extra – Two-element weights with exact division."""
from solution import allocate as _case14_allocate

def test_extra_exact_division_two():
    """allocate(10, [2, 8]) -> [2, 8] (exact proportional split)."""
    result = _case14_allocate(10, [2, 8])
    assert result == [2, 8]
    assert sum(result) == 10
