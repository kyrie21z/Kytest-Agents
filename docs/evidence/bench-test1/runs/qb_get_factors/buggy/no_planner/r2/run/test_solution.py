# Accepted by submit_tests; explanations in testgen_report.json.

from solution import get_factors as _case0_get_factors

def test_get_factors_one():
    """Contract: get_factors(1) returns []"""
    result = _case0_get_factors(1)
    assert result == []
    assert isinstance(result, list)
