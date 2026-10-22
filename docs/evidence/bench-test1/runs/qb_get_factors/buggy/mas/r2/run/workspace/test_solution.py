# Accepted by submit_tests; explanations in testgen_report.json.

from solution import get_factors as _case0_get_factors

def test_p3_empty_list():
    """Handle the lowest valid input which yields no factors.

    Contract quote: 'A list of the prime factors of n in sorted order with repetition'
    Input domain: n = 1 (precondition boundary, n >= 1)
    Oracle: By mathematical definition, 1 has no prime factors; output must be [].
    Fault hypothesis: An implementation might return [1] or raise an error for n=1.
    """
    result = _case0_get_factors(1)
    assert result == []
    assert isinstance(result, list)
