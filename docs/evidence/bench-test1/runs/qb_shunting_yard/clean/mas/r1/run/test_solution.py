# Accepted by submit_tests; explanations in testgen_report.json.

# Accepted by submit_tests; explanations in testgen_report.json.

from solution import shunting_yard as _case0_shunting_yard

def test_p1_chain_subtraction():
    result = _case0_shunting_yard([10, '-', 5, '-', 2])
    assert result == [10, 5, '-', 2, '-']

from solution import shunting_yard as _case1_shunting_yard

def test_p2_mixed_sub_div():
    result = _case1_shunting_yard([34, '-', 12, '/', 5])
    assert result == [34, 12, 5, '/', '-']

from solution import shunting_yard as _case2_shunting_yard

def test_p3_complex_expression():
    result = _case2_shunting_yard([4, '+', 9, '*', 9, '-', 10, '+', 13])
    assert result == [4, 9, 9, '*', '+', 10, '-', 13, '+']

from solution import shunting_yard as _case3_shunting_yard

def test_p4_single_operand():
    result = _case3_shunting_yard([42])
    assert result == [42]

from solution import shunting_yard as _case4_shunting_yard

def test_p5_empty_list():
    result = _case4_shunting_yard([])
    assert result == []

from solution import shunting_yard as _case5_shunting_yard

def test_p6_precedence_star_plus():
    result = _case5_shunting_yard([2, '*', 3, '+', 4])
    assert result == [2, 3, '*', 4, '+']

from solution import shunting_yard as _case6_shunting_yard

def test_p7_left_associative_division():
    result = _case6_shunting_yard([10, '/', 2, '/', 5])
    assert result == [10, 2, '/', 5, '/']

from solution import shunting_yard as _case7_shunting_yard

def test_p8_left_associative_addition():
    result = _case7_shunting_yard([1, '+', 2, '+', 3])
    assert result == [1, 2, '+', 3, '+']

from solution import shunting_yard as _case8_shunting_yard

def test_extra_multiply_chain():
    result = _case8_shunting_yard([8, '*', 2, '*', 3])
    assert result == [8, 2, '*', 3, '*']

from solution import shunting_yard as _case9_shunting_yard

def test_extra_higher_prec_then_lower():
    result = _case9_shunting_yard([1, '+', 2, '*', 3])
    assert result == [1, 2, 3, '*', '+']

from solution import shunting_yard as _case10_shunting_yard

def test_extra_return_type_list():
    result = _case10_shunting_yard([1, '+', 2])
    assert isinstance(result, list)


from solution import shunting_yard as _newab53f3b40__case11_shunting_yard

def test_extra_preserves_all_tokens():
    """Verify that every token in the output appears exactly as many times as in the input.

    Contract quote: 'The input tokens reordered into Reverse Polish Notation'
    Input domain: any valid infix expression list satisfying the precondition.
    Oracle: multiset equality — the output must be a permutation of the input.
    Fault hypothesis: a buggy implementation could drop an operator, duplicate a number,
      or otherwise change the token multiset while still producing a syntactically valid RPN.
    """

    def _count(lst):
        d = {}
        for x in lst:
            d[x] = d.get(x, 0) + 1
        return d
    result = _newab53f3b40__case11_shunting_yard([10, '-', 5, '-', 2])
    assert _count(result) == _count([10, '-', 5, '-', 2])
    result2 = _newab53f3b40__case11_shunting_yard([34, '-', 12, '/', 5])
    assert _count(result2) == _count([34, '-', 12, '/', 5])
    result3 = _newab53f3b40__case11_shunting_yard([4, '+', 9, '*', 9, '-', 10, '+', 13])
    assert _count(result3) == _count([4, '+', 9, '*', 9, '-', 10, '+', 13])
    result4 = _newab53f3b40__case11_shunting_yard([42])
    assert _count(result4) == _count([42])
    result5 = _newab53f3b40__case11_shunting_yard([])
    assert _count(result5) == _count([])
