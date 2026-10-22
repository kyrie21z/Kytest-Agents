# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

def test_docstring_example():
    """Verify the example from the docstring: [4,1,5,3,7,6,2] -> 3."""
    from solution import lis
    result = lis([4, 1, 5, 3, 7, 6, 2])
    assert result == 3
    assert isinstance(result, int)
