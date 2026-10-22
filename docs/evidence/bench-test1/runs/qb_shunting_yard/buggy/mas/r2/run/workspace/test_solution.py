# Accepted by submit_tests; explanations in testgen_report.json.

# Accepted by submit_tests; explanations in testgen_report.json.

from solution import shunting_yard as _case0_shunting_yard

def test_p4_single_operand_boundary():
    result = _case0_shunting_yard([42])
    assert result == [42]


from solution import shunting_yard as _new0c945ee60_shunting_yard

def test_p6_empty_list():
    """P6: Handles an empty input list gracefully."""
    result = _new0c945ee60_shunting_yard([])
    assert result == []
