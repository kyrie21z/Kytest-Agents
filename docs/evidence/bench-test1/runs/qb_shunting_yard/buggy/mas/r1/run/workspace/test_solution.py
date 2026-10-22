# Accepted by submit_tests; explanations in testgen_report.json.

def test_p4_single_operand():
    from solution import shunting_yard
    result = shunting_yard([42])
    assert result == [42]

def test_p8_empty_list():
    from solution import shunting_yard
    result = shunting_yard([])
    assert result == []
