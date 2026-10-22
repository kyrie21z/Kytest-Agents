# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

def test_spec_example_simple():
    from solution import shunting_yard
    result = shunting_yard([10, '-', 5, '-', 2])
    assert result == [10, 5, '-', 2, '-']
