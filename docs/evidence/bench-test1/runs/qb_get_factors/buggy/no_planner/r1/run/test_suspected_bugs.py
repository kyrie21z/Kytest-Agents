# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

def test_prime_two():
    """Test that get_factors(2) returns [2] since 2 is prime."""
    from solution import get_factors
    result = get_factors(2)
    assert isinstance(result, list)
    assert result == [2]

def test_square_of_two():
    """Test that get_factors(4) returns [2, 2]."""
    from solution import get_factors
    result = get_factors(4)
    assert isinstance(result, list)
    assert result == [2, 2]

def test_cube_of_two():
    """Test that get_factors(8) returns [2, 2, 2]."""
    from solution import get_factors
    result = get_factors(8)
    assert isinstance(result, list)
    assert result == [2, 2, 2]

def test_prime_three():
    """Test that get_factors(3) returns [3] since 3 is prime."""
    from solution import get_factors
    result = get_factors(3)
    assert isinstance(result, list)
    assert result == [3]

def test_docstring_100():
    """Test the docstring example: get_factors(100) == [2, 2, 5, 5]."""
    from solution import get_factors
    result = get_factors(100)
    assert isinstance(result, list)
    assert result == [2, 2, 5, 5]

def test_docstring_101():
    """Test the docstring example: get_factors(101) == [101]."""
    from solution import get_factors
    result = get_factors(101)
    assert isinstance(result, list)
    assert result == [101]

def test_prime_seven():
    """Test that get_factors(7) returns [7], since 7 is prime."""
    from solution import get_factors
    result = get_factors(7)
    assert isinstance(result, list)
    assert result == [7], f'get_factors(7) returned {result}, expected [7] for prime 7'

def test_composite_14():
    """Test that get_factors(14) returns [2, 7], not [2]."""
    from solution import get_factors
    result = get_factors(14)
    assert isinstance(result, list)
    assert result == [2, 7], f'get_factors(14) returned {result}, expected [2, 7]'

def test_composite_49():
    """Test that get_factors(49) returns [7, 7], not [7]."""
    from solution import get_factors
    result = get_factors(49)
    assert isinstance(result, list)
    assert result == [7, 7], f'get_factors(49) returned {result}, expected [7, 7]'

def test_composite_21():
    """Test that get_factors(21) returns [3, 7], not [3]."""
    from solution import get_factors
    result = get_factors(21)
    assert isinstance(result, list)
    assert result == [3, 7], f'get_factors(21) returned {result}, expected [3, 7]'

def test_prime_two():
    """Test that get_factors(2) returns [2], since 2 is prime."""
    from solution import get_factors
    result = get_factors(2)
    assert isinstance(result, list)
    assert result == [2], f'get_factors(2) returned {result}, expected [2] for prime 2'

def test_prime_101():
    """Test that get_factors(101) returns [101], per the docstring example."""
    from solution import get_factors
    result = get_factors(101)
    assert isinstance(result, list)
    assert result == [101], f'get_factors(101) returned {result}, expected [101] as shown in docstring'

def test_prime_three():
    """Test that get_factors(3) returns [3], since 3 is prime."""
    from solution import get_factors
    result = get_factors(3)
    assert isinstance(result, list)
    assert result == [3], f'get_factors(3) returned {result}, expected [3] for prime 3'

def test_prime_eleven():
    """Test that get_factors(11) returns [11], since 11 is prime."""
    from solution import get_factors
    result = get_factors(11)
    assert isinstance(result, list)
    assert result == [11], f'get_factors(11) returned {result}, expected [11] for prime 11'

def test_composite_6():
    """Test that get_factors(6) returns [2, 3], not [2]."""
    from solution import get_factors
    result = get_factors(6)
    assert isinstance(result, list)
    assert result == [2, 3], f'get_factors(6) returned {result}, expected [2, 3]'

def test_composite_15():
    """Test that get_factors(15) returns [3, 5], not [3]."""
    from solution import get_factors
    result = get_factors(15)
    assert isinstance(result, list)
    assert result == [3, 5], f'get_factors(15) returned {result}, expected [3, 5]'

def test_composite_100():
    """Test that get_factors(100) returns [2, 2, 5, 5], per the docstring example."""
    from solution import get_factors
    result = get_factors(100)
    assert isinstance(result, list)
    assert result == [2, 2, 5, 5], f'get_factors(100) returned {result}, expected [2, 2, 5, 5]'

def test_composite_8():
    """Test that get_factors(8) returns [2, 2, 2], not [2, 2]."""
    from solution import get_factors
    result = get_factors(8)
    assert isinstance(result, list)
    assert result == [2, 2, 2], f'get_factors(8) returned {result}, expected [2, 2, 2]'

def test_factor_100_matches_docstring():
    """Test that get_factors(100) returns [2, 2, 5, 5] per the docstring example."""
    from solution import get_factors
    result = get_factors(100)
    assert isinstance(result, list)
    assert result == [2, 2, 5, 5], f'get_factors(100) returned {result}, expected [2, 2, 5, 5]'

def test_factor_101_matches_docstring():
    """Test that get_factors(101) returns [101] per the docstring example."""
    from solution import get_factors
    result = get_factors(101)
    assert isinstance(result, list)
    assert result == [101], f'get_factors(101) returned {result}, expected [101]'

def test_factor_2_is_prime():
    """Test that get_factors(2) returns [2], since 2 is the smallest prime."""
    from solution import get_factors
    result = get_factors(2)
    assert isinstance(result, list)
    assert result == [2], f'get_factors(2) returned {result}, expected [2]'

def test_factor_6_has_two_factors():
    """Test that get_factors(6) returns [2, 3], not just [2]."""
    from solution import get_factors
    result = get_factors(6)
    assert isinstance(result, list)
    assert result == [2, 3], f'get_factors(6) returned {result}, expected [2, 3]'

def test_factor_8_has_three_factors():
    """Test that get_factors(8) returns [2, 2, 2], not [2, 2]."""
    from solution import get_factors
    result = get_factors(8)
    assert isinstance(result, list)
    assert result == [2, 2, 2], f'get_factors(8) returned {result}, expected [2, 2, 2]'

def test_factor_two_type_and_length():
    """Test that get_factors(2) returns a list of length 1."""
    from solution import get_factors
    result = get_factors(2)
    assert isinstance(result, list), f'get_factors(2) returned {type(result).__name__}, expected list'
    assert len(result) == 1, f'get_factors(2) returned list of length {len(result)}, expected 1'

def test_factor_4_missing_factor():
    """Test that get_factors(4) returns [2, 2], not [2]."""
    from solution import get_factors
    result = get_factors(4)
    assert isinstance(result, list)
    assert result == [2, 2], f'get_factors(4) returned {result}, expected [2, 2]'
