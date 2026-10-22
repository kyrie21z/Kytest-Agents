# Accepted by submit_tests; explanations in testgen_report.json.

def test_p1_empty_list():
    """P1: Factor the smallest valid input n=1 -> [].

    Contract quote: 'Prime Factorization' and example '>>> get_factors(1) []'.
    Input domain: n = 1, the smallest allowed integer per precondition.
    Oracle: The function should return an empty list because 1 has no prime factors.
    Fault hypothesis: If the implementation does not special-case n == 1, it might
      return [1] or enter an infinite loop or raise an error.
    """
    from solution import get_factors
    result = get_factors(1)
    assert result == []
    assert isinstance(result, list)
