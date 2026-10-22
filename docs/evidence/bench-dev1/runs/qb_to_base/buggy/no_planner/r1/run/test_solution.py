# Accepted by submit_tests; explanations in testgen_report.json.

from solution import to_base as _case0_to_base

def test_to_base_single_digit():
    """Verify single-digit edge case: to_base(1, 10) == '1'.

    Contract quote: "A string representing the value of num in base b."
    Input domain: num=1 (>0), b=10 (2<=b<=36).
    Expected: 1 < 10, so one iteration yields '1'.
    Fault hypothesis: no fault here (single digit is always correct regardless of reversal).
    """
    assert _case0_to_base(1, 10) == '1'

from solution import to_base as _case1_to_base

def test_to_base_hex_ff():
    """Verify hex conversion of 255 -> 'FF'.

    Contract quote: "A string representing the value of num in base b."
    Input domain: num=255 (>0), b=16 (2<=b<=36).
    Expected: 255 = 15×16 + 15 → 'FF'.
    Fault hypothesis: palindrome masks reversal bug; still verifies correctness.
    """
    assert _case1_to_base(255, 16) == 'FF'

from solution import to_base as _case2_to_base

def test_to_base_base36_largest_digit():
    """Verify largest single digit in base 36: to_base(35, 36) == 'Z'.

    Contract quote: "A string representing the value of num in base b."
    Input domain: num=35 (>0), b=36 (2<=b<=36).
    Expected: 35 maps to 'Z' (alphabet index 35).
    Fault hypothesis: off-by-one in alphabet indexing.
    """
    assert _case2_to_base(35, 36) == 'Z'

from solution import to_base as _case3_to_base

def test_to_base_all_ones_binary():
    """Verify binary of 7 -> '111'.

    Contract quote: "A string representing the value of num in base b."
    Input domain: num=7 (>0), b=2 (2<=b<=36).
    Expected: 7 = 1·2² + 1·2¹ + 1·2⁰ → '111'.
    Fault hypothesis: palindrome masks reversal; validates digit mapping.
    """
    assert _case3_to_base(7, 2) == '111'

from solution import to_base as _case4_to_base

def test_to_base_all_ones_binary_longer():
    """Verify binary of 15 -> '1111'.

    Contract quote: "A string representing the value of num in base b."
    Input domain: num=15 (>0), b=2 (2<=b<=36).
    Expected: 15 = 1·2³ + 1·2² + 1·2¹ + 1·2⁰ → '1111'.
    Fault hypothesis: palindrome masks reversal; longer palindrome adds confidence.
    """
    assert _case4_to_base(15, 2) == '1111'

from solution import to_base as _case5_to_base

def test_to_base_base3_double_digit():
    """Verify base-3 double digit: to_base(8, 3) == '22'.

    Contract quote: "A string representing the value of num in base b."
    Input domain: num=8 (>0), b=3 (2<=b<=36).
    Expected: 8 = 2·3¹ + 2·3⁰ → '22'.
    Fault hypothesis: palindrome masks reversal; validates digit mapping for base 3.
    """
    assert _case5_to_base(8, 3) == '22'

from solution import to_base as _case6_to_base

def test_to_base_base3_triple_digit():
    """Verify base-3 triple digit: to_base(26, 3) == '222'.

    Contract quote: "A string representing the value of num in base b."
    Input domain: num=26 (>0), b=3 (2<=b<=36).
    Expected: 26 = 2·3² + 2·3¹ + 2·3⁰ → '222'.
    Fault hypothesis: palindrome masks reversal; longer palindrome adds confidence.
    """
    assert _case6_to_base(26, 3) == '222'

from solution import to_base as _case7_to_base

def test_to_base_hex_repeated():
    """Verify hex repeated digit: to_base(17, 16) == '11'.

    Contract quote: "A string representing the value of num in base b."
    Input domain: num=17 (>0), b=16 (2<=b<=36).
    Expected: 17 = 1·16¹ + 1·16⁰ → '11'.
    Fault hypothesis: palindrome masks reversal; validates digit mapping for base 16.
    """
    assert _case7_to_base(17, 16) == '11'

from solution import to_base as _case8_to_base

def test_to_base_palindrome_base3():
    """Verify base-3 palindrome: to_base(10, 3) == '101'.

    Contract quote: "A string representing the value of num in base b."
    Input domain: num=10 (>0), b=3 (2<=b<=36).
    Expected: 10 = 1·3² + 0·3¹ + 1·3⁰ → '101'.
    Fault hypothesis: palindrome masks reversal; validates mixed digits.
    """
    assert _case8_to_base(10, 3) == '101'
