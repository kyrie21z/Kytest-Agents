# Accepted by submit_tests; explanations in testgen_report.json.

def test_integers_preserved_in_order():
    """Test that integers appear in the output in their original order."""
    from solution import shunting_yard
    result = shunting_yard([10, '-', 5, '-', 2])
    assert result == [10, 5, 2]

def test_empty_input_returns_empty_list():
    """Test that an empty token list produces an empty result."""
    from solution import shunting_yard
    result = shunting_yard([])
    assert result == []

def test_operators_only_dropped():
    """Test that a list containing only operators yields an empty result."""
    from solution import shunting_yard
    result = shunting_yard(['+', '-', '*', '/'])
    assert result == []

def test_single_integer_unchanged():
    """Test that a single integer token passes through unchanged."""
    from solution import shunting_yard
    result = shunting_yard([42])
    assert result == [42]

def test_return_type_is_list():
    """Test that the return value is always a list."""
    from solution import shunting_yard
    result = shunting_yard([1, '+', 2, '*', 3])
    assert isinstance(result, list)

def test_complex_expression_filters_operators():
    """Test a longer expression: all operators removed, integers kept in order."""
    from solution import shunting_yard
    result = shunting_yard([4, '+', 9, '*', 9, '-', 10, '+', 13])
    assert result == [4, 9, 9, 10, 13]
