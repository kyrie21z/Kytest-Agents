# Accepted by submit_tests; explanations in testgen_report.json.

# Accepted by submit_tests; explanations in testgen_report.json.

from solution import factorial_sums as _case0_factorial_sums
import pytest as _case0_pytest

def test_p5_non_list_input():
    """Test P5: Rejects non-list input."""
    with _case0_pytest.raises(TypeError):
        _case0_factorial_sums('abc')

from solution import factorial_sums as _case1_factorial_sums
import pytest as _case1_pytest

def test_p6_non_integer_elements():
    """Test P6: Rejects list containing non-integers."""
    with _case1_pytest.raises(TypeError):
        _case1_factorial_sums([1, 2.0])


from solution import factorial_sums as _new95a5b22b0__p7_factorial_sums
import pytest as _new95a5b22b0__p7_pytest

def test_p7_negative_integers():
    """Test P7: Rejects negative integers."""
    with _new95a5b22b0__p7_pytest.raises(ValueError):
        _new95a5b22b0__p7_factorial_sums([-2, 3])
