# Accepted by submit_tests; explanations in testgen_report.json.

def test_empty_input():
    """Test that an empty input list returns an empty RPN list."""
    from solution import shunting_yard
    result = shunting_yard([])
    assert result == []
    assert isinstance(result, list)

def test_single_number():
    """Test that a single integer token passes through unchanged."""
    from solution import shunting_yard
    result = shunting_yard([42])
    assert result == [42]
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] == 42

def test_simple_subtraction():
    """Test basic left-to-right subtraction from docstring example."""
    from solution import shunting_yard
    result = shunting_yard([10, '-', 5, '-', 2])
    assert result == [10, 5, '-', 2, '-']
    assert isinstance(result, list)
    assert len(result) == 5

def test_mixed_precedence():
    """Test that higher-precedence operators bind tighter than lower ones."""
    from solution import shunting_yard
    result = shunting_yard([34, '-', 12, '/', 5])
    assert result == [34, 12, 5, '/', '-']
    assert isinstance(result, list)
    assert len(result) == 5

def test_complex_expression():
    """Test multi-operator expression with mixed precedences from docstring."""
    from solution import shunting_yard
    result = shunting_yard([4, '+', 9, '*', 9, '-', 10, '+', 13])
    assert result == [4, 9, 9, '*', '+', 10, '-', 13, '+']
    assert isinstance(result, list)
    assert len(result) == 9

def test_left_to_right_associativity():
    """Test that equal-precedence operators are evaluated left-to-right."""
    from solution import shunting_yard
    result = shunting_yard([1, '+', 2, '+', 3])
    assert result == [1, 2, '+', 3, '+']
    assert isinstance(result, list)
    assert result[2] == '+'
    assert result[4] == '+'
