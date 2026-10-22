# Accepted by submit_tests; explanations in testgen_report.json.

from solution import to_base as _case0_to_base

def test_p1_small_odd_to_binary():
    """Convert a small odd integer to binary.

    Contract quote: "Output: A string representing the value of num in base b."
    Input domain: num = 5 (> 0), b = 2 (valid, 2 <= b <= 36).
    Oracle: 5 decimal = 101 binary by standard positional notation.
    Fault hypothesis: Implementation might produce lowercase '101' or wrong digits.
    """
    result = _case0_to_base(5, 2)
    assert result == '101'
    assert isinstance(result, str)

from solution import to_base as _case1_to_base

def test_p2_same_base_conversion():
    """Convert integer to same base yields identical digit sequence.

    Contract quote: "Output: A string representing the value of num in base b."
    Input domain: num = 123 (> 0), b = 10 (valid, 2 <= b <= 36).
    Oracle: In base 10, the representation of 123 is '123'.
    Fault hypothesis: Off-by-one in division/modulo could corrupt digits.
    """
    result = _case1_to_base(123, 10)
    assert result == '123'
    assert isinstance(result, str)

from solution import to_base as _case2_to_base

def test_p3_minimum_valid_num():
    """Test minimum valid num (precondition: num > 0).

    Contract quote: "Precondition: num > 0, 2 <= b <= 36."
    Input domain: num = 1 (smallest valid positive integer), b = 2.
    Oracle: Any positive integer n < b maps to a single digit; 1 < 2 so result is '1'.
    Fault hypothesis: Loop condition off could return empty string for num=1.
    """
    result = _case2_to_base(1, 2)
    assert result == '1'
    assert isinstance(result, str)

from solution import to_base as _case3_to_base

def test_p4_minimum_valid_base():
    """Test minimum valid base (precondition: 2 <= b <= 36).

    Contract quote: "Precondition: num > 0, 2 <= b <= 36."
    Input domain: num = 10 (> 0), b = 2 (lower bound of valid bases).
    Oracle: 10 decimal = 1010 binary (8 + 2 = 10).
    Fault hypothesis: Incorrect bit extraction at base-2 boundary.
    """
    result = _case3_to_base(10, 2)
    assert result == '1010'
    assert isinstance(result, str)

from solution import to_base as _case4_to_base

def test_p5_maximum_valid_base():
    """Test maximum valid base (precondition: 2 <= b <= 36).

    Contract quote: "Precondition: num > 0, 2 <= b <= 36."
    Input domain: num = 35 (> 0), b = 36 (upper bound of valid bases).
    Oracle: In base 36, values 10-35 map to 'A'-'Z'. Value 35 maps to 'Z'.
    Fault hypothesis: Alphabet indexing error at upper bound could give wrong char.
    """
    result = _case4_to_base(35, 36)
    assert result == 'Z'
    assert isinstance(result, str)

from solution import to_base as _case5_to_base

def test_p6_docstring_example():
    """Verify against provided example in the docstring.

    Contract quote: "Example:
        >>> to_base(31, 16)
        '1F'"
    Input domain: num = 31 (> 0), b = 16 (valid, 2 <= b <= 36).
    Oracle: 31 = 1*16 + 15, so digits are 1 and F (15), giving '1F'.
    Fault hypothesis: Letter case mismatch (e.g., '1f' instead of '1F').
    """
    result = _case5_to_base(31, 16)
    assert result == '1F'
    assert isinstance(result, str)

from solution import to_base as _case6_to_base

def test_p7_letter_mapping_base_16():
    """Test letter mapping for base 16 with multiple letter digits.

    Contract quote: "Output: A string representing the value of num in base b."
    Input domain: num = 255 (> 0), b = 16 (valid, 2 <= b <= 36).
    Oracle: 255 = 15*16 + 15, both digits are 15 which maps to 'F', giving 'FF'.
    Fault hypothesis: Lowercase letters used, or incorrect digit decomposition.
    """
    result = _case6_to_base(255, 16)
    assert result == 'FF'
    assert isinstance(result, str)

from solution import to_base as _case7_to_base

def test_p8_num_equals_base():
    """Test num equals base (positional notation boundary).

    Contract quote: "Output: A string representing the value of num in base b."
    Input domain: num = 8 (> 0), b = 8 (valid, 2 <= b <= 36).
    Oracle: In any base b, the number b itself is represented as '10'.
    Fault hypothesis: Could return '8' or empty string instead of '10'.
    """
    result = _case7_to_base(8, 8)
    assert result == '10'
    assert isinstance(result, str)

from solution import to_base as _case8_to_base

def test_extra_large_number_base_2():
    """Test a larger number in base 2 to verify multi-digit correctness.

    Contract quote: "Output: A string representing the value of num in base b."
    Input domain: num = 1024 (> 0), b = 2 (valid, 2 <= b <= 36).
    Oracle: 1024 = 2^10, so binary is '1' followed by ten '0's = '10000000000'.
    Fault hypothesis: Accumulation error over many iterations could flip bits.
    """
    result = _case8_to_base(1024, 2)
    assert result == '10000000000'
    assert isinstance(result, str)

from solution import to_base as _case9_to_base

def test_extra_mixed_digits_base_36():
    """Test a number requiring mixed digit types in base 36.

    Contract quote: "Output: A string representing the value of num in base b."
    Input domain: num = 1234 (> 0), b = 36 (valid, 2 <= b <= 36).
    Oracle: 1234 // 36 = 34 remainder 10. 34 maps to 'Y', 10 maps to 'A'. Result is 'YA'.
    Fault hypothesis: Wrong alphabet index for digits >= 10 or reversed order.
    """
    result = _case9_to_base(1234, 36)
    assert result == 'YA'
    assert isinstance(result, str)
