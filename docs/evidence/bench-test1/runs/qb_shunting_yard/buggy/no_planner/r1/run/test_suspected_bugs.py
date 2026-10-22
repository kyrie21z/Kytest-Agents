# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

def test_docstring_example_1():
    """Test the first example from the docstring: 10 - 5 - 2."""
    from solution import shunting_yard
    result = shunting_yard([10, '-', 5, '-', 2])
    assert result == [10, 5, '-', 2, '-']

def test_docstring_example_2():
    """Test the second example from the docstring: 34 - 12 / 5."""
    from solution import shunting_yard
    result = shunting_yard([34, '-', 12, '/', 5])
    assert result == [34, 12, 5, '/', '-']

def test_single_operator():
    """Test simplest non-trivial case: 1 + 2."""
    from solution import shunting_yard
    result = shunting_yard([1, '+', 2])
    assert result == [1, 2, '+']

def test_multiplication_precedence():
    """Test precedence: 2 * 3 + 4 — multiplication binds before addition."""
    from solution import shunting_yard
    result = shunting_yard([2, '*', 3, '+', 4])
    assert result == [2, 3, '*', 4, '+']
