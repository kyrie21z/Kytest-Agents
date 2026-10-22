# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

from solution import kth

def test_p5_negative_ints():
    """Correctly orders and selects from negative integers.

    Spec quote: 'The kth-lowest element of arr (0-based)'
    Input domain: arr=[-5, -1, -3, 0], k=1; precondition 0<=1<4 holds.
    Oracle: sorted([-5,-1,-3,0]) = [-5,-3,-1,0]; index 1 yields -3.
    Fault hypothesis: Sign handling or comparison logic fails for negatives,
        or the recursion offset bug produces wrong result.
    """
    assert kth([-5, -1, -3, 0], 1) == -3
