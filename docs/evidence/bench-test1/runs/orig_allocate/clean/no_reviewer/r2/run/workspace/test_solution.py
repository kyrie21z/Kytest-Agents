# Accepted by submit_tests; explanations in testgen_report.json.

def test_p2_remainder_largest_fractional():
    """P2: Remainder distributed to entry with strictly largest fractional part."""
    from solution import allocate
    result = allocate(10, [1, 2, 3])
    assert result == [2, 3, 5]
    assert sum(result) == 10
    assert isinstance(result, list) and len(result) == 3

def test_p5_negative_total():
    """P5: Negative total raises ValueError."""
    from solution import allocate
    import pytest
    with pytest.raises(ValueError):
        allocate(-5, [1, 2])

def test_p1_exact_division():
    """P1: Exact division with no remainder; zero-weight entries receive 0."""
    from solution import allocate
    result = allocate(10, [3, 0, 7])
    assert result == [3, 0, 7]
    assert isinstance(result, list)
    assert len(result) == 3
    assert all((isinstance(x, int) for x in result))

def test_p3_total_zero():
    """P3: Total is zero; all shares must be zero."""
    from solution import allocate
    result = allocate(0, [5, 5])
    assert result == [0, 0]
    assert sum(result) == 0
    assert all((x == 0 for x in result))

def test_p4_single_entry():
    """P4: Single weight entry consumes entire total."""
    from solution import allocate
    result = allocate(42, [1])
    assert result == [42]
    assert isinstance(result, list) and len(result) == 1
    assert result[0] == 42

def test_p6_empty_weights():
    """P6: Empty weights list raises ValueError."""
    from solution import allocate
    import pytest
    with pytest.raises(ValueError):
        allocate(10, [])

def test_p7_all_weights_zero():
    """P7: All weights zero raises ValueError."""
    from solution import allocate
    import pytest
    with pytest.raises(ValueError):
        allocate(10, [0, 0, 0])

def test_p8_sum_equals_total():
    """P8: Sum of returned shares always equals total."""
    from solution import allocate
    result = allocate(100, [1, 2, 3, 4, 5])
    assert sum(result) == 100
    assert len(result) == 5
    assert all((isinstance(x, int) for x in result))

def test_p9_zero_weight_positions():
    """P9: Zero-weight positions never receive allocated units."""
    from solution import allocate
    result = allocate(50, [10, 0, 20, 0, 10])
    assert result[1] == 0
    assert result[3] == 0
    assert sum(result) == 50
    assert isinstance(result, list) and len(result) == 5

def test_p10_tie_breaking_lower_index():
    """P10: Tie-breaking favors lower index when fractional remainders are equal."""
    from solution import allocate
    result = allocate(100, [1, 1, 1])
    assert result == [34, 33, 33]
    assert sum(result) == 100
    assert isinstance(result, list) and len(result) == 3

def test_p11_multiple_leftover_units():
    """P11: Multiple leftover units distributed sequentially with tie-breaking."""
    from solution import allocate
    result = allocate(10, [1, 1, 1, 1])
    assert result == [3, 3, 2, 2]
    assert sum(result) == 10
    assert isinstance(result, list) and len(result) == 4
