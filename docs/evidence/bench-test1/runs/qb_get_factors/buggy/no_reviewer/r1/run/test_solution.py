# Accepted by submit_tests; explanations in testgen_report.json.

from solution import get_factors as _case0_get_factors

def test_p1_empty_list():
    """Returns an empty list for the minimum valid input n=1."""
    result = _case0_get_factors(1)
    assert result == []
    assert isinstance(result, list)
