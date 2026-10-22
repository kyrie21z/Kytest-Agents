# New tests for solution.py — implements plan items P1–P5, P6–P8.
# These are NOT written directly to test_solution.py; they are submitted via submit_tests.

from solution import shunting_yard


def test_p1_left_assoc_subtraction():
    """P1: Converts a simple left-associative subtraction chain to RPN."""
    result = shunting_yard([10, '-', 5, '-', 2])
    assert result == [10, 5, '-', 2, '-']


def test_p2_division_over_subtraction():
    """P2: Handles mixed operator precedence (division over subtraction)."""
    result = shunting_yard([34, '-', 12, '/', 5])
    assert result == [34, 12, 5, '/', '-']


def test_p3_complex_interleaved():
    """P3: Processes a complex expression with interleaved addition, multiplication, and subtraction."""
    result = shunting_yard([4, '+', 9, '*', 9, '-', 10, '+', 13])
    assert result == [4, 9, 9, '*', '+', 10, '-', 13, '+']


def test_p5_simplest_infix():
    """P5: Converts the simplest non-trivial infix expression."""
    result = shunting_yard([3, '+', 7])
    assert result == [3, 7, '+']


def test_p6_empty_list():
    """P6: Handles an empty input list gracefully."""
    result = shunting_yard([])
    assert result == []


def test_p7_token_preservation():
    """P7: Preserves all original tokens (multiset equality)."""
    tokens = [1, '+', 2, '*', 3, '-', 4]
    result = shunting_yard(tokens)
    assert sorted(result) == sorted(tokens)


def test_p8_precedence_multiplication_before_addition():
    """P8: Enforces standard mathematical precedence (multiplication before addition)."""
    result = shunting_yard([5, '+', 6, '*', 2])
    assert result == [5, 6, 2, '*', '+']
