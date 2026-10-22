# Accepted by submit_tests; explanations in testgen_report.json.

"""Test the first docstring example: equal weights split total."""
from solution import allocate as _case0_allocate

def test_basic_equal_weights():
    """'>>> allocate(100, [1, 1, 1])
     [34, 33, 33]'

    Three equal weights split 100: each gets floor(100/3)=33, one unit
    leftover goes to index 0 (largest remainder tie-break).
    Expected: [34, 33, 33].
    Faulty behaviour detected: wrong distribution when leftovers exist.
    """
    result = _case0_allocate(100, [1, 1, 1])
    assert result == [34, 33, 33]

"""Test the second docstring example: a zero-weight entry."""
from solution import allocate as _case1_allocate

def test_zero_weight_entry():
    """'>>> allocate(10, [3, 0, 7])
     [3, 0, 7]'

    Weight-0 entry must always receive 0; remaining total splits
    proportionally between weights 3 and 7.
    Expected: [3, 0, 7].
    Faulty behaviour detected: non-zero share given to weight-0 entry.
    """
    result = _case1_allocate(10, [3, 0, 7])
    assert result == [3, 0, 7]

"""Test that negative total raises ValueError."""
from solution import allocate as _case2_allocate
import pytest as _case2_pytest

def test_negative_total_raises_value_error():
    """'Raises ValueError if total is negative …'

    Passing a negative total violates the precondition.
    Expected: ValueError raised.
    Faulty behaviour detected: silently accepting negative total.
    """
    with _case2_pytest.raises(ValueError):
        _case2_allocate(-1, [1, 2, 3])

"""Test that empty weights list raises ValueError."""
from solution import allocate as _case3_allocate
import pytest as _case3_pytest

def test_empty_weights_raises_value_error():
    """'Raises ValueError if … weights is empty …'

    An empty weight list has no valid allocation.
    Expected: ValueError raised.
    Faulty behaviour detected: returning an unexpected result for empty input.
    """
    with _case3_pytest.raises(ValueError):
        _case3_allocate(10, [])

"""Test that all-zero weights raises ValueError."""
from solution import allocate as _case4_allocate
import pytest as _case4_pytest

def test_all_zero_weights_raises_value_error():
    """'Raises ValueError if … all weights are zero.'

    With no positive weight there is nothing to allocate to.
    Expected: ValueError raised.
    Faulty behaviour detected: infinite loop or incorrect return.
    """
    with _case4_pytest.raises(ValueError):
        _case4_allocate(10, [0, 0, 0])

"""Test remainder-based bonus assignment with unequal weights."""
from solution import allocate as _case5_allocate

def test_weighted_remainder_distribution():
    """Manual calculation for allocate(10, [1, 2, 3]).

    whole = 6. Base shares: [10*1//6=1, 10*2//6=3, 10*3//6=5] = [1,3,5].
    Remainders: [10%6=4, 20%6=2, 30%6=0] = [4,2,0].
    Leftover = 10 - 9 = 1. Sorted by (-rem, idx): [(4,0),(2,1),(0,2)].
    One unit to index 0 → [2, 3, 5].
    Expected: [2, 3, 5].
    Faulty behaviour detected: incorrect remainder-based bonus assignment.
    """
    result = _case5_allocate(10, [1, 2, 3])
    assert result == [2, 3, 5]

"""Test that zero total yields all-zero shares."""
from solution import allocate as _case6_allocate

def test_total_is_zero():
    """When total is 0 every share must be 0 regardless of weights.

    floor(0 * w / sum) = 0 for every w; leftover = 0.
    Expected: [0, 0, 0].
    Faulty behaviour detected: non-zero entries returned for zero total.
    """
    result = _case6_allocate(0, [1, 2, 3])
    assert result == [0, 0, 0]

"""Test that returned shares always sum to the requested total."""
from solution import allocate as _case7_allocate

def test_sum_equals_total_invariant():
    """The returned shares must always sum to the requested total.

    This is a core invariant stated in the docstring: '…summing to total'.
    Faulty behaviour detected: shares not summing to total.
    """
    result = _case7_allocate(100, [1, 2, 3, 4, 5])
    assert sum(result) == 100
    assert all((isinstance(s, int) for s in result))

"""Test that any negative weight raises ValueError."""
from solution import allocate as _case8_allocate
import pytest as _case8_pytest

def test_negative_weight_raises_value_error():
    """'Raises ValueError if … any weight is negative …'

    A negative weight violates the precondition.
    Expected: ValueError raised.
    Faulty behaviour detected: silently accepting negative weight.
    """
    with _case8_pytest.raises(ValueError):
        _case8_allocate(10, [1, -2, 3])

"""Test tie-breaking: same remainder, lower index wins."""
from solution import allocate as _case9_allocate

def test_tie_breaking_remainders():
    """allocate(5, [2, 2]): manual calculation.

    whole = 4. Base shares: [5*2//4=2, 5*2//4=2] = [2,2].
    Remainders: [5*2%4=2, 5*2%4=2] = [2,2].
    Leftover = 5 - 4 = 1. Sorted by (-rem,idx): [(2,0),(2,1)].
    One unit to index 0 (lower index wins tie) → [3, 2].
    Expected: [3, 2].
    Faulty behaviour detected: higher index gets the bonus instead of lower.
    """
    result = _case9_allocate(5, [2, 2])
    assert result == [3, 2]

