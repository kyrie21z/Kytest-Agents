# New tests for solution.py — P1, P2, P3, P4, P7, P8, P9, P10
import pytest
from solution import factorial_sums


def test_p1_distinct_positive_integers():
    """Distinct positive integers [1, 2, 3].
    Docstring quote: 'Raises: TypeError: If numbers is not a list of integers.'
    Input domain: numbers = [1, 2, 3]
    Oracle: Returns ([9, 9, 9, 9, 9, 9], [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]).
      1!+2!+3! = 1+2+6 = 9 per permutation; 3! = 6 permutations.
    Faulty: Wrong sums or wrong permutation order/content."""
    expected_sums = [9, 9, 9, 9, 9, 9]
    expected_perms = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    fac, perm = factorial_sums([1, 2, 3])
    assert fac == expected_sums
    assert perm == expected_perms


def test_p2_zero_and_positive():
    """Zero and positive integer [0, 4].
    Docstring quote: 'Raises: TypeError: If numbers is not a list of integers.'
    Input domain: numbers = [0, 4]
    Oracle: Returns ([25, 25], [(0, 4), (4, 0)]).
      0!+4! = 1+24 = 25 per permutation; 2 permutations.
    Faulty: Wrong sums or wrong permutation content."""
    expected_sums = [25, 25]
    expected_perms = [(0, 4), (4, 0)]
    fac, perm = factorial_sums([0, 4])
    assert fac == expected_sums
    assert perm == expected_perms


def test_p3_empty_list():
    """Empty list input.
    Docstring quote: 'If an empty list is given, the function returns empty lists.'
    Input domain: numbers = []
    Oracle: Returns ([], []).
    Faulty: Non-empty result returned."""
    fac, perm = factorial_sums([])
    assert fac == []
    assert perm == []


def test_p4_single_element():
    """Single element list [5].
    Docstring quote: 'Raises: TypeError: If numbers is not a list of integers.'
    Input domain: numbers = [5]
    Oracle: Returns ([120], [(5,)]).
      5! = 120; one permutation of a single-element list.
    Faulty: Wrong sum or wrong permutation structure."""
    fac, perm = factorial_sums([5])
    assert fac == [120]
    assert perm == [(5,)]


def test_p7_negative_integers():
    """Negative integers [-1, 2].
    Docstring quote: 'Raises: ValueError: If input numbers are negative.'
    Input domain: numbers = [-1, 2]
    Oracle: Raises ValueError.
    Faulty: No exception raised or wrong exception type."""
    with pytest.raises(ValueError):
        factorial_sums([-1, 2])


def test_p8_duplicate_values():
    """Duplicate values [2, 2].
    Docstring quote: 'Raises: TypeError: If numbers is not a list of integers.'
    Input domain: numbers = [2, 2]
    Oracle: Returns ([4, 4], [(2, 2), (2, 2)]).
      2!+2! = 2+2 = 4 per permutation; itertools.permutations yields 2 tuples by position.
    Faulty: Wrong number of permutations or wrong sums."""
    expected_sums = [4, 4]
    expected_perms = [(2, 2), (2, 2)]
    fac, perm = factorial_sums([2, 2])
    assert fac == expected_sums
    assert perm == expected_perms


def test_p9_sum_consistency():
    """Sum consistency across permutations.
    Docstring quote: 'Returns: list of int: A list containing the sums of the factorials...'
    Input domain: numbers = [1, 2, 3]
    Oracle: All elements in the returned sums list are equal.
      Since every permutation contains the same multiset, the sum of factorials must be identical.
    Faulty: Sums differ across permutations."""
    fac, _ = factorial_sums([1, 2, 3])
    assert len(fac) > 0
    first = fac[0]
    for s in fac:
        assert s == first


def test_p10_return_structure():
    """Return structure unpacking for [1, 2].
    Docstring quote: 'Returns: list of int ... list of list of int'
    Input domain: numbers = [1, 2]
    Oracle: Unpacks successfully into exactly two variables: fac, perm = factorial_sums([1, 2]).
      fac should be a list, perm should be a list of tuples.
    Faulty: Return value does not unpack into two items or has wrong types."""
    result = factorial_sums([1, 2])
    # Must be a tuple/list of length 2
    assert isinstance(result, (list, tuple))
    assert len(result) == 2
    fac, perm = result
    assert isinstance(fac, list)
    assert isinstance(perm, list)
    # Each permutation should be a tuple
    for p in perm:
        assert isinstance(p, tuple)
