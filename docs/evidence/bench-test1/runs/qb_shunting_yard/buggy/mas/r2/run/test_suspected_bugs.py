# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

from solution import shunting_yard
def test_p1_simple_left_associative_subtraction():
    result = shunting_yard([10, '-', 5, '-', 2])
    assert result == [10, 5, '-', 2, '-']

from solution import shunting_yard
def test_p2_mixed_precedence_division_over_subtraction():
    result = shunting_yard([34, '-', 12, '/', 5])
    assert result == [34, 12, 5, '/', '-']

from solution import shunting_yard
def test_p3_complex_interleaved_operators():
    result = shunting_yard([4, '+', 9, '*', 9, '-', 10, '+', 13])
    assert result == [4, 9, 9, '*', '+', 10, '-', 13, '+']

from solution import shunting_yard
def test_p5_simplest_non_trivial_infix():
    result = shunting_yard([3, '+', 7])
    assert result == [3, 7, '+']

from solution import shunting_yard

def test_p1_left_assoc_subtraction():
    """P1: Converts a simple left-associative subtraction chain to RPN."""
    result = shunting_yard([10, '-', 5, '-', 2])
    assert result == [10, 5, '-', 2, '-']

from solution import shunting_yard

def test_p2_division_over_subtraction():
    """P2: Handles mixed operator precedence (division over subtraction)."""
    result = shunting_yard([34, '-', 12, '/', 5])
    assert result == [34, 12, 5, '/', '-']

from solution import shunting_yard

def test_p3_complex_interleaved():
    """P3: Processes a complex expression with interleaved addition, multiplication, and subtraction."""
    result = shunting_yard([4, '+', 9, '*', 9, '-', 10, '+', 13])
    assert result == [4, 9, 9, '*', '+', 10, '-', 13, '+']

from solution import shunting_yard

def test_p5_simplest_infix():
    """P5: Converts the simplest non-trivial infix expression."""
    result = shunting_yard([3, '+', 7])
    assert result == [3, 7, '+']

from solution import shunting_yard

def test_p7_token_preservation():
    """P7: Preserves all original tokens (multiset equality)."""
    tokens = [1, '+', 2, '*', 3, '-', 4]
    result = shunting_yard(tokens)
    # Convert all to strings for safe sorting of mixed int/str types
    assert sorted((str(t) for t in result)) == sorted((str(t) for t in tokens))

from solution import shunting_yard

def test_p8_precedence_multiplication_before_addition():
    """P8: Enforces standard mathematical precedence (multiplication before addition)."""
    result = shunting_yard([5, '+', 6, '*', 2])
    assert result == [5, 6, 2, '*', '+']
