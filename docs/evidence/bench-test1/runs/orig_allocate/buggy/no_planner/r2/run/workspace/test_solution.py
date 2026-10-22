# Accepted by submit_tests; explanations in testgen_report.json.

def test_value_error_negative_total():
    """allocate must raise ValueError when total is negative."""
    from solution import allocate
    import pytest
    with pytest.raises(ValueError):
        allocate(-1, [1, 2])

def test_sum_equals_total():
    """The sum of allocated shares must always equal the input total."""
    from solution import allocate
    for total, weights in [(100, [1, 1, 1]), (10, [3, 0, 7]), (0, [5, 3]), (7, [1, 0, 1]), (5, [2, 2, 2]), (13, [4, 6]), (1, [100]), (50, [1, 2, 3, 4])]:
        result = allocate(total, weights)
        assert sum(result) == total, f'sum({result}) != {total}'

def test_zero_weight_entry():
    """Entries with weight 0 must always receive 0, even when leftover exists."""
    from solution import allocate
    result = allocate(7, [1, 0, 1])
    assert result == [3, 0, 4]
    assert result[1] == 0

def test_tie_breaking_higher_index():
    """When multiple entries share the same largest remainder, higher index wins per the sort key (-remainders[i], -i)."""
    from solution import allocate
    result = allocate(5, [2, 2, 2])
    assert result == [1, 2, 2]

def test_single_weight():
    """With a single weight, all of total goes to that one entry."""
    from solution import allocate
    result = allocate(42, [100])
    assert result == [42]

def test_zero_total():
    """When total is 0, every entry receives 0 regardless of weights."""
    from solution import allocate
    result = allocate(0, [5, 3, 2])
    assert result == [0, 0, 0]

def test_large_weights_ratio():
    """Allocation with very different weight magnitudes distributes proportionally."""
    from solution import allocate
    result = allocate(10, [3, 0, 7])
    assert result == [3, 0, 7]
