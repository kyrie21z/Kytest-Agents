# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

import pytest
from solution import allocate

def test_p6_tie_breaking_lower_index():
    """P6: Tie-breaking rule for equal fractional remainders.
    
    Plan rationale: S=2. Base: 0, 0. Leftover=1. Remainders: 1%2=1 for both. Spec states 'ties go to the entry with the lower index', so index 0 gets the unit. Result [1, 0].
    Input domain: total=1, weights=[1,1].
    Oracle: result=[1,0].
    Fault hypothesis: tie-breaking might give unit to higher index.
    """
    result = allocate(1, [1, 1])
    assert result == [1, 0]
    assert sum(result) == 1

import pytest
from solution import allocate

def test_p1_equal_weights_odd_remainder():
    """P1: Equal weights with odd total requiring remainder distribution.
    
    Docstring quote: 'Every entry first receives floor(total * w / sum(weights)).'
    Input domain: total=100, weights=[1,1,1].
    Oracle: S=3, base=floor(100/3)=33 each, leftover=1, rem=[1,1,1], idx0 gets +1.
    Fault hypothesis: implementation might distribute remainder differently or use round().
    """
    result = allocate(100, [1, 1, 1])
    assert result == [34, 33, 33]
    assert len(result) == 3
    assert sum(result) == 100

import pytest
from solution import allocate

def test_extra_zero_weight_with_remainder():
    """Extra: Zero-weight entry never gets extra units even with remainder.
    
    Spec quote: 'Entries with weight 0 always receive 0.'
    Input domain: total=11, weights=[0,5,5].
    Oracle: S=10, base=[0,5,5], leftover=1, remainders=[0,5,5], idx1 gets +1 -> [0,6,5].
    Fault hypothesis: zero-weight entry might incorrectly receive an extra unit.
    """
    result = allocate(11, [0, 5, 5])
    assert result == [0, 6, 5]
    assert result[0] == 0
    assert sum(result) == 11

import pytest
from solution import allocate

def test_p1_equal_weights_remainder():
    """P1: Equal weights with odd total requiring remainder distribution.

    Docstring quote: '>>> allocate(100, [1, 1, 1])\n    [34, 33, 33]'
    Input domain: total=100, weights=[1,1,1].
    Oracle: S=3, base=[33,33,33], remainders=[1,1,1], leftover=1. All remainders tied; spec says 'ties go to the entry with the lower index', so index 0 gets +1 → [34,33,33].
    Fault hypothesis: sorting key (-remainders[i], -i) breaks ties by higher index, producing [33,33,34] instead.
    """
    result = allocate(100, [1, 1, 1])
    assert result == [34, 33, 33]
    assert sum(result) == 100
    assert len(result) == 3

import pytest
from solution import allocate

def test_p6_tie_lower_index_wins():
    """P6: Tie-breaking rule for equal fractional remainders.

    Spec quote: 'ties go to the entry with the lower index'
    Input domain: total=1, weights=[1,1].
    Oracle: S=2, base=[0,0], remainders=[1,1], leftover=1. Both tied at remainder 1; lower index 0 wins → [1,0].
    Fault hypothesis: implementation gives priority to higher index, producing [0,1].
    """
    result = allocate(1, [1, 1])
    assert result == [1, 0]
    assert sum(result) == 1
    assert len(result) == 2

import pytest
from solution import allocate

def test_extra_zero_weight_with_remainder():
    """Extra: Zero-weight entry with tie involving non-zero entries.

    Spec quote: 'ties go to the entry with the lower index'
    Input domain: total=1, weights=[1,0,1].
    Oracle: S=2, base=[0,0,0], remainders=[1,0,1], leftover=1. Indices 0 and 2 tied at remainder 1; lower index 0 wins → [1,0,0]. Weight-0 entry stays 0.
    Fault hypothesis: higher index wins the tie (producing [0,0,1]), violating both the tie-breaking rule and potentially zero-weight guarantee.
    """
    result = allocate(1, [1, 0, 1])
    assert result == [1, 0, 0]
    assert sum(result) == 1
    assert result[1] == 0  # zero-weight entry must stay 0
