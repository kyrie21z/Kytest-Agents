# New test candidates for revision — submitted via submit_tests.

from solution import factorial_sums as _case2_factorial_sums

def test_positive_integers():
    """Verify core computation with valid positive integers [1, 2, 3].
    Contract example: fac=[9,9,9,9,9,9], perm has 6 permutations.
    Each permutation's factorial sum is 1!+2!+3! = 1+2+6 = 9.
    This covers the permutation generation and factorial summation logic,
    killing the 'Add -> Sub' mutation survivor."""
    result = _case2_factorial_sums([1, 2, 3])
    assert isinstance(result, tuple)
    assert len(result) == 2
    sums, perms = result
    assert len(sums) == 6
    assert all(s == 9 for s in sums)
    assert len(perms) == 6
    # Verify all 6 permutations are present
    expected_perms = {
        (1, 2, 3), (1, 3, 2), (2, 1, 3),
        (2, 3, 1), (3, 1, 2), (3, 2, 1)
    }
    assert set(perms) == expected_perms


from solution import factorial_sums as _case3_factorial_sums

def test_zero_in_input():
    """Verify that input containing zero (e.g., [0, 4]) is accepted.
    Contract: non-negative check permits 0. 0! = 1, so 0!+4! = 1+24 = 25.
    Two permutations: (0,4) and (4,0).
    This kills the 'constant 0 -> 1' mutation survivor that would reject 0."""
    result = _case3_factorial_sums([0, 4])
    assert isinstance(result, tuple)
    assert len(result) == 2
    sums, perms = result
    assert len(sums) == 2
    assert all(s == 25 for s in sums)
    assert len(perms) == 2
    assert set(perms) == {(0, 4), (4, 0)}


import pytest as _case4_pytest
from solution import factorial_sums as _case4_factorial_sums

def test_negative_numbers():
    """Verify ValueError is raised when input contains negative numbers.
    Contract: 'ValueError: If input numbers are negative.'"""
    with _case4_pytest.raises(ValueError):
        _case4_factorial_sums([-1])
    with _case4_pytest.raises(ValueError):
        _case4_factorial_sums([1, -5, 3])


import pytest as _case5_pytest
from solution import factorial_sums as _case5_factorial_sums

def test_non_integer_elements():
    """Verify TypeError is raised when list contains non-integer elements.
    Contract: 'TypeError: If numbers is not a list of integers.'"""
    with _case5_pytest.raises(TypeError):
        _case5_factorial_sums([1.5])
    with _case5_pytest.raises(TypeError):
        _case5_factorial_sums(['a'])
    with _case5_pytest.raises(TypeError):
        _case5_factorial_sums([1, 2.0])
