# Accepted by submit_tests; explanations in testgen_report.json.

def test_p1_docstring_example():
    """Returns the correct LIS length for the documented example."""
    from solution import lis
    assert lis([4, 1, 5, 3, 7, 6, 2]) == 3

def test_p4_sorted_ascending():
    """Returns full length for already sorted ascending input."""
    from solution import lis
    result = lis([1, 2, 3, 4, 5])
    assert isinstance(result, int)
    assert result == 5

def test_p5_reverse_sorted():
    """Returns minimum length for reverse-sorted input."""
    from solution import lis
    result = lis([5, 4, 3, 2, 1])
    assert isinstance(result, int)
    assert result == 1

def test_p6_interleaved():
    """Correctly selects optimal path through interleaved values."""
    from solution import lis
    result = lis([1, 3, 2, 4, 6, 5])
    assert isinstance(result, int)
    assert result == 4

def test_p2_empty_list():
    """Handles empty sequence input."""
    from solution import lis
    result = lis([])
    assert isinstance(result, int)
    assert result == 0

def test_p3_single_element():
    """Handles single-element sequence."""
    from solution import lis
    result = lis([42])
    assert isinstance(result, int)
    assert result == 1
