# Accepted by submit_tests; explanations in testgen_report.json.

def test_sorted_with_repetition():
    """Factors are returned in non-decreasing order, including repeats."""
    from solution import get_factors
    assert get_factors(100) == [2, 2, 5, 5]
    assert get_factors(60) == [2, 2, 3, 5]
    assert get_factors(8) == [2, 2, 2]

def test_power_of_two():
    """Powers of two decompose into repeated 2s."""
    from solution import get_factors
    assert get_factors(2) == [2]
    assert get_factors(4) == [2, 2]
    assert get_factors(16) == [2, 2, 2, 2]
    assert get_factors(1024) == [2] * 10

def test_product_of_distinct_primes():
    """Product of distinct primes returns each once, sorted."""
    from solution import get_factors
    assert get_factors(6) == [2, 3]
    assert get_factors(30) == [2, 3, 5]
    assert get_factors(210) == [2, 3, 5, 7]

def test_one_returns_empty():
    """get_factors(1) returns [] because 1 has no prime factors."""
    from solution import get_factors
    assert get_factors(1) == []

def test_large_prime():
    """A large prime number returns itself as the only factor."""
    from solution import get_factors
    assert get_factors(997) == [997]

def test_factors_multiply_small_range():
    """For n in [2, 50], the product of returned factors equals n."""
    from solution import get_factors

    def prod(lst):
        r = 1
        for x in lst:
            r *= x
        return r
    for n in range(2, 51):
        factors = get_factors(n)
        assert prod(factors) == n, f'product mismatch for {n}'

def test_perfect_cube():
    """Perfect cubes decompose correctly into repeated prime factors."""
    from solution import get_factors
    assert get_factors(8) == [2, 2, 2]
    assert get_factors(27) == [3, 3, 3]
    assert get_factors(64) == [2, 2, 2, 2, 2, 2]
