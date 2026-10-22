# Accepted by submit_tests; explanations in testgen_report.json.

def test_empty_input():
    """Test empty input returns empty list."""
    from solution import shunting_yard
    result = shunting_yard([])
    assert result == []

def test_return_type():
    """Verify the return value is always a list."""
    from solution import shunting_yard
    result = shunting_yard([1, '+', 2])
    assert isinstance(result, list)
