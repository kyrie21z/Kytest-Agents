# Accepted by submit_tests; explanations in testgen_report.json.

from solution import get_factors as _case0_get_factors

def test_one():
    """Test that n=1 returns an empty list."""
    result = _case0_get_factors(1)
    assert result == []

from solution import get_factors as _case1_get_factors

def test_result_is_list():
    """Test that the return value is always a list."""
    for n in [1, 2, 6, 12, 100]:
        result = _case1_get_factors(n)
        assert isinstance(result, list)

from solution import get_factors as _case2_get_factors

def test_product_of_factors_le_n():
    """Test that the product of returned factors does not exceed n."""
    import math
    for n in [1, 6, 12, 100, 49, 30, 8, 15]:
        result = _case2_get_factors(n)
        if result:
            product = math.prod(result)
            assert product <= n
