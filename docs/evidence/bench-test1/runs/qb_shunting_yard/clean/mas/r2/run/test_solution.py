# Accepted by submit_tests; explanations in testgen_report.json.

from solution import shunting_yard as _case0_shunting_yard

def test_p1_empty_list():
    result = _case0_shunting_yard([])
    assert result == []

from solution import shunting_yard as _case1_shunting_yard

def test_p2_single_operand():
    result = _case1_shunting_yard([42])
    assert result == [42]

from solution import shunting_yard as _case2_shunting_yard

def test_p3_two_operands_one_operator():
    result = _case2_shunting_yard([1, '+', 2])
    assert result == [1, 2, '+']

from solution import shunting_yard as _case3_shunting_yard

def test_p4_left_associativity():
    result = _case3_shunting_yard([10, '-', 5, '-', 2])
    assert result == [10, 5, '-', 2, '-']

from solution import shunting_yard as _case4_shunting_yard

def test_p5_precedence_division_over_subtraction():
    result = _case4_shunting_yard([34, '-', 12, '/', 5])
    assert result == [34, 12, 5, '/', '-']

from solution import shunting_yard as _case5_shunting_yard

def test_p6_mixed_precedence_and_associativity():
    result = _case5_shunting_yard([4, '+', 9, '*', 9, '-', 10, '+', 13])
    assert result == [4, 9, 9, '*', '+', 10, '-', 13, '+']

from solution import shunting_yard as _case6_shunting_yard

def test_p7_division_before_subtraction():
    result = _case6_shunting_yard([10, '/', 2, '-', 3])
    assert result == [10, 2, '/', 3, '-']

from solution import shunting_yard as _case7_shunting_yard

def test_p8_multiplication_before_addition():
    result = _case7_shunting_yard([2, '+', 3, '*', 4])
    assert result == [2, 3, 4, '*', '+']
