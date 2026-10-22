# Accepted by submit_tests; explanations in testgen_report.json.

from solution import get_factors as _case0_get_factors

def test_get_factors_one():
    """Test that get_factors(1) returns empty list per precondition."""
    result = _case0_get_factors(1)
    assert result == []
    assert isinstance(result, list)

from solution import get_factors as _case1_get_factors

def test_get_factors_returns_list_type():
    """Verify return type is always a list for valid inputs."""
    for n in [1, 2, 4, 6, 8, 10, 100]:
        result = _case1_get_factors(n)
        assert isinstance(result, list), f'get_factors({n}) did not return a list'

from solution import get_factors as _case2_get_factors

def test_get_factors_empty_for_n1():
    """Test get_factors(1) returns empty list per docstring."""
    result = _case2_get_factors(1)
    assert result == []
    assert isinstance(result, list)

from solution import get_factors as _case3_get_factors

def test_get_factors_returns_list_always():
    """Verify return type is always a list for valid inputs."""
    for n in [1, 2, 4, 6, 8, 10, 100]:
        result = _case3_get_factors(n)
        assert isinstance(result, list), f'get_factors({n}) did not return a list'
