# Accepted by submit_tests; explanations in testgen_report.json.

# Accepted by submit_tests; explanations in testgen_report.json.

from solution import get_factors as _case0_get_factors

def test_p1_highly_composite():
    result = _case0_get_factors(100)
    assert result == [2, 2, 5, 5]

from solution import get_factors as _case1_get_factors

def test_p2_prime_number():
    result = _case1_get_factors(101)
    assert result == [101]

from solution import get_factors as _case2_get_factors

def test_p4_prime_power():
    result = _case2_get_factors(8)
    assert result == [2, 2, 2]

from solution import get_factors as _case3_get_factors

def test_p3_unit_input():
    result = _case3_get_factors(1)
    assert result == []

from solution import get_factors as _case4_get_factors

def test_p5_semiprime():
    result = _case4_get_factors(6)
    assert result == [2, 3]

from solution import get_factors as _case5_get_factors

def test_p6_smallest_prime():
    result = _case5_get_factors(2)
    assert result == [2]


from solution import get_factors as _new569018ec0_get_factors

def test_p7_repeated_factors():
    """P7: Check multiplicative reconstruction and sorting for a composite with repeated factors."""
    result = _new569018ec0_get_factors(12)
    assert result == [2, 2, 3]

from solution import get_factors as _new569018ec1_get_factors

def test_p8_distinct_primes():
    """P8: Check multiplicative reconstruction and sorting for a product of distinct primes."""
    result = _new569018ec1_get_factors(210)
    assert result == [2, 3, 5, 7]
