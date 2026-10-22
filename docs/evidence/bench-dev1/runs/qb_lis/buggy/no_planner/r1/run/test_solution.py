# Accepted by submit_tests; explanations in testgen_report.json.

def test_empty_list():
    """Empty list should return 0 since no elements exist."""
    from solution import lis
    result = lis([])
    assert result == 0
    assert isinstance(result, int)

def test_single_element():
    """A single-element list has LIS of length 1."""
    from solution import lis
    result = lis([42])
    assert result == 1
    assert isinstance(result, int)

def test_sorted_increasing():
    """A fully sorted list has LIS equal to its full length."""
    from solution import lis
    arr = list(range(1, 11))
    result = lis(arr)
    assert result == 10
    assert isinstance(result, int)

def test_reverse_sorted():
    """A reverse-sorted list has LIS of length 1 (any single element)."""
    from solution import lis
    arr = list(range(10, 0, -1))
    result = lis(arr)
    assert result == 1
    assert isinstance(result, int)

def test_negative_and_mixed_values():
    """Test with negative numbers and mixed values.
    LIS of [-3, -1, -2, 0, 1] is 4: [-3, -1, 0, 1] or [-3, -2, 0, 1]."""
    from solution import lis
    result = lis([-3, -1, -2, 0, 1])
    assert result == 4
    assert isinstance(result, int)

def test_two_elements_increasing():
    """Two elements in increasing order have LIS of 2."""
    from solution import lis
    result = lis([1, 2])
    assert result == 2
    assert isinstance(result, int)

def test_two_elements_decreasing():
    """Two elements in decreasing order have LIS of 1."""
    from solution import lis
    result = lis([2, 1])
    assert result == 1
    assert isinstance(result, int)

def test_alternating_pattern():
    """Alternating up-down pattern: [1, 3, 2, 4, 3, 5].
    LIS is 3: e.g., [1, 2, 3] or [1, 2, 4] or [1, 3, 4] etc.
    Actually [1, 2, 3, 5] has length 4. Let me verify.
    Subsequences: [1,3,4,5] len=4, [1,2,3,5] len=4, [1,2,4,5] len=4."""
    from solution import lis
    result = lis([1, 3, 2, 4, 3, 5])
    assert result == 4
    assert isinstance(result, int)

def test_larger_sorted():
    """Test with a larger sorted sequence to verify scalability."""
    from solution import lis
    arr = list(range(1, 101))
    result = lis(arr)
    assert result == 100
    assert isinstance(result, int)

def test_interleaved_subsequences():
    """Interleaved increasing subsequences: [5, 1, 6, 2, 7, 3].
    LIS is 3 via [1,2,3] or [5,6,7]."""
    from solution import lis
    result = lis([5, 1, 6, 2, 7, 3])
    assert result == 3
    assert isinstance(result, int)
