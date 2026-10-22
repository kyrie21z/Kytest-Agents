# Accepted by submit_tests; explanations in testgen_report.json.

def test_get_factors_small_composite():
    from solution import get_factors
    result = get_factors(4)
    assert result == [2, 2]
    assert isinstance(result, list)

def test_get_factors_product_two_primes():
    from solution import get_factors
    result = get_factors(6)
    assert result == [2, 3]
    assert isinstance(result, list)

def test_get_factors_power_of_two():
    from solution import get_factors
    result = get_factors(32)
    assert result == [2, 2, 2, 2, 2]
    assert isinstance(result, list)

def test_get_factors_one():
    from solution import get_factors
    result = get_factors(1)
    assert result == []
    assert isinstance(result, list)

def test_get_factors_prime():
    from solution import get_factors
    result = get_factors(101)
    assert result == [101]
    assert isinstance(result, list)

def test_get_factors_composite_repeated():
    from solution import get_factors
    result = get_factors(100)
    assert result == [2, 2, 5, 5]
    assert isinstance(result, list)
