# Accepted by submit_tests; explanations in testgen_report.json.

from solution import shunting_yard as _case0_shunting_yard

def test_basic_subtraction():
    """Test basic left-to-right subtraction chain."""
    result = _case0_shunting_yard([10, '-', 5, '-', 2])
    assert result == [10, 5, '-', 2, '-']

from solution import shunting_yard as _case1_shunting_yard

def test_mixed_precedence():
    """Test that higher precedence operators appear earlier in RPN output."""
    result = _case1_shunting_yard([34, '-', 12, '/', 5])
    assert result == [34, 12, 5, '/', '-']

from solution import shunting_yard as _case2_shunting_yard

def test_complex_expression():
    """Test complex expression with multiple operators of varying precedence and associativity."""
    result = _case2_shunting_yard([4, '+', 9, '*', 9, '-', 10, '+', 13])
    assert result == [4, 9, 9, '*', '+', 10, '-', 13, '+']

from solution import shunting_yard as _case3_shunting_yard

def test_empty_input():
    """Test that empty input returns empty output without error."""
    result = _case3_shunting_yard([])
    assert result == []
    assert isinstance(result, list)

from solution import shunting_yard as _case4_shunting_yard

def test_single_number():
    """Test that a single number passes through unchanged."""
    result = _case4_shunting_yard([42])
    assert result == [42]
    assert len(result) == 1

from solution import shunting_yard as _case5_shunting_yard

def test_left_associativity_multiplication():
    """Test that same-precedence operators are left-associative via chained multiplications."""
    result = _case5_shunting_yard([2, '*', 3, '*', 4])
    assert result == [2, 3, '*', 4, '*']
