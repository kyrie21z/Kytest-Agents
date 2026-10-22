# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

def test_p1_simple_chain_subtraction():
    from solution import shunting_yard
    result = shunting_yard([10, '-', 5, '-', 2])
    assert result == [10, 5, '-', 2, '-']

def test_p2_mixed_precedence():
    from solution import shunting_yard
    result = shunting_yard([34, '-', 12, '/', 5])
    assert result == [34, 12, 5, '/', '-']

def test_p3_complex_interleaved():
    from solution import shunting_yard
    result = shunting_yard([4, '+', 9, '*', 9, '-', 10, '+', 13])
    assert result == [4, 9, 9, '*', '+', 10, '-', 13, '+']

def test_p5_minimal_expression():
    from solution import shunting_yard
    result = shunting_yard([3, '+', 7])
    assert result == [3, 7, '+']

def test_p6_left_associativity_multiplication():
    from solution import shunting_yard
    result = shunting_yard([10, '*', 2, '*', 5])
    assert result == [10, 2, '*', 5, '*']

def test_p7_precedence_add_mul():
    from solution import shunting_yard
    result = shunting_yard([2, '+', 3, '*', 4])
    assert result == [2, 3, 4, '*', '+']

def test_p9_multiset_preservation():
    from solution import shunting_yard
    result = shunting_yard([1, '+', 2, '*', 3])
    # Verify the multiset of tokens is preserved
    sorted_input = sorted([1, '+', 2, '*', 3], key=lambda x: (isinstance(x, str), x))
    sorted_output = sorted(result, key=lambda x: (isinstance(x, str), x))
    assert sorted_input == sorted_output

def test_extra_negative_operands():
    from solution import shunting_yard
    result = shunting_yard([-5, '+', -3])
    assert result == [-5, -3, '+']

def test_extra_division_precedence():
    from solution import shunting_yard
    result = shunting_yard([100, '/', 10, '*', 2])
    assert result == [100, 10, 2, '*', '/']

def test_extra_multiple_operators_same_precedence():
    from solution import shunting_yard
    result = shunting_yard([1, '+', 2, '+', 3, '+', 4])
    assert result == [1, 2, '+', 3, '+', 4, '+']

def test_extra_higher_precedence_first():
    from solution import shunting_yard
    result = shunting_yard([5, '*', 3, '+', 2])
    assert result == [5, 3, '*', 2, '+']
