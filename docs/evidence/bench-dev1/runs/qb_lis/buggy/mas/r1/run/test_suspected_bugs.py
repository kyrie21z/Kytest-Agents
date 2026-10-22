# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

from solution import lis

def test_p5_docstring_example():
    """Match provided docstring example.

    Contract quote:
        'The length of the longest monotonically increasing subsequence of arr'

    Valid subsequences include [1, 3, 7] or [1, 5, 7], both of length 3.
    No subsequence of length 4 exists because after picking any 3 increasing elements,
    the remaining elements cannot extend them.
    """
    result = lis([4, 1, 5, 3, 7, 6, 2])
    assert isinstance(result, int)
    assert result == 3

from solution import lis

def test_p7_tuple_input():
    """Accept tuple sequences.

    Contract quote:
        'Input: arr: A sequence of ints'

    Tuples are standard Python sequences and should yield the same result as equivalent lists.
    For (10, 20, 5, 30), the LIS is [10, 20, 30] of length 3.
    """
    result = lis((10, 20, 5, 30))
    assert isinstance(result, int)
    assert result == 3

from solution import lis

def test_extra_unique_precondition():
    """Test with larger unique-element input to verify correctness.

    Contract quote:
        'Precondition: The ints in arr are unique'

    Using a known case: [3, 1, 4, 1, 5] violates the uniqueness precondition.
    Instead, use [10, 20, 1, 30, 2, 40, 3, 50] where LIS = [10, 20, 30, 40, 50] = 5.
    """
    result = lis([10, 20, 1, 30, 2, 40, 3, 50])
    assert isinstance(result, int)
    assert result == 5

from solution import lis

def test_extra_ascending_then_drop():
    """Test ascending sequence followed by a drop.

    Contract quote:
        'Output: The length of the longest monotonically increasing subsequence of arr'

    [1, 2, 3, 0, 4, 5]: LIS is [1, 2, 3, 4, 5] of length 5.
    The drop to 0 does not break the non-contiguous subsequence.
    """
    result = lis([1, 2, 3, 0, 4, 5])
    assert isinstance(result, int)
    assert result == 5
