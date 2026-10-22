# Accepted by submit_tests; explanations in testgen_report.json.

# Accepted by submit_tests; explanations in testgen_report.json.

import pytest as _case0_pytest
from solution import allocate as _case0_allocate

def test_p3_minimum_total_zero():
    """P3: Minimum valid total (zero).
    
    Spec quote: 'Split a non-negative integer total into integer shares'
    Input domain: total=0, weights=[2,3].
    Oracle: floor(0*w/S)=0 for all, leftover=0. All zeros.
    Fault hypothesis: might return non-zero or wrong length.
    """
    result = _case0_allocate(0, [2, 3])
    assert result == [0, 0]
    assert sum(result) == 0

import pytest as _case1_pytest
from solution import allocate as _case1_allocate

def test_p4_single_weight_entry():
    """P4: Single weight entry.
    
    Spec quote: 'weights is a list of non-negative ints with at least one positive entry.'
    Input domain: total=5, weights=[1].
    Oracle: S=1, base=[5], leftover=0. Full total to single entry.
    Fault hypothesis: might fail on single-element list.
    """
    result = _case1_allocate(5, [1])
    assert result == [5]
    assert len(result) == 1

import pytest as _case2_pytest
from solution import allocate as _case2_allocate

def test_p5_remainder_distribution_no_ties():
    """P5: Remainder distribution without ties.
    
    Plan rationale: S=6. Base: floor(10/6)=1, floor(20/6)=3, floor(30/6)=5. Sum=9, leftover=1. Remainders: 10%6=4, 20%6=2, 30%6=0. Largest remainder is index 0, which receives the extra unit.
    Input domain: total=10, weights=[1,2,3].
    Oracle: result=[2,3,5].
    Fault hypothesis: remainder sorting might be wrong direction or tie-breaking broken.
    """
    result = _case2_allocate(10, [1, 2, 3])
    assert result == [2, 3, 5]
    assert sum(result) == 10

import pytest as _case3_pytest
from solution import allocate as _case3_allocate

def test_p2_mixed_weights_zero_entry_exact():
    """P2: Mixed weights including zero entry with exact division.
    
    Docstring quote: 'Entries with weight 0 always receive 0.'
    Input domain: total=10, weights=[3,0,7].
    Oracle: S=10, base=[3,0,7], leftover=0. Zero weight gets 0.
    Fault hypothesis: zero-weight entry might get a non-zero share.
    """
    result = _case3_allocate(10, [3, 0, 7])
    assert result == [3, 0, 7]
    assert result[1] == 0

import pytest as _case4_pytest
from solution import allocate as _case4_allocate

def test_p8_negative_total():
    """P8: Negative total triggers ValueError.
    
    Docstring quote: 'Raises ValueError if total is negative, weights is empty'
    Input domain: total=-5, weights=[1,2].
    Oracle: Should raise ValueError.
    Fault hypothesis: might silently accept negative total.
    """
    with _case4_pytest.raises(ValueError):
        _case4_allocate(-5, [1, 2])

import pytest as _case5_pytest
from solution import allocate as _case5_allocate

def test_p9_empty_weights():
    """P9: Empty weights list triggers ValueError.
    
    Docstring quote: 'Raises ValueError if total is negative, weights is empty'
    Input domain: total=10, weights=[].
    Oracle: Should raise ValueError.
    Fault hypothesis: might crash with IndexError or return empty list.
    """
    with _case5_pytest.raises(ValueError):
        _case5_allocate(10, [])

import pytest as _case6_pytest
from solution import allocate as _case6_allocate

def test_p10_negative_weight():
    """P10: Negative weight triggers ValueError.
    
    Docstring quote: 'Raises ValueError if total is negative, weights is empty, any weight is'
    Input domain: total=10, weights=[1,-1].
    Oracle: Should raise ValueError.
    Fault hypothesis: might accept negative weight and produce wrong allocation.
    """
    with _case6_pytest.raises(ValueError):
        _case6_allocate(10, [1, -1])

import pytest as _case7_pytest
from solution import allocate as _case7_allocate

def test_p11_all_zero_weights():
    """P11: All-zero weights triggers ValueError.
    
    Docstring quote: 'Raises ValueError if total is negative, weights is empty, any weight is'
    Input domain: total=10, weights=[0,0].
    Oracle: Should raise ValueError (prevents division by zero).
    Fault hypothesis: might crash with ZeroDivisionError instead of ValueError.
    """
    with _case7_pytest.raises(ValueError):
        _case7_allocate(10, [0, 0])

import pytest as _case8_pytest
from solution import allocate as _case8_allocate

def test_extra_large_weights_small_total():
    """Extra: Large weights with small total.
    
    Spec quote: 'Every entry first receives floor(total * w / sum(weights)).'
    Input domain: total=1, weights=[100,200,300].
    Oracle: S=600, base=[0,0,0], leftover=1, remainders=[100,200,300], largest is idx2 -> [0,0,1].
    Fault hypothesis: remainder ranking might be inverted.
    """
    result = _case8_allocate(1, [100, 200, 300])
    assert result == [0, 0, 1]
    assert sum(result) == 1


import pytest as _newf91c6bd90_pytest
from solution import allocate as _newf91c6bd90_allocate

def test_p7_result_length_and_sum():
    """P7: Result list length matches input weights length.

    Spec quote: 'The result is a new list of ints, one per weight, summing to total.'
    Input domain: total=50, weights=[10,20,30].
    Oracle: S=60, base=[8,16,25], remainders=[20,40,0], leftover=1. Largest remainder is index 1 (40), so index 1 gets +1 → [8,17,25]. Sum=50 matches total.
    Fault hypothesis: output length differs from input length, or sum != total.
    """
    result = _newf91c6bd90_allocate(50, [10, 20, 30])
    assert result == [8, 17, 25]
    assert sum(result) == 50
    assert len(result) == 3
