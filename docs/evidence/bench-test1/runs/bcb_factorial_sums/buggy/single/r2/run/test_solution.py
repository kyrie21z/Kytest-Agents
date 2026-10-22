# Accepted by submit_tests; explanations in testgen_report.json.

import solution as _case0_solution

def test_factorial_sums_empty_list():
    '''Per the docstring: "If an empty list is given, the function returns empty lists."'''
    result = _case0_solution.factorial_sums([])
    assert result == ([], [])
    assert isinstance(result, tuple)
    assert len(result) == 2
