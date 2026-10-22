# Accepted by submit_tests; explanations in testgen_report.json.

def test_empty_for_one():
    from solution import get_factors
    assert get_factors(1) == []

def test_prime_returns_single():
    from solution import get_factors
    for p in [2, 3, 7, 13, 97]:
        assert get_factors(p) == [p]

def test_factors_product_equals_n():
    from solution import get_factors

    def prod(lst):
        r = 1
        for x in lst:
            r *= x
        return r
    for n in [4, 6, 12, 30, 60, 100, 256]:
        factors = get_factors(n)
        if n == 1:
            assert factors == []
        else:
            assert prod(factors) == n

def test_known_factorizations():
    from solution import get_factors
    expected = {1: [], 2: [2], 4: [2, 2], 8: [2, 2, 2], 16: [2, 2, 2, 2], 100: [2, 2, 5, 5], 101: [101], 210: [2, 3, 5, 7], 720: [2, 2, 2, 2, 3, 3, 5], 997: [997]}
    for n, exp in expected.items():
        assert get_factors(n) == exp, f'get_factors({n}) = {get_factors(n)}, expected {exp}'

def test_odd_prime_powers():
    from solution import get_factors
    assert get_factors(27) == [3, 3, 3]
    assert get_factors(125) == [5, 5, 5]
    assert get_factors(343) == [7, 7, 7]

def test_larger_prime():
    from solution import get_factors
    assert get_factors(1009) == [1009]

def test_mixed_factors():
    from solution import get_factors
    assert get_factors(36) == [2, 2, 3, 3]
    assert get_factors(48) == [2, 2, 2, 2, 3]
    assert get_factors(84) == [2, 2, 3, 7]

def test_semicube():
    from solution import get_factors
    assert get_factors(216) == [2, 2, 2, 3, 3, 3]

def test_power_of_three():
    from solution import get_factors
    assert get_factors(81) == [3, 3, 3, 3]

def test_product_five_distinct_primes():
    from solution import get_factors
    assert get_factors(2310) == [2, 3, 5, 7, 11]
