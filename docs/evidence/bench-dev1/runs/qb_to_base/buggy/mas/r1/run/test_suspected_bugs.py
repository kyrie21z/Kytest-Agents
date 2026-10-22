# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

from solution import to_base

def test_p1_standard_decimal():
    """Verify standard decimal conversion remains unchanged."""
    assert to_base(123, 10) == '123'

from solution import to_base

def test_p6_base_rollover():
    """Verify base rollover behavior where num equals the base."""
    assert to_base(36, 36) == '10'

from solution import to_base

def test_p5_spec_example():
    """Verify the exact behavior shown in the specification example."""
    assert to_base(31, 16) == '1F'

from solution import to_base

def test_p7_power_of_two_binary():
    """Test a power-of-two value in the minimum base to verify zero-padding/multiple zeros."""
    assert to_base(256, 2) == '100000000'
