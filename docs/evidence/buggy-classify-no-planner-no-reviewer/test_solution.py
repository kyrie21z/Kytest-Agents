# Accepted by submit_tests; explanations in testgen_report.json.

def test_classify_inside_interval():
    """Test that classify returns 0 for values strictly between low and high."""
    from solution import classify
    assert classify(5, 1, 10) == 0
    assert classify(0, -5, 5) == 0
    assert classify(3, 0, 10) == 0

def test_classify_below_low():
    """Test that classify returns -1 for values strictly below low."""
    from solution import classify
    assert classify(0, 1, 10) == -1
    assert classify(-5, 0, 5) == -1
    assert classify(-100, -50, -10) == -1

def test_classify_at_low_boundary():
    """Test that classify returns 0 when value equals low (inclusive on left)."""
    from solution import classify
    assert classify(1, 1, 10) == 0
    assert classify(0, 0, 5) == 0
    assert classify(-5, -5, 0) == 0

def test_classify_at_high_boundary():
    """Test that classify returns 1 when value equals high (exclusive on right)."""
    from solution import classify
    assert classify(10, 1, 10) == 1
    assert classify(5, 0, 5) == 1
    assert classify(0, -5, 0) == 1

def test_classify_empty_interval():
    """Test behavior when low == high (degenerate/empty interval)."""
    from solution import classify
    assert classify(0, 5, 5) == -1
    assert classify(5, 5, 5) == 1
    assert classify(10, 5, 5) == 1

def test_classify_return_type():
    """Test that classify always returns an int (-1, 0, or 1)."""
    from solution import classify
    result = classify(5, 1, 10)
    assert isinstance(result, int)
    assert result in (-1, 0, 1)
    result = classify(0, 1, 10)
    assert isinstance(result, int)
    assert result in (-1, 0, 1)
    result = classify(10, 1, 10)
    assert isinstance(result, int)
    assert result in (-1, 0, 1)
