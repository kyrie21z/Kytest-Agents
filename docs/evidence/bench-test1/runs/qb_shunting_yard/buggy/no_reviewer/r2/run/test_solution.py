# Accepted by submit_tests; explanations in testgen_report.json.

from solution import shunting_yard as _case0_shunting_yard

def test_p4_empty_list():
    result = _case0_shunting_yard([])
    assert result == []

from solution import shunting_yard as _case1_shunting_yard

def test_p5_single_operand():
    result = _case1_shunting_yard([42])
    assert result == [42]
