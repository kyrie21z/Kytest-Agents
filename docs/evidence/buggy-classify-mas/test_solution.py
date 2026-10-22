# Accepted by submit_tests; explanations in testgen_report.json.

from solution import classify as _case0_classify

def test_p1_value_inside_interval():
    """Value strictly inside interval.

    Docstring quote: 'return -1 below low, 1 above high, and 0 inside the inclusive interval.'

    Input domain: value=5, low=1, high=10 — integer, value strictly between bounds.

    Oracle: 5 is strictly greater than low (1) and strictly less than high (10),
    so it lies inside the inclusive interval [1, 10]. Expected return is 0.

    Fault hypothesis: If the implementation mistakenly treats the interval as
    exclusive on one side or swaps the return values, this case would still pass
    only if both sides are symmetric; however combined with boundary tests it
    helps confirm correct interior semantics.
    """
    result = _case0_classify(5, 1, 10)
    assert isinstance(result, int), f'Expected int, got {type(result)}'
    assert result == 0, f'Value 5 inside [1, 10] should return 0, got {result}'

from solution import classify as _case1_classify

def test_p2_value_below_interval():
    """Value strictly below interval.

    Docstring quote: 'return -1 below low, 1 above high, and 0 inside the inclusive interval.'

    Input domain: value=0, low=1, high=10 — integer, value below lower bound.

    Oracle: 0 < 1, so the value is below the interval. Expected return is -1.

    Fault hypothesis: If the implementation confuses the sign of the return
    value (e.g., returns 1 instead of -1 for below), this assertion catches it.
    """
    result = _case1_classify(0, 1, 10)
    assert isinstance(result, int), f'Expected int, got {type(result)}'
    assert result == -1, f'Value 0 below [1, 10] should return -1, got {result}'

from solution import classify as _case2_classify

def test_p3_value_above_interval():
    """Value strictly above interval.

    Docstring quote: 'return -1 below low, 1 above high, and 0 inside the inclusive interval.'

    Input domain: value=11, low=1, high=10 — integer, value above upper bound.

    Oracle: 11 > 10, so the value is above the interval. Expected return is 1.

    Fault hypothesis: If the implementation returns -1 for above (swapped signs)
or fails to distinguish above from inside, this catches it.
    """
    result = _case2_classify(11, 1, 10)
    assert isinstance(result, int), f'Expected int, got {type(result)}'
    assert result == 1, f'Value 11 above [1, 10] should return 1, got {result}'

from solution import classify as _case3_classify

def test_p4_lower_bound():
    """Value equals lower bound.

    Docstring quote: 'return -1 below low, 1 above high, and 0 inside the inclusive interval.'

    Input domain: value=1, low=1, high=10 — integer, value equals low.

    Oracle: The interval is inclusive, so low <= value <= high yields 0.
    Since 1 == low, the value is inside the interval. Expected return is 0.

    Fault hypothesis: If the implementation uses strict inequality (<) for the
    lower-bound check instead of <=, it would incorrectly return -1 here.
    """
    result = _case3_classify(1, 1, 10)
    assert isinstance(result, int), f'Expected int, got {type(result)}'
    assert result == 0, f'Value 1 at lower bound of [1, 10] should return 0, got {result}'

from solution import classify as _case4_classify

def test_p7_negative_values():
    """Negative numeric values.

    Docstring quote: 'return -1 below low, 1 above high, and 0 inside the inclusive interval.'

    Input domain: value=-5, low=-10, high=-1 — negative integers, value strictly between bounds.

    Oracle: -10 < -5 < -1, so -5 is inside the inclusive interval [-10, -1]. Expected return is 0.

    Fault hypothesis: If the implementation mishandles negative numbers (e.g., sign errors in comparison), this would catch it.
    """
    result = _case4_classify(-5, -10, -1)
    assert isinstance(result, int), f'Expected int, got {type(result)}'
    assert result == 0, f'Value -5 inside [-10, -1] should return 0, got {result}'

from solution import classify as _case5_classify

def test_p8_float_lower_bound():
    """Floating point exact match at lower bound.

    Docstring quote: 'return -1 below low, 1 above high, and 0 inside the inclusive interval.'

    Input domain: value=0.0, low=0.0, high=1.0 — floats, value equals low.

    Oracle: The interval is inclusive, so low <= value <= high yields 0.
    Since 0.0 == low, the value is inside the interval. Expected return is 0.

    Fault hypothesis: If the implementation uses strict inequality for the lower-bound check,
    it would incorrectly return -1 here with float inputs.
    """
    result = _case5_classify(0.0, 0.0, 1.0)
    assert isinstance(result, int), f'Expected int, got {type(result)}'
    assert result == 0, f'Value 0.0 at lower bound of [0.0, 1.0] should return 0, got {result}'
