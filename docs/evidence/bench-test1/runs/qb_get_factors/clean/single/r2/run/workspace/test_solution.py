# Accepted by submit_tests; explanations in testgen_report.json.

def test_get_factors_prime():
    from solution import get_factors
    result = get_factors(2)
    assert isinstance(result, list)
    assert result == [2], 'get_factors(2) should return [2]'

def test_get_factors_power_of_two():
    from solution import get_factors
    result = get_factors(1024)
    assert isinstance(result, list)
    assert result == [2] * 10, 'get_factors(1024) should return ten 2s'
    assert len(result) == 10, 'should have exactly 10 factors'

def test_get_factors_one():
    from solution import get_factors
    result = get_factors(1)
    assert isinstance(result, list), 'return value must be a list'
    assert result == [], 'get_factors(1) should return empty list per docstring example'

def test_get_factors_100_docstring_example():
    from solution import get_factors
    result = get_factors(100)
    assert isinstance(result, list)
    assert result == [2, 2, 5, 5], 'get_factors(100) must match docstring example exactly'

def test_get_factors_101_prime_docstring():
    from solution import get_factors
    result = get_factors(101)
    assert isinstance(result, list)
    assert result == [101], 'get_factors(101) must match docstring example exactly'

def test_get_factors_two_is_prime():
    from solution import get_factors
    result = get_factors(2)
    assert isinstance(result, list)
    assert result == [2], 'get_factors(2) should return [2] since 2 is prime'

def test_get_factors_powers_of_two():
    from solution import get_factors
    for exp in range(1, 11):
        n = 2 ** exp
        result = get_factors(n)
        assert isinstance(result, list)
        assert result == [2] * exp, f'get_factors({n}) should return {exp} copies of 2'

def test_get_factors_returns_list_type():
    from solution import get_factors
    result = get_factors(6)
    assert isinstance(result, list), f'get_factors(6) must return a list, got {type(result)}'
    assert result == [2, 3], 'get_factors(6) must return [2, 3] since 6 = 2*3'

def test_get_factors_large_prime():
    from solution import get_factors
    result = get_factors(997)
    assert isinstance(result, list)
    assert result == [997], 'get_factors(997) should return [997] since 997 is prime'

def test_get_factors_product_invariant():
    from solution import get_factors
    test_cases = {1: [], 2: [2], 4: [2, 2], 6: [2, 3], 12: [2, 2, 3], 30: [2, 3, 5], 60: [2, 2, 3, 5]}
    for n, expected in test_cases.items():
        result = get_factors(n)
        assert result == expected, f'get_factors({n}) should return {expected}, got {result}'
