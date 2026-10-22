# Accepted by submit_tests; explanations in testgen_report.json.

# Accepted by submit_tests; explanations in testgen_report.json.

from solution import kth as _case0_kth

def test_p2_min_element():
    """Returns minimum element when k=0.

    Spec quote: 'The kth-lowest element of arr (0-based)'
    Input domain: arr=[10, 20, 30], k=0; precondition 0<=0<3 holds.
    Oracle: sorted([10,20,30])[0] = 10.
    Fault hypothesis: Off-by-one error could skip the first element entirely.
    """
    assert _case0_kth([10, 20, 30], 0) == 10

from solution import kth as _case1_kth

def test_p4_duplicates():
    """Handles duplicate values correctly by counting them in rank order.

    Spec quote: 'efficient equivalent to sorted(arr)[k]'
    Input domain: arr=[4, 2, 4, 1, 2], k=1; precondition 0<=1<5 holds.
    Oracle: sorted([4,2,4,1,2]) = [1,2,2,4,4]; index 1 yields 2.
    Fault hypothesis: Duplicates of the pivot might be mishandled in partition
        boundaries, causing incorrect rank assignment.
    """
    assert _case1_kth([4, 2, 4, 1, 2], 1) == 2

from solution import kth as _case2_kth

def test_p6_single_element():
    """Works correctly on a single-element list.

    Spec quote: 'Precondition: 0 <= k < len(arr)'
    Input domain: arr=[99], k=0; precondition 0<=0<1 holds.
    Oracle: sorted([99])[0] = 99.
    Fault hypothesis: Edge case where below/above are both empty might
        incorrectly recurse instead of returning pivot.
    """
    assert _case2_kth([99], 0) == 99

from solution import kth as _case3_kth

def test_p8_large_k():
    """Handles larger k values near the upper bound.

    Spec quote: 'equivalent to sorted(arr)[k]'
    Input domain: arr=[15, 3, 12, 7, 9], k=4; precondition 0<=4<5 holds.
    Oracle: sorted([15,3,12,7,9]) = [3,7,9,12,15]; index 4 yields 15.
    Fault hypothesis: Recursion into 'above' without adjusting k causes
        out-of-range access or infinite recursion.
    """
    assert _case3_kth([15, 3, 12, 7, 9], 4) == 15

from solution import kth as _case4_kth

def test_extra_all_same():
    """All elements identical: any k should return that element.

    Spec quote: 'efficient equivalent to sorted(arr)[k]'
    Input domain: arr=[5, 5, 5, 5], k=2; precondition 0<=2<4 holds.
    Oracle: sorted([5,5,5,5]) = [5,5,5,5]; any index yields 5.
    Fault hypothesis: When all elements equal pivot, below=[] and above=[],
        num_less=0, num_lessoreq=4. k=2 falls in else branch returning pivot=5.
        But if k >= num_lessoreq triggers recursion into empty above, crash occurs.
    """
    assert _case4_kth([5, 5, 5, 5], 2) == 5

from solution import kth as _case5_kth

def test_extra_two_elements():
    """Two-element list with both k=0 and k=1 tested.

    Spec quote: 'The kth-lowest element of arr (0-based)'
    Input domain: arr=[42, 17], k=0 and k=1; precondition holds for both.
    Oracle: sorted([42,17]) = [17,42]; index 0 yields 17, index 1 yields 42.
    Fault hypothesis: Small lists may not exercise partition logic properly;
        k adjustment bug could manifest here.
    """
    assert _case5_kth([42, 17], 0) == 17
    assert _case5_kth([42, 17], 1) == 42


from solution import kth as _new5dc508700_kth

def test_min_element():
    """Returns minimum element when k=0.

    Spec quote: 'The kth-lowest element of arr (0-based)'
    Input domain: arr=[10, 20, 30], k=0; precondition 0<=0<3 holds.
    Oracle: sorted([10,20,30])[0] = 10.
    Fault hypothesis: Off-by-one could skip the first element entirely.
    """
    assert _new5dc508700_kth([10, 20, 30], 0) == 10

from solution import kth as _new5dc508701_kth

def test_single_element():
    """Works correctly on a single-element list.

    Spec quote: 'Precondition: 0 <= k < len(arr)'
    Input domain: arr=[99], k=0; precondition 0<=0<1 holds.
    Oracle: sorted([99])[0] = 99.
    Fault hypothesis: Edge case where below/above are both empty might
        incorrectly recurse instead of returning pivot.
    """
    assert _new5dc508701_kth([99], 0) == 99

from solution import kth as _new5dc508702_kth

def test_all_same():
    """All elements identical: any k should return that element.

    Spec quote: 'efficient equivalent to sorted(arr)[k]'
    Input domain: arr=[5, 5, 5, 5], k=2; precondition 0<=2<4 holds.
    Oracle: sorted([5,5,5,5]) = [5,5,5,5]; any index yields 5.
    Fault hypothesis: When all elements equal pivot, below=[] and above=[],
        num_less=0, num_lessoreq=4. k=2 falls in else branch returning pivot=5.
    """
    assert _new5dc508702_kth([5, 5, 5, 5], 2) == 5

from solution import kth as _new5dc508703_kth

def test_recurse_below():
    """Handles duplicate values correctly by counting them in rank order.

    Spec quote: 'efficient equivalent to sorted(arr)[k]'
    Input domain: arr=[4, 2, 4, 1, 2], k=1; precondition 0<=1<5 holds.
    Oracle: sorted([4,2,4,1,2]) = [1,2,2,4,4]; index 1 yields 2.
    Fault hypothesis: Duplicates of the pivot might be mishandled in partition
        boundaries, causing incorrect rank assignment.
    """
    assert _new5dc508703_kth([4, 2, 4, 1, 2], 1) == 2

from solution import kth as _new5dc508704_kth

def test_return_pivot():
    """Handles larger k values near the upper bound.

    Spec quote: 'equivalent to sorted(arr)[k]'
    Input domain: arr=[15, 3, 12, 7, 9], k=4; precondition 0<=4<5 holds.
    Oracle: sorted([15,3,12,7,9]) = [3,7,9,12,15]; index 4 yields 15.
    Fault hypothesis: Recursion into 'above' without adjusting k causes
        out-of-range access or infinite recursion.
    """
    assert _new5dc508704_kth([15, 3, 12, 7, 9], 4) == 15

from solution import kth as _new5dc508705_kth

def test_two_elements():
    """Two-element list with both k=0 and k=1 tested.

    Spec quote: 'The kth-lowest element of arr (0-based)'
    Input domain: arr=[42, 17], k=0 and k=1; precondition holds for both.
    Oracle: sorted([42,17]) = [17,42]; index 0 yields 17, index 1 yields 42.
    Fault hypothesis: Small lists may not exercise partition logic properly;
        k adjustment bug could manifest here.
    """
    assert _new5dc508705_kth([42, 17], 0) == 17
    assert _new5dc508705_kth([42, 17], 1) == 42
