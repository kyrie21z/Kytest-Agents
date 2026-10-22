# Accepted by submit_tests; explanations in testgen_report.json.

"""P1: Add a single item with explicit quantity and verify stored state."""
from solution import ShoppingCart as _case0_ShoppingCart

def test_p1_single_item():
    cart = _case0_ShoppingCart()
    cart.add_item('apple', 1.5, 3)
    assert cart.view_items() == {'apple': {'price': 1.5, 'quantity': 3}}

"""P3: Inspect state of a newly initialized empty cart."""
from solution import ShoppingCart as _case1_ShoppingCart

def test_p3_empty_view():
    cart = _case1_ShoppingCart()
    assert cart.view_items() == {}

"""P4: Calculate total price of an empty cart."""
from solution import ShoppingCart as _case2_ShoppingCart

def test_p4_empty_total():
    cart = _case2_ShoppingCart()
    assert cart.total_price() == 0.0

"""P5: Partially remove an item and verify remaining quantity."""
from solution import ShoppingCart as _case3_ShoppingCart

def test_p5_partial_remove():
    cart = _case3_ShoppingCart()
    cart.add_item('x', 5.0, 10)
    cart.remove_item('x', 3)
    assert cart.view_items() == {'x': {'price': 5.0, 'quantity': 7}}

"""P6: Add item using default quantity parameter."""
from solution import ShoppingCart as _case4_ShoppingCart

def test_p6_default_quantity():
    cart = _case4_ShoppingCart()
    cart.add_item('y', 2.5)
    assert cart.view_items() == {'y': {'price': 2.5, 'quantity': 1}}
