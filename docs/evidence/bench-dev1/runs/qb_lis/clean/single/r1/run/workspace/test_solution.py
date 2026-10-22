# Accepted by submit_tests; explanations in testgen_report.json.

from solution import lis as _case0_lis

def test_lis_empty():
    """Test that an empty array returns 0."""
    result = _case0_lis([])
    assert result == 0
    assert isinstance(result, int)

from solution import lis as _case1_lis

def test_lis_single_element():
    """Test that a single-element array returns 1."""
    result = _case1_lis([42])
    assert result == 1
    assert isinstance(result, int)

from solution import lis as _case2_lis

def test_lis_all_increasing():
    """Test that a fully sorted increasing array returns its length."""
    result = _case2_lis([1, 2, 3, 4, 5])
    assert result == 5
    assert isinstance(result, int)

from solution import lis as _case3_lis

def test_lis_all_decreasing():
    """Test that a fully sorted decreasing array returns 1."""
    result = _case3_lis([5, 4, 3, 2, 1])
    assert result == 1
    assert isinstance(result, int)

from solution import lis as _case4_lis

def test_lis_two_elements():
    """Test boundary case with two elements, both increasing and decreasing."""
    assert _case4_lis([1, 2]) == 2
    assert _case4_lis([2, 1]) == 1
    assert isinstance(_case4_lis([1, 2]), int)
    assert isinstance(_case4_lis([2, 1]), int)

from solution import lis as _case5_lis

def test_lis_example_from_docstring():
    """Test the example given in the docstring."""
    result = _case5_lis([4, 1, 5, 3, 7, 6, 2])
    assert result == 3
    assert isinstance(result, int)
