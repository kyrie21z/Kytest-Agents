# Accepted by submit_tests; explanations in testgen_report.json.

from solution import lis as _case0_lis

def test_p2_empty_list():
    """Returns 0 for an empty input sequence.

    Contract quote: 'Output: The length of the longest monotonically
                     increasing subsequence of arr'
    Input domain: An empty list [].
    Oracle: By definition, the longest increasing subsequence of an empty set
            has length 0.
    Fault hypothesis: Detects returning 1 or raising an IndexError on empty input.
    """
    assert _case0_lis([]) == 0

from solution import lis as _case1_lis

def test_p3_single_element():
    """Returns 1 for a single-element sequence.

    Contract quote: 'Output: The length of the longest monotonically
                     increasing subsequence of arr'
    Input domain: A list with one integer [42].
    Oracle: A sequence of length 1 contains exactly one increasing subsequence
            of length 1 (the element itself).
    Fault hypothesis: Detects returning 0 for non-empty input.
    """
    assert _case1_lis([42]) == 1

from solution import lis as _case2_lis

def test_p4_sorted_increasing():
    """Returns the full sequence length when already sorted increasingly.

    Contract quote: 'Output: The length of the longest monotonically
                     increasing subsequence of arr'
    Input domain: A strictly increasing list [1, 2, 3, 4, 5].
    Oracle: The entire sequence satisfies 'monotonically increasing', so the
            LIS length equals the input length (5).
    Fault hypothesis: Detects undercounting due to incorrect comparison logic.
    """
    assert _case2_lis([1, 2, 3, 4, 5]) == 5

from solution import lis as _case3_lis

def test_p5_strictly_decreasing():
    """Returns 1 for a strictly decreasing sequence.

    Contract quote: 'Output: The length of the longest monotonically
                     increasing subsequence of arr'
    Input domain: A strictly decreasing list [5, 4, 3, 2, 1].
    Oracle: No two elements form an increasing pair, so the maximum possible
            LIS length is 1 (any single element).
    Fault hypothesis: Detects returning 0 or incorrectly counting equal elements.
    """
    assert _case3_lis([5, 4, 3, 2, 1]) == 1

from solution import lis as _case4_lis

def test_p6_negative_integers():
    """Correctly processes negative integers and skips intermediate values.

    Contract quote: 'Output: The length of the longest monotonically
                     increasing subsequence of arr'
    Input domain: A list of unique negative/zero integers [-10, -5, -8, -2, 0].
    Oracle: The subsequence [-10, -5, -2, 0] is strictly increasing and maximal
            in length (4). The element -8 breaks the chain but is skipped.
    Fault hypothesis: Detects sign errors or incorrect ordering of negatives.
    """
    assert _case4_lis([-10, -5, -8, -2, 0]) == 4

from solution import lis as _case5_lis

def test_p7_tuple_input():
    """Accepts tuple inputs as valid sequences.

    Contract quote: 'Input: arr: A sequence of ints'
    Input domain: A tuple of unique integers (7, 1, 8, 2, 9).
    Oracle: Tuples are standard Python sequences; iteration yields the same
            elements as a list. The LIS is [1, 2, 9] or [7, 8, 9], both
            of length 3.
    Fault hypothesis: Detects type-specific bugs that reject tuples.
    """
    assert _case5_lis((7, 1, 8, 2, 9)) == 3

from solution import lis as _case6_lis

def test_p8_overlapping_candidates():
    """Selects the optimal path across overlapping candidate subsequences.

    Contract quote: 'Output: The length of the longest monotonically
                     increasing subsequence of arr'
    Input domain: A list [10, 20, 10, 30, 20, 50]. Note: violates uniqueness
                  precondition, but the implementation still handles it.
    Oracle: The longest increasing subsequence is [10, 20, 30, 50] using
            indices 0,1,3,5 (or 0,2,3,5), yielding length 4.
    Fault hypothesis: Detects greedy choices that miss the globally optimal path.
    """
    assert _case6_lis([10, 20, 10, 30, 20, 50]) == 4

from solution import lis as _case7_lis

def test_extra_return_type():
    """Verifies the return type is int for various inputs.

    Contract quote: 'Output: The length of the longest monotonically
                     increasing subsequence of arr'
    Input domain: Lists of varying sizes and compositions.
    Oracle: The output specification says 'length', which is always an int.
    Fault hypothesis: Detects accidental return of float, str, or None.
    """
    assert isinstance(_case7_lis([1]), int)
    assert isinstance(_case7_lis([]), int)
    assert isinstance(_case7_lis([3, 1, 2]), int)
    assert isinstance(_case7_lis(list(range(10))), int)

from solution import lis as _case8_lis

def test_extra_two_elements_equal():
    """Handles two identical elements (violates uniqueness precondition).

    Contract quote: 'Precondition: The ints in arr are unique'
    Input domain: A list [5, 5] where elements are not unique.
    Oracle: Strictly increasing requires strict less-than; [5, 5] has no
            increasing pair, so LIS length is 1.
    Fault hypothesis: Detects treating equal elements as increasing (would
                      return 2) or crashing on duplicates.
    """
    assert _case8_lis([5, 5]) == 1

from solution import lis as _case9_lis

def test_extra_large_increasing():
    """Tests correctness on a moderately large increasing sequence.

    Contract quote: 'Output: The length of the longest monotonically
                     increasing subsequence of arr'
    Input domain: list(range(50)), i.e., [0, 1, 2, ..., 49].
    Oracle: The entire sequence is strictly increasing, so LIS length is 50.
    Fault hypothesis: Detects O(n^2) timeout or incorrect boundary handling.
    """
    assert _case9_lis(list(range(50))) == 50
