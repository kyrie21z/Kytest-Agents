# Accepted by submit_tests; explanations in testgen_report.json.

from solution import lis as _case0_lis

def test_p1_empty_list():
    """Return length for empty input.

    Contract quote:
        'Output: The length of the longest monotonically increasing subsequence of arr'

    An empty sequence has no elements, so the length must be 0.
    """
    result = _case0_lis([])
    assert isinstance(result, int)
    assert result == 0

from solution import lis as _case1_lis

def test_p2_single_element():
    """Return length for single-element input.

    Contract quote:
        'Output: The length of the longest monotonically increasing subsequence of arr'

    A single element trivially satisfies the increasing condition. Length is 1.
    """
    result = _case1_lis([42])
    assert isinstance(result, int)
    assert result == 1

from solution import lis as _case2_lis

def test_p3_already_sorted():
    """Return full length for already sorted input.

    Contract quote:
        'Output: The length of the longest monotonically increasing subsequence of arr'

    The entire sequence [1, 2, 3, 4, 5] is strictly increasing.
    The longest increasing subsequence is the sequence itself, yielding length 5.
    """
    result = _case2_lis([1, 2, 3, 4, 5])
    assert isinstance(result, int)
    assert result == 5

from solution import lis as _case3_lis

def test_p4_reverse_sorted():
    """Return minimal length for reverse-sorted input.

    Contract quote:
        'Output: The length of the longest monotonically increasing subsequence of arr'

    No two elements form an increasing pair in [5, 4, 3, 2, 1].
    The longest increasing subsequence consists of any single element, so length is 1.
    """
    result = _case3_lis([5, 4, 3, 2, 1])
    assert isinstance(result, int)
    assert result == 1

from solution import lis as _case4_lis

def test_p6_negative_integers():
    """Handle negative integers correctly.

    Contract quote:
        'Input: arr: A sequence of ints'

    The spec accepts 'A sequence of ints' without range restrictions.
    Negative integers follow standard numeric ordering, making [-10, -5, 0, 5] fully increasing.
    """
    result = _case4_lis([-10, -5, 0, 5])
    assert isinstance(result, int)
    assert result == 4

from solution import lis as _case5_lis

def test_p8_non_contiguous():
    """Verify non-contiguous increasing patterns.

    Contract quote:
        'Output: The length of the longest monotonically increasing subsequence of arr'

    Tests interleaved elements. The longest increasing subsequence is [1, 2, 3, 7]
    (or [1, 2, 6, 7]), confirming the algorithm correctly skips non-increasing elements
    while maintaining order.
    """
    result = _case5_lis([1, 5, 2, 6, 3, 7])
    assert isinstance(result, int)
    assert result == 4

from solution import lis as _case6_lis

def test_extra_return_type():
    """Verify return type is always int.

    Contract quote:
        'Output: The length of the longest monotonically increasing subsequence of arr'

    The output is defined as a length, which must be an integer.
    Test across multiple inputs to ensure consistent return type.
    """
    for arr, expected_len in [([], 0), ([1], 1), ([1, 2], 2), ([2, 1], 1), ([1, 3, 2], 2)]:
        result = _case6_lis(arr)
        assert isinstance(result, int), f'Expected int, got {type(result)} for input {arr}'
        assert result == expected_len, f'Expected {expected_len}, got {result} for input {arr}'

from solution import lis as _case7_lis

def test_extra_two_elements():
    """Test all two-element combinations.

    Contract quote:
        'Output: The length of the longest monotonically increasing subsequence of arr'

    For any two distinct elements, the LIS is 2 if first < second, else 1.
    """
    assert _case7_lis([1, 2]) == 2
    assert _case7_lis([2, 1]) == 1
    assert _case7_lis([-5, -3]) == 2
    assert _case7_lis([-3, -5]) == 1

from solution import lis as _case8_lis

def test_extra_alternating():
    """Test alternating high-low pattern.

    Contract quote:
        'Output: The length of the longest monotonically increasing subsequence of arr'

    [5, 1, 6, 2, 7, 3, 8, 4]: Pick every other starting from index 1:
    [1, 2, 3, 4] = length 4. Or [5, 6, 7, 8] = length 4.
    Both yield 4; no longer subsequence exists.
    """
    result = _case8_lis([5, 1, 6, 2, 7, 3, 8, 4])
    assert isinstance(result, int)
    assert result == 4
