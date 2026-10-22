# Accepted by submit_tests; explanations in testgen_report.json.

from solution import shunting_yard as _case0_shunting_yard

def test_basic_addition():
    """Test simple two-number addition."""
    result = _case0_shunting_yard([1, '+', 2])
    assert result == [1, 2, '+']

from solution import shunting_yard as _case1_shunting_yard

def test_multiplication_precedence():
    """Test that multiplication binds tighter than addition."""
    result = _case1_shunting_yard([1, '+', 2, '*', 3])
    assert result == [1, 2, 3, '*', '+']

from solution import shunting_yard as _case2_shunting_yard

def test_empty_input():
    """Test that empty input returns empty output."""
    result = _case2_shunting_yard([])
    assert result == []
    assert isinstance(result, list)

from solution import shunting_yard as _case3_shunting_yard

def test_single_operand():
    """Test a single integer with no operators."""
    result = _case3_shunting_yard([42])
    assert result == [42]
    assert isinstance(result, list)

from solution import shunting_yard as _case4_shunting_yard

def test_division_and_multiplication():
    """Test left-associative chain of same-precedence operators (* and /)."""
    result = _case4_shunting_yard([8, '/', 2, '*', 4])
    assert result == [8, 2, '/', 4, '*']

from solution import shunting_yard as _case5_shunting_yard

def test_left_associativity():
    """Test left-to-right associativity for same-precedence operators."""
    result = _case5_shunting_yard([10, '-', 5, '-', 2])
    assert result == [10, 5, '-', 2, '-']
