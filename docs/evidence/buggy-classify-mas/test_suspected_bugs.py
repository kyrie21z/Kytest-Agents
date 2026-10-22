# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

from solution import classify

def test_p5_upper_bound():
    """Value equals upper bound.

    Docstring quote: 'return -1 below low, 1 above high, and 0 inside the inclusive interval.'

    Input domain: value=10, low=1, high=10 — integer, value equals high.

    Oracle: The interval is inclusive, so low <= value <= high yields 0.
    Since 10 == high, the value is inside the interval. Expected return is 0.

    Fault hypothesis: If the implementation uses '>=' for the upper-bound check
    (i.e., value >= high → return 1), it will return 1 instead of 0, treating
    the upper bound as exclusive. This is a known off-by-one bug pattern.
    """
    result = classify(10, 1, 10)
    assert isinstance(result, int), f"Expected int, got {type(result)}"
    assert result == 0, f"Value 10 at upper bound of [1, 10] should return 0, got {result}"

from solution import classify

def test_p6_degenerate_interval():
    """Degenerate interval where low equals high.

    Docstring quote: 'return -1 below low, 1 above high, and 0 inside the inclusive interval.'

    Input domain: value=5, low=5, high=5 — integer, degenerate single-point interval.

    Oracle: When low == high, the interval contains only one point. Since it's
    inclusive, value == low == high means the value is inside. Expected return is 0.

    Fault hypothesis: With low == high, any value equal to that point must return 0.
    If the implementation uses 'value >= high' to detect 'above', then value == high
    triggers the 'above' branch and returns 1, which is wrong for an inclusive interval.
    """
    result = classify(5, 5, 5)
    assert isinstance(result, int), f"Expected int, got {type(result)}"
    assert result == 0, f"Value 5 in degenerate interval [5, 5] should return 0, got {result}"
