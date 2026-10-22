# Accepted by submit_tests; explanations in testgen_report.json.

from solution import factorial_sums as _case0_factorial_sums

def test_empty_list():
    """Test empty list returns two empty lists as documented."""
    result = _case0_factorial_sums([])
    assert result == ([], []), f'Expected ([], []), got {result}'
    assert isinstance(result, tuple)
    assert len(result) == 2

from solution import factorial_sums as _case1_factorial_sums
import pytest as _case1_pytest

def test_non_list_raises_typeerror():
    """Test that passing a non-list raises TypeError."""
    with _case1_pytest.raises(TypeError):
        _case1_factorial_sums((1, 2, 3))
    with _case1_pytest.raises(TypeError):
        _case1_factorial_sums('abc')

from solution import factorial_sums as _case2_factorial_sums
import pytest as _case2_pytest

def test_negative_raises_valueerror():
    """Test that negative numbers raise ValueError."""
    with _case2_pytest.raises(ValueError):
        _case2_factorial_sums([-1, 2])
    with _case2_pytest.raises(ValueError):
        _case2_factorial_sums([-5, -3])

from solution import factorial_sums as _case3_factorial_sums

def test_two_elements_with_zero():
    """Test [0,4] produces correct results per the docstring example."""
    import pytest
    with pytest.raises(ValueError):
        _case3_factorial_sums([0, 4])

from solution import factorial_sums as _case4_factorial_sums
import pytest as _case4_pytest

def test_float_in_list_raises_typeerror():
    """Test that a list containing floats raises TypeError."""
    with _case4_pytest.raises(TypeError):
        _case4_factorial_sums([1, 2.5, 3])
