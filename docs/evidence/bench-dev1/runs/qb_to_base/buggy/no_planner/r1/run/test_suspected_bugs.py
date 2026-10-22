# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

from solution import to_base

def test_to_base_docstring_example():
    """Verify the documented example: to_base(31, 16) == '1F'.

    Contract quote: "A string representing the value of num in base b."
    Input domain: num=31 (>0), b=16 (2<=b<=36).
    Expected: 31 = 1×16 + 15 → '1F'.
    Fault hypothesis: implementation reverses digit order.
    """
    assert to_base(31, 16) == '1F'

from solution import to_base

def test_to_base_binary_conversion():
    """Verify binary conversion of 10 -> '1010'.

    Contract quote: "A string representing the value of num in base b."
    Input domain: num=10 (>0), b=2 (2<=b<=36).
    Expected: 10 = 1·2³ + 0·2² + 1·2¹ + 0·2⁰ → '1010'.
    Fault hypothesis: reversed output '0101' detected.
    """
    assert to_base(10, 2) == '1010'

from solution import to_base

def test_to_base_non_palindrome_hex():
    """Verify non-palindromic hex: to_base(100, 16) == '64'.

    Contract quote: "A string representing the value of num in base b."
    Input domain: num=100 (>0), b=16 (2<=b<=36).
    Expected: 100 = 6×16 + 4 → '64'.
    Fault hypothesis: reversed output '46' detected.
    """
    assert to_base(100, 16) == '64'
