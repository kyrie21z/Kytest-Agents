# Accepted by submit_tests; explanations in testgen_report.json.

from solution import shunting_yard as _case0_shunting_yard

def test_p1_left_assoc_sub():
    result = _case0_shunting_yard([10, '-', 5, '-', 2])
    assert result == [10, 5, '-', 2, '-']

from solution import shunting_yard as _case1_shunting_yard

def test_p2_mixed_precedence():
    result = _case1_shunting_yard([34, '-', 12, '/', 5])
    assert result == [34, 12, 5, '/', '-']

from solution import shunting_yard as _case2_shunting_yard

def test_p3_complex_grouping():
    result = _case2_shunting_yard([4, '+', 9, '*', 9, '-', 10, '+', 13])
    assert result == [4, 9, 9, '*', '+', 10, '-', 13, '+']

from solution import shunting_yard as _case3_shunting_yard

def test_p4_single_operand():
    result = _case3_shunting_yard([42])
    assert result == [42]

from solution import shunting_yard as _case4_shunting_yard

def test_p5_minimal_binary():
    result = _case4_shunting_yard([7, '+', 3])
    assert result == [7, 3, '+']

from solution import shunting_yard as _case5_shunting_yard

def test_p6_div_prec_add():
    result = _case5_shunting_yard([8, '+', 10, '/', 2])
    assert result == [8, 10, 2, '/', '+']
