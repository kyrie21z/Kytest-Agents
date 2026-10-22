# Accepted by submit_tests; explanations in testgen_report.json.

from solution import shunting_yard as _case0_shunting_yard

def test_empty_input():
    """Test empty input — precondition holds vacuously."""
    result = _case0_shunting_yard([])
    assert result == []
    assert isinstance(result, list)

from solution import shunting_yard as _case1_shunting_yard

def test_single_operand():
    """Test a single integer with no operators."""
    result = _case1_shunting_yard([42])
    assert result == [42]
    assert isinstance(result, list)
    assert len(result) == 1

from solution import shunting_yard as _case2_shunting_yard

def test_return_type_is_list():
    """Verify the return value is always a list per the contract."""
    result = _case2_shunting_yard([1, '+', 2])
    assert isinstance(result, list)
    result2 = _case2_shunting_yard([1, '+', 2, '*', 3])
    assert isinstance(result2, list)

from solution import shunting_yard as _case3_shunting_yard

def test_operands_preserved_in_order():
    """All integer operands should appear in the output in their original infix order."""
    tokens = [5, '+', 3, '-', 8, '*', 2]
    result = _case3_shunting_yard(tokens)
    operands_out = [t for t in result if isinstance(t, int)]
    operands_in = [t for t in tokens if isinstance(t, int)]
    assert operands_out == operands_in, f'Operands out {operands_out} != operands in {operands_in}'

from solution import shunting_yard as _case4_shunting_yard

def test_zero_operand():
    """Test that zero (an int) is handled correctly as an operand."""
    result = _case4_shunting_yard([0, '+', 0])
    assert 0 in result
    assert result.count(0) == 2
    assert isinstance(result, list)

from solution import shunting_yard as _case5_shunting_yard

def test_large_integer_operand():
    """Test that large integer values are preserved without modification."""
    result = _case5_shunting_yard([999999999, '+', 1])
    assert 999999999 in result
    assert 1 in result
    assert isinstance(result, list)

from solution import shunting_yard as _case6_shunting_yard

def test_negative_operand():
    """Test that negative integers are handled as valid operands."""
    result = _case6_shunting_yard([-5, '+', 3])
    assert -5 in result
    assert 3 in result
    assert isinstance(result, list)

from solution import shunting_yard as _case7_shunting_yard

def test_return_type_consistency():
    """Return type must be consistently list across all valid inputs."""
    samples = [[], [42], [1, '+', 2], [1, '+', 2, '*', 3], [1, '+', 2, '-', 3, '*', 4, '/', 5]]
    for tokens in samples:
        result = _case7_shunting_yard(tokens)
        assert isinstance(result, list), f'Expected list for input {tokens}, got {type(result)}'

from solution import shunting_yard as _case8_shunting_yard

def test_operands_in_original_order():
    """Integer operands must appear in the same left-to-right order as input."""
    tokens = [7, '+', 3, '-', 9, '*', 1]
    result = _case8_shunting_yard(tokens)
    operands_out = [t for t in result if isinstance(t, int)]
    operands_in = [t for t in tokens if isinstance(t, int)]
    assert operands_out == operands_in, f'Order changed: {operands_in} -> {operands_out}'

from solution import shunting_yard as _case9_shunting_yard

def test_negative_operand_preserved():
    """Negative integers must be preserved as-is in the output."""
    result = _case9_shunting_yard([-5, '+', -3])
    assert -5 in result
    assert -3 in result
    nums = [t for t in result if isinstance(t, int)]
    assert nums == [-5, -3], f'Negative operands modified: {nums}'

from solution import shunting_yard as _case10_shunting_yard

def test_return_type_is_list_for_all_inputs():
    """Return type must be consistently list across various valid inputs."""
    samples = [[], [42], [1, '+', 2], [1, '+', 2, '*', 3], [1, '+', 2, '-', 3, '*', 4, '/', 5]]
    for tokens in samples:
        result = _case10_shunting_yard(tokens)
        assert isinstance(result, list), f'Expected list for input {tokens}, got {type(result)}'

from solution import shunting_yard as _case11_shunting_yard

def test_deterministic_output():
    """Same input must always produce the same output."""
    tokens = [1, '+', 2, '-', 3]
    results = [_case11_shunting_yard(tokens) for _ in range(10)]
    first = results[0]
    for r in results[1:]:
        assert r == first, f'Non-deterministic: {first} vs {r}'

from solution import shunting_yard as _case12_shunting_yard

def test_many_operands_no_operators():
    """Expression with many operands and no operators should pass through unchanged."""
    tokens = list(range(1, 11))
    result = _case12_shunting_yard(tokens)
    assert result == tokens, f'Expected {tokens}, got {result}'
