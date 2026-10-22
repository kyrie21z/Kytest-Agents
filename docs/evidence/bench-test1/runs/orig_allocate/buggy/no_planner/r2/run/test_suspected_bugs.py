# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

def test_tie_breaking_lower_index():
    """When multiple entries share the same largest remainder, lower index wins."""
    from solution import allocate
    result = allocate(5, [2, 2, 2])
    assert result == [2, 2, 1]
