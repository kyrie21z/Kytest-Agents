# Accepted by submit_tests; explanations in testgen_report.json.

def test_empty_input():
    """Verify that an empty token list returns an empty RPN list."""
    from solution import shunting_yard
    result = shunting_yard([])
    assert result == []
    assert isinstance(result, list)

def test_single_number():
    """A lone integer should pass through unchanged."""
    from solution import shunting_yard
    result = shunting_yard([42])
    assert result == [42]
    assert isinstance(result, list)

def test_left_associativity_same_precedence():
    """Same-precedence operators must be left-associative.
    '10 - 5 - 2' => [10, 5, '-', 2, '-'] per docstring."""
    from solution import shunting_yard
    result = shunting_yard([10, '-', 5, '-', 2])
    assert result == [10, 5, '-', 2, '-']

def test_precedence_multiplication_over_addition():
    """Higher-precedence '*' stays on stack past '+'.
    '2 + 3 * 4' => [2, 3, 4, '*', '+]."""
    from solution import shunting_yard
    result = shunting_yard([2, '+', 3, '*', 4])
    assert result == [2, 3, 4, '*', '+']

def test_division_and_subtraction_ordering():
    """From docstring: '34 - 12 / 5' => [34, 12, 5, '/', '-']."""
    from solution import shunting_yard
    result = shunting_yard([34, '-', 12, '/', 5])
    assert result == [34, 12, 5, '/', '-']

def test_complex_docstring_example():
    """Third docstring example with mixed operators."""
    from solution import shunting_yard
    result = shunting_yard([4, '+', 9, '*', 9, '-', 10, '+', 13])
    assert result == [4, 9, 9, '*', '+', 10, '-', 13, '+']

def test_consecutive_same_precedence_ops():
    """Multiple same-precedence ops in sequence: '1 + 2 + 3 + 4'."""
    from solution import shunting_yard
    result = shunting_yard([1, '+', 2, '+', 3, '+', 4])
    assert result == [1, 2, '+', 3, '+', 4, '+']

def test_higher_then_lower_precedence_drain():
    """'1 * 2 + 3' => higher prec * processed first during drain."""
    from solution import shunting_yard
    result = shunting_yard([1, '*', 2, '+', 3])
    assert result == [1, 2, '*', 3, '+']
