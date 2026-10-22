# Accepted by submit_tests; explanations in testgen_report.json.

"""P1: Add item with default quantity."""
from solution import ShoppingCart as _case0_ShoppingCart

def test_p1_default_quantity():
    cart = _case0_ShoppingCart()
    cart.add_item('apple', 1.5)
    result = cart.view_items()
    assert result == {'apple': {'price': 1.5, 'quantity': 1}}

"""P2: Add item with explicit quantity."""
from solution import ShoppingCart as _case1_ShoppingCart

def test_p2_explicit_quantity():
    cart = _case1_ShoppingCart()
    cart.add_item('banana', 2.0, 3)
    result = cart.view_items()
    assert result == {'banana': {'price': 2.0, 'quantity': 3}}

"""P3: Remove partial quantity."""
from solution import ShoppingCart as _case2_ShoppingCart

def test_p3_remove_partial():
    cart = _case2_ShoppingCart()
    cart.add_item('cherry', 5.0, 10)
    cart.remove_item('cherry', 4)
    result = cart.view_items()
    assert result == {'cherry': {'price': 5.0, 'quantity': 6}}

"""P4: Calculate total price with multiple items."""
from solution import ShoppingCart as _case3_ShoppingCart

def test_p4_total_price_multiple():
    cart = _case3_ShoppingCart()
    cart.add_item('a', 1.0, 2)
    cart.add_item('b', 3.0, 4)
    result = cart.total_price()
    assert result == 14.0

"""P5: View and total on empty cart."""
from solution import ShoppingCart as _case4_ShoppingCart

def test_p5_empty_cart():
    cart = _case4_ShoppingCart()
    assert cart.view_items() == {}
    assert cart.total_price() == 0.0

"""P6: State consistency across mutation sequence."""
from solution import ShoppingCart as _case5_ShoppingCart

def test_p6_state_consistency():
    cart = _case5_ShoppingCart()
    cart.add_item('x', 10.0, 5)
    cart.remove_item('x', 2)
    result = cart.view_items()
    assert result == {'x': {'price': 10.0, 'quantity': 3}}

"""P7: Add item with zero quantity."""
from solution import ShoppingCart as _case6_ShoppingCart

def test_p7_zero_quantity():
    cart = _case6_ShoppingCart()
    cart.add_item('zero_qty', 9.99, 0)
    result = cart.view_items()
    assert result == {'zero_qty': {'price': 9.99, 'quantity': 0}}

"""P8: Remove exact remaining quantity."""
from solution import ShoppingCart as _case7_ShoppingCart

def test_p8_remove_exact():
    cart = _case7_ShoppingCart()
    cart.add_item('exact', 5.0, 1)
    cart.remove_item('exact', 1)
    result = cart.view_items()
    assert result == {'exact': {'price': 5.0, 'quantity': 0}}

"""P10: Update existing item price and quantity."""
from solution import ShoppingCart as _case8_ShoppingCart

def test_p10_update_existing():
    cart = _case8_ShoppingCart()
    cart.add_item('dup', 10.0, 2)
    cart.add_item('dup', 15.0, 4)
    result = cart.view_items()
    assert result == {'dup': {'price': 15.0, 'quantity': 4}}

"""P9: Total price returns float type."""
from solution import ShoppingCart as _case9_ShoppingCart

def test_p9_float_return_type():
    cart = _case9_ShoppingCart()
    cart.add_item('float_test', 0.1, 1)
    result = cart.total_price()
    assert isinstance(result, float)
