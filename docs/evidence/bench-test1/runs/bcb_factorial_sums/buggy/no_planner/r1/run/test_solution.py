# Accepted by submit_tests; explanations in testgen_report.json.

# Accepted by submit_tests; explanations in testgen_report.json.

def test_empty_list_returns_empty_tuples():
    """Empty list should return ([], [])."""
    from solution import factorial_sums
    result = factorial_sums([])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert result[0] == []
    assert result[1] == []

def test_type_error_non_list():
    """Non-list input should raise TypeError."""
    from solution import factorial_sums
    import pytest
    with pytest.raises(TypeError):
        factorial_sums((1, 2, 3))
    with pytest.raises(TypeError):
        factorial_sums('not a list')
    with pytest.raises(TypeError):
        factorial_sums(None)

def test_value_error_negative_and_zero():
    """Negative numbers and zero should raise ValueError (code checks number > 0)."""
    from solution import factorial_sums
    import pytest
    with pytest.raises(ValueError):
        factorial_sums([-1, 2, 3])
    with pytest.raises(ValueError):
        factorial_sums([0, 4])
    with pytest.raises(ValueError):
        factorial_sums([0])


def test_valid_positive_integers():
    """Valid positive integers [1, 2, 3] should return correct sums and permutations."""
    from solution import factorial_sums
    result = factorial_sums([1, 2, 3])
    assert isinstance(result, tuple)
    assert len(result) == 2
    expected_sums = [9, 9, 9, 9, 9, 9]
    expected_perms = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    assert result[0] == expected_sums
    assert result[1] == expected_perms

def test_type_error_non_integer_elements():
    """List containing non-integer elements should raise TypeError."""
    from solution import factorial_sums
    import pytest
    with pytest.raises(TypeError):
        factorial_sums([1, 2.5])
    with pytest.raises(TypeError):
        factorial_sums(['a', 'b'])
    with pytest.raises(TypeError):
        factorial_sums([1, None])

def test_value_error_negative_only():
    """Strictly negative numbers should raise ValueError."""
    from solution import factorial_sums
    import pytest
    with pytest.raises(ValueError):
        factorial_sums([-1, 2, 3])
    with pytest.raises(ValueError):
        factorial_sums([-5])
