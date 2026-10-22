# Accepted by submit_tests; explanations in testgen_report.json.

from solution import to_base as _case0_to_base

def test_p2_min_num():
    """Test the minimum allowed value for num."""
    assert _case0_to_base(1, 2) == '1'

from solution import to_base as _case1_to_base

def test_p3_min_base():
    """Test the minimum allowed value for b."""
    assert _case1_to_base(7, 2) == '111'

from solution import to_base as _case2_to_base

def test_p4_max_base_single_digit():
    """Test the maximum allowed value for b with largest single-digit value."""
    assert _case2_to_base(35, 36) == 'Z'

from solution import to_base as _case3_to_base

def test_p8_hex_ff():
    """Verify mixed-digit conversion in a mid-range base."""
    assert _case3_to_base(255, 16) == 'FF'
