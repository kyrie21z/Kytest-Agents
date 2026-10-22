# Accepted by submit_tests; explanations in testgen_report.json.

from solution import ShoppingCart as _case0_ShoppingCart

def test_p1_add_explicit_quantity():
    """P1: Add a new item with explicit quantity."""
    cart = _case0_ShoppingCart()
    cart.add_item('apple', 1.5, 2)
    result = cart.view_items()
    assert result == {'apple': {'price': 1.5, 'quantity': 2}}

from solution import ShoppingCart as _case1_ShoppingCart

def test_p2_default_quantity():
    """P2: Add item using default quantity of 1."""
    cart = _case1_ShoppingCart()
    cart.add_item('orange', 2.0)
    result = cart.view_items()
    assert result == {'orange': {'price': 2.0, 'quantity': 1}}

from solution import ShoppingCart as _case2_ShoppingCart

def test_p5_remove_partial():
    """P5: Remove a partial quantity from an existing item."""
    cart = _case2_ShoppingCart()
    cart.add_item('apple', 1.0, 5)
    cart.remove_item('apple', 3)
    result = cart.view_items()
    assert result == {'apple': {'price': 1.0, 'quantity': 2}}

from solution import ShoppingCart as _case3_ShoppingCart

def test_p6_remove_exact_zero():
    """P6: Remove exact quantity resulting in zero stock."""
    cart = _case3_ShoppingCart()
    cart.add_item('apple', 1.0, 5)
    cart.remove_item('apple', 5)
    result = cart.view_items()
    assert result == {'apple': {'price': 1.0, 'quantity': 0}}

from solution import ShoppingCart as _case4_ShoppingCart

def test_p3_total_multiple_items_fixed():
    """P3 (corrected): Calculate total price with multiple distinct items."""
    cart = _case4_ShoppingCart()
    cart.add_item('a', 10.0, 2)
    cart.add_item('b', 5.0, 3)
    total = cart.total_price()
    assert total == 35.0

from solution import ShoppingCart as _case5_ShoppingCart

def test_p7_view_returns_dict():
    """P7: View items returns a dict reflecting added items."""
    cart = _case5_ShoppingCart()
    cart.add_item('x', 9.99, 1)
    result = cart.view_items()
    assert isinstance(result, dict)
    assert 'x' in result
    assert result['x']['price'] == 9.99
    assert result['x']['quantity'] == 1

from solution import ShoppingCart as _case6_ShoppingCart

def test_p8_price_invariant():
    """P8: Price persists across add/remove cycles."""
    cart = _case6_ShoppingCart()
    cart.add_item('milk', 3.5, 2)
    cart.remove_item('milk', 2)
    cart.add_item('milk', 3.5, 1)
    result = cart.view_items()
    assert result == {'milk': {'price': 3.5, 'quantity': 1}}

from solution import ShoppingCart as _case7_ShoppingCart

def test_extra_remove_nonexistent():
    """Extra: Remove a non-existent item does not raise."""
    cart = _case7_ShoppingCart()
    cart.add_item('apple', 1.0, 3)
    cart.remove_item('banana', 1)
    result = cart.view_items()
    assert result == {'apple': {'price': 1.0, 'quantity': 3}}

from solution import ShoppingCart as _case8_ShoppingCart

def test_extra_overwrite_item():
    """Extra: Adding same item twice overwrites price and quantity."""
    cart = _case8_ShoppingCart()
    cart.add_item('apple', 1.0, 5)
    cart.add_item('apple', 2.0, 3)
    result = cart.view_items()
    assert result == {'apple': {'price': 2.0, 'quantity': 3}}

from solution import ShoppingCart as _case9_ShoppingCart

def test_p4_empty_cart_total():
    """P4: Calculate total price on empty cart."""
    cart = _case9_ShoppingCart()
    total = cart.total_price()
    assert total == 0.0
