# Accepted by submit_tests; explanations in testgen_report.json.

def test_p1_example():
    """P1: Returns the length of the LIS for the provided example."""
    from solution import lis
    assert lis([4, 1, 5, 3, 7, 6, 2]) == 3

def test_p2_sorted():
    """P2: Returns full length when array is already sorted."""
    from solution import lis
    assert lis([1, 2, 3, 4, 5]) == 5

def test_p3_reverse_sorted():
    """P3: Returns 1 when array is reverse sorted."""
    from solution import lis
    assert lis([5, 4, 3, 2, 1]) == 1

def test_p4_single_element():
    """P4: Returns 1 for a single-element sequence."""
    from solution import lis
    assert lis([42]) == 1

def test_p5_empty():
    """P5: Returns 0 for an empty sequence."""
    from solution import lis
    assert lis([]) == 0

def test_p6_interleaved():
    """P6: Correctly identifies LIS across interleaved patterns."""
    from solution import lis
    assert lis([10, 2, 30, 4, 50]) == 3

def test_p7_large_integers():
    """P7: Handles large integer values correctly."""
    from solution import lis
    assert lis([1000000000, 999999999, 999999998]) == 1

def test_p8_tuple_input():
    """P8: Accepts tuple input as a valid sequence."""
    from solution import lis
    assert lis((3, 1, 2)) == 2

def test_extra_two_elements_increasing():
    """Extra: Two-element increasing sequence."""
    from solution import lis
    assert lis([1, 2]) == 2

def test_extra_two_elements_decreasing():
    """Extra: Two-element decreasing sequence."""
    from solution import lis
    assert lis([5, 3]) == 1

def test_extra_alternating():
    """Extra: Alternating up-down pattern."""
    from solution import lis
    assert lis([1, 3, 2, 4, 3, 5]) == 4
