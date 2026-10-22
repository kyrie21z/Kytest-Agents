# Test P1: Verify [1, 2, 3] yields ([9, 9, 9, 9, 9, 9], [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]).
from solution import factorial_sums as _p1_factorial_sums
import pytest as _p1_pytest

def test_p1_distinct_positive_integers():
    """Test P1: Returns list of factorial sums and list of permutations for distinct positive integers."""
    fac, perm = _p1_factorial_sums([1, 2, 3])
    assert fac == [9, 9, 9, 9, 9, 9]
    assert perm == [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]


# Test P2: Verify [0, 4] yields ([25, 25], [(0, 4), (4, 0)]).
from solution import factorial_sums as _p2_factorial_sums
import pytest as _p2_pytest

def test_p2_zero_and_positive_integer():
    """Test P2: Returns list of factorial sums and list of permutations for zero and positive integer."""
    fac, perm = _p2_factorial_sums([0, 4])
    assert fac == [25, 25]
    assert perm == [(0, 4), (4, 0)]


# Test P3: Verify [] yields ([], []).
from solution import factorial_sums as _p3_factorial_sums
import pytest as _p3_pytest

def test_p3_empty_list():
    """Test P3: Handles empty input list."""
    fac, perm = _p3_factorial_sums([])
    assert fac == []
    assert perm == []


# Test P4: Verify [5] yields ([120], [(5,)]).
from solution import factorial_sums as _p4_factorial_sums
import pytest as _p4_pytest

def test_p4_single_element():
    """Test P4: Handles single-element list."""
    fac, perm = _p4_factorial_sums([5])
    assert fac == [120]
    assert perm == [(5,)]


# Test P7: Verify [-2, 3] raises ValueError.
from solution import factorial_sums as _p7_factorial_sums
import pytest as _p7_pytest

def test_p7_negative_integers():
    """Test P7: Rejects negative integers."""
    with _p7_pytest.raises(ValueError):
        _p7_factorial_sums([-2, 3])


# Test P8: Verify that for any valid input, all elements in the sums list are identical.
from solution import factorial_sums as _p8_factorial_sums
import pytest as _p8_pytest

def test_p8_consistent_sum_across_permutations():
    """Test P8: Maintains consistent sum across all permutations."""
    fac, perm = _p8_factorial_sums([1, 2, 3])
    # Since addition is commutative, the sum of factorials is the same for every permutation.
    assert len(fac) > 0
    first = fac[0]
    for val in fac:
        assert val == first


# Test P9: Verify [10] yields ([3628800], [(10,)]).
from solution import factorial_sums as _p9_factorial_sums
import pytest as _p9_pytest

def test_p9_larger_integer():
    """Test P9: Handles larger integer correctly."""
    fac, perm = _p9_factorial_sums([10])
    assert fac == [3628800]
    assert perm == [(10,)]


# Test P10: Verify [2, 3, 4] results in len(fac) == len(perm) == 6.
from solution import factorial_sums as _p10_factorial_sums
import pytest as _p10_pytest

def test_p10_output_lengths_match_permutation_count():
    """Test P10: Ensures output lengths match permutation count."""
    fac, perm = _p10_factorial_sums([2, 3, 4])
    assert len(fac) == 6
    assert len(perm) == 6
