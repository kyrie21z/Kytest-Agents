# Accepted by submit_tests; explanations in testgen_report.json.

"""Factor the smallest valid input which yields no prime factors."""
from solution import get_factors as _case0_get_factors

def test_p1_empty_list():
    assert _case0_get_factors(1) == []

"""Verify return type is always a list."""
from solution import get_factors as _case1_get_factors

def test_extra_return_type():
    assert isinstance(_case1_get_factors(1), list)
    assert isinstance(_case1_get_factors(2), list)
    assert isinstance(_case1_get_factors(6), list)
