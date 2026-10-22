# Accepted by submit_tests; explanations in testgen_report.json.

def test_p1_repeated_factors():
    """Factor a composite number with repeated prime factors."""
    from solution import get_factors
    result = get_factors(100)
    assert result == [2, 2, 5, 5]

def test_p2_distinct_factors():
    """Factor a composite number with distinct prime factors."""
    from solution import get_factors
    result = get_factors(30)
    assert result == [2, 3, 5]

def test_p5_power_of_prime():
    """Factor a power of a single prime."""
    from solution import get_factors
    result = get_factors(8)
    assert result == [2, 2, 2]

def test_p3_smallest_prime():
    """Factor the smallest prime number."""
    from solution import get_factors
    result = get_factors(2)
    assert result == [2]

def test_p4_unit_value():
    """Factor the unit value."""
    from solution import get_factors
    result = get_factors(1)
    assert result == []

def test_p8_large_prime():
    """Factor a large prime number."""
    from solution import get_factors
    result = get_factors(101)
    assert result == [101]

def test_extra_sorted_order():
    """Verify output is in sorted (non-decreasing) order."""
    from solution import get_factors
    result = get_factors(60)
    assert result == [2, 2, 3, 5]
    for i in range(len(result) - 1):
        assert result[i] <= result[i + 1], 'Factors are not in sorted order'

def test_extra_square_of_prime():
    """Factor the square of a larger prime."""
    from solution import get_factors
    result = get_factors(121)
    assert result == [11, 11]

def test_p7_all_prime():
    """Verify all output elements are prime numbers."""
    from solution import get_factors
    result = get_factors(49)
    assert result == [7, 7]

def test_extra_product_property_60():
    """Verify correct factorization for n=60."""
    from solution import get_factors
    result = get_factors(60)
    assert result == [2, 2, 3, 5]