"""Test multiple leftovers distributed by descending remainder."""
from solution import allocate as _case10_allocate

def test_multiple_leftovers_correctly_distributed():
    """allocate(20, [1, 2, 3, 4]): manual calculation.

    whole = 10. Base: [20*1//10=2, 20*2//10=4, 20*3//10=6, 20*4//10=8] = [2,4,6,8].
    Remainders: [20%10=0, 40%10=0, 60%10=0, 80%10=0] = [0,0,0,0].
    Leftover = 20 - 20 = 0 → [2,4,6,8].
    Now try allocate(21, [1, 2, 3, 4]):
    Base: [2,4,6,8], Remainders: [1,2,3,4], Leftover=1.
    Sorted: [(4,3),(3,2),(2,1),(1,0)] → bonus to index 3 → [2,4,6,9].
    Expected: [2, 4, 6, 9].
    Faulty behaviour detected: leftover not assigned to highest-remainder entry.
    """
    result = _case10_allocate(21, [1, 2, 3, 4])
    assert result == [2, 4, 6, 9]

"""Test that a single weight returns the entire total."""
from solution import allocate as _case11_allocate

def test_single_weight_returns_total():
    """When there is exactly one weight the entire total goes to that entry.

    Contract says every entry receives floor(total*w/sum(w)); with one
    element this is floor(total*1/1) = total, and leftover = 0.
    Expected: [total].
    Faulty behaviour detected: truncation or extra logic modifying single-element result.
    """
    result = _case11_allocate(42, [7])
    assert result == [42]
    assert isinstance(result, list)
    assert len(result) == 1

"""Test that zero-weight entries always receive zero allocation."""
from solution import allocate as _case12_allocate

def test_entries_with_zero_weight_always_zero():
    """Every entry whose weight is 0 must receive exactly 0.

    Contract: 'Entries with weight 0 always receive 0.'
    Faulty behaviour detected: any non-zero value at a zero-weight position.
    """
    result = _case12_allocate(100, [0, 5, 0, 10])
    assert result[0] == 0
    assert result[2] == 0
    assert result[1] > 0
    assert result[3] > 0

"""Test many leftovers distributed correctly across multiple entries."""
from solution import allocate as _case13_allocate

def test_large_leftover_distribution():
    """allocate(100, [1, 1, 1]): three equal weights.

    whole=3. Base: [33,33,33]. Remainders: [1,1,1]. Leftover=1.
    Sorted by (-rem,idx): [(1,0),(1,1),(1,2)]. One unit to index 0.
    Expected: [34, 33, 33].
    Also test allocate(7, [1, 1, 1, 1, 1, 1, 1]):
    whole=7. Base: [1]*7. Remainders: [0]*7. Leftover=0.
    Expected: [1, 1, 1, 1, 1, 1, 1].
    Faulty behaviour detected: leftover distribution fails with many entries.
    """
    r1 = _case13_allocate(100, [1, 1, 1])
    assert r1 == [34, 33, 33]
    r2 = _case13_allocate(7, [1, 1, 1, 1, 1, 1, 1])
    assert r2 == [1, 1, 1, 1, 1, 1, 1]

"""Test case where total divides evenly among weights with no remainder."""
from solution import allocate as _case14_allocate

def test_exact_division_no_leftover():
    """allocate(12, [1, 1, 1]): whole=3, each gets 12/3=4 exactly.

    Base: [4,4,4], Remainders: [0,0,0], Leftover=0.
    Expected: [4, 4, 4].
    Faulty behaviour detected: spurious leftover units distributed when none exist.
    """
    result = _case14_allocate(12, [1, 1, 1])
    assert result == [4, 4, 4]

"""Test that all returned shares are non-negative."""
from solution import allocate as _case15_allocate

def test_all_shares_non_negative():
    """Every share must be >= 0 since total >= 0 and weights >= 0.

    Contract implies non-negative shares (floor of non-negative values).
    Faulty behaviour detected: negative share produced by arithmetic error.
    """
    result = _case15_allocate(50, [3, 7, 2, 8])
    assert all((s >= 0 for s in result))
    assert result == [8, 17, 5, 20]

"""Test allocation across many entries with varied weights."""
from solution import allocate as _case16_allocate

def test_many_entries_with_varied_weights():
    """allocate(30, [1, 2, 3, 4, 5, 6, 7, 8]).

    whole=36. Base: [0,1,2,3,4,5,5,6]. Remainders: [30,24,18,12,6,0,30,24].
    Leftover=30-26=4. Sorted:(30,0),(30,6),(24,1),(24,7),(18,2),(12,3),(6,4),(0,5).
    Four units to indices 0,6,1,7 → [1,2,2,3,4,5,6,7].
    Expected: [1, 2, 2, 3, 4, 5, 6, 7].
    Faulty behaviour detected: wrong entry gets the bonus unit.
    """
    result = _case16_allocate(30, [1, 2, 3, 4, 5, 6, 7, 8])
    assert result == [1, 2, 2, 3, 4, 5, 6, 7]
    assert sum(result) == 30
