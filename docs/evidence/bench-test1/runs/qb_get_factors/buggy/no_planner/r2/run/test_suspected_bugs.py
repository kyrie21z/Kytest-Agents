# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

from solution import get_factors

def test_get_factors_100():
    """Contract: get_factors(100) returns [2, 2, 5, 5]"""
    result = get_factors(100)
    assert result == [2, 2, 5, 5]
    assert isinstance(result, list)

from solution import get_factors

def test_get_factors_prime_101():
    """Contract: get_factors(101) returns [101] since 101 is prime."""
    result = get_factors(101)
    assert result == [101]
    assert isinstance(result, list)
    assert len(result) == 1

from solution import get_factors

def test_get_factors_two():
    """Boundary: get_factors(2) returns [2], the smallest prime."""
    result = get_factors(2)
    assert result == [2]
    assert isinstance(result, list)
    assert len(result) == 1

from solution import get_factors

def test_get_factors_three():
    """Boundary: get_factors(3) returns [3], another small prime."""
    result = get_factors(3)
    assert result == [3]
    assert isinstance(result, list)
    assert len(result) == 1

from solution import get_factors

def test_get_factors_six():
    """Composite product: get_factors(6) returns [2, 3]."""
    result = get_factors(6)
    assert result == [2, 3]
    assert isinstance(result, list)
    assert len(result) == 2

from solution import get_factors

def test_get_factors_eight():
    """Power of two: get_factors(8) returns [2, 2, 2]."""
    result = get_factors(8)
    assert result == [2, 2, 2]
    assert isinstance(result, list)
    assert len(result) == 3

from solution import get_factors

def test_get_factors_twelve():
    """Composite: get_factors(12) returns [2, 2, 3]."""
    result = get_factors(12)
    assert result == [2, 2, 3]
    assert isinstance(result, list)
    assert len(result) == 3

from solution import get_factors

def test_get_factors_four():
    """Composite square: get_factors(4) returns [2, 2]."""
    result = get_factors(4)
    assert result == [2, 2]
    assert isinstance(result, list)
    assert len(result) == 2

from solution import get_factors

def test_get_factors_prime_2():
    """Smallest prime boundary: get_factors(2) returns [2]."""
    result = get_factors(2)
    assert result == [2]
    assert isinstance(result, list)
    assert len(result) == 1

from solution import get_factors

def test_get_factors_prime_3():
    """Small prime: get_factors(3) returns [3]."""
    result = get_factors(3)
    assert result == [3]
    assert isinstance(result, list)
    assert len(result) == 1

from solution import get_factors

def test_get_factors_prime_5():
    """Prime above sqrt threshold: get_factors(5) returns [5]."""
    result = get_factors(5)
    assert result == [5]
    assert isinstance(result, list)
    assert len(result) == 1

from solution import get_factors

def test_get_factors_prime_7():
    """Prime: get_factors(7) returns [7]."""
    result = get_factors(7)
    assert result == [7]
    assert isinstance(result, list)
    assert len(result) == 1
