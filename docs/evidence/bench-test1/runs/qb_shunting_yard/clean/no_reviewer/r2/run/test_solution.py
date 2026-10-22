# Accepted by submit_tests; explanations in testgen_report.json.

from solution import shunting_yard as _case0_shunting_yard

def test_p1_basic_subtraction():
    """P1: single subtraction between two operands."""
    result = _case0_shunting_yard([10, '-', 5])
    assert result == [10, 5, '-']

from solution import shunting_yard as _case1_shunting_yard

def test_p2_precedence_mul_over_add():
    """P2: '*' (prec 2) stays on stack above '+' (prec 1)."""
    result = _case1_shunting_yard([4, '+', 9, '*', 2])
    assert result == [4, 9, 2, '*', '+']

from solution import shunting_yard as _case2_shunting_yard

def test_p3_left_associativity():
    """P3: equal-precedence '+' operators are left-associative."""
    result = _case2_shunting_yard([1, '+', 2, '+', 3])
    assert result == [1, 2, '+', 3, '+']

from solution import shunting_yard as _case3_shunting_yard

def test_p4_single_operand():
    """P4: a lone integer passes through unchanged."""
    result = _case3_shunting_yard([42])
    assert result == [42]
    assert type(result) is list

from solution import shunting_yard as _case4_shunting_yard

def test_p5_empty_input():
    """P5: empty list returns empty list."""
    result = _case4_shunting_yard([])
    assert result == []
    assert type(result) is list

from solution import shunting_yard as _case5_shunting_yard

def test_p6_mixed_chain():
    """P6: '*' fires before '+' and '-' due to higher precedence."""
    result = _case5_shunting_yard([2, '*', 3, '+', 4, '-', 5])
    assert result == [2, 3, '*', 4, '+', 5, '-']

from solution import shunting_yard as _case6_shunting_yard

def test_p7_div_then_mul():
    """P7: '/' and '*' have equal precedence → left-associative."""
    result = _case6_shunting_yard([10, '/', 2, '*', 3])
    assert result == [10, 2, '/', 3, '*']

from solution import shunting_yard as _case7_shunting_yard

def test_extra_return_type():
    """Ensure the return value is always a list for various inputs."""
    for inp in [[1], [1, '+', 2], [], [1, '+', 2, '*', 3]]:
        r = _case7_shunting_yard(inp)
        assert isinstance(r, list), f'Expected list, got {type(r)}'

from solution import shunting_yard as _case8_shunting_yard

def test_extra_docstring_example_1():
    """Verify Example 1 from the docstring: [10, '-', 5, '-', 2]."""
    result = _case8_shunting_yard([10, '-', 5, '-', 2])
    assert result == [10, 5, '-', 2, '-']

from solution import shunting_yard as _case9_shunting_yard

def test_extra_docstring_example_2():
    """Verify Example 2 from the docstring: [34, '-', 12, '/', 5]."""
    result = _case9_shunting_yard([34, '-', 12, '/', 5])
    assert result == [34, 12, 5, '/', '-']
