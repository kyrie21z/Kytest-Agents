# Accepted by submit_tests; explanations in testgen_report.json.

from solution import to_base as _case0_to_base

def test_binary_conversion():
    """Convert decimal 10 to binary: expected '1010'."""
    assert _case0_to_base(10, 2) == '1010'

from solution import to_base as _case1_to_base

def test_large_binary():
    """Convert 1000 to binary: expected '1111101000'."""
    assert _case1_to_base(1000, 2) == '1111101000'

from solution import to_base as _case2_to_base

def test_hex_power_of_two():
    """Convert 1024 to hexadecimal: expected '400'."""
    assert _case2_to_base(1024, 16) == '400'

from solution import to_base as _case3_to_base

def test_docstring_example():
    """Verify the example from the docstring: to_base(31, 16) == '1F'."""
    assert _case3_to_base(31, 16) == '1F'

from solution import to_base as _case4_to_base

def test_single_digit_result():
    """When num < b, result should be a single character."""
    assert _case4_to_base(5, 16) == '5'

from solution import to_base as _case5_to_base

def test_max_base_letter():
    """Convert 35 to base 36: expected 'Z' (the largest single digit in base 36)."""
    assert _case5_to_base(35, 36) == 'Z'
