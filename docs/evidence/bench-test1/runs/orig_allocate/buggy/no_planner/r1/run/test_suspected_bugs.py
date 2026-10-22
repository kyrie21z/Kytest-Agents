# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

def test_tie_breaking_lower_index():
    """Verify exact output for tie-breaking: allocate(10, [1, 1, 1]) == [4, 3, 3]."""
    from solution import allocate
    result = allocate(10, [1, 1, 1])
    assert result == [4, 3, 3], f"Expected [4, 3, 3] but got {result}"
    assert isinstance(result, list)
    assert len(result) == 3
    assert all(isinstance(x, int) for x in result)

def test_zero_weight_with_leftover():
    """Verify zero-weight entries stay 0 even when leftovers exist: allocate(11, [0, 5, 5]) == [0, 6, 5]."""
    from solution import allocate
    result = allocate(11, [0, 5, 5])
    assert result == [0, 6, 5], f"Expected [0, 6, 5] but got {result}"
    assert isinstance(result, list)
    assert len(result) == 3
    assert all(isinstance(x, int) for x in result)
    assert result[0] == 0, "Zero-weight entry must receive 0"
