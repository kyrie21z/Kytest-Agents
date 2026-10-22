# Accepted by submit_tests; explanations in testgen_report.json.

from solution import ShoppingCart as _case0_ShoppingCart

def test_p1_default_quantity():
    """P1: Add single item using default quantity.

    Docstring quote: 'The default quantity is 1'
    Input domain: new cart, add_item called with two positional args (item, price).
    Oracle: view_items must contain the item with price as given and quantity=1.
    Fault hypothesis: if quantity defaults to something other than 1 or is omitted,
    the assertion will catch it.
    """
    cart = _case0_ShoppingCart()
    cart.add_item('apple', 1.5)
    result = cart.view_items()
    assert isinstance(result, dict)
    assert 'apple' in result
    assert result['apple']['price'] == 1.5
    assert result['apple']['quantity'] == 1

from solution import ShoppingCart as _case1_ShoppingCart

def test_p2_explicit_quantity_float_price():
    """P2: Add item with explicit quantity and float price.

    Docstring quote: ':param price: float, The price of the item' / ':param quantity:int'
    Input domain: new cart, add_item('banana', 2.5, 4).
    Oracle: view_items must store the exact price and quantity provided.
    Fault hypothesis: wrong key names ('Price', 'Qty') or swapped values.
    """
    cart = _case1_ShoppingCart()
    cart.add_item('banana', 2.5, 4)
    result = cart.view_items()
    assert isinstance(result, dict)
    assert 'banana' in result
    assert result['banana']['price'] == 2.5
    assert result['banana']['quantity'] == 4

from solution import ShoppingCart as _case2_ShoppingCart

def test_p4_partial_remove():
    """P4: Partially remove item quantity.

    Docstring quote: 'Subtract the specified quantity of item from the shopping list items'
    Input domain: add_item('apple', 1.0, 5) then remove_item('apple', 3).
    Oracle: view_items() == {"apple": {"price": 1.0, "quantity": 2}}.
    Fault hypothesis: remove_item does not decrement quantity or uses wrong initial qty.
    """
    cart = _case2_ShoppingCart()
    cart.add_item('apple', 1.0, 5)
    cart.remove_item('apple', 3)
    result = cart.view_items()
    assert isinstance(result, dict)
    assert 'apple' in result
    assert result['apple']['price'] == 1.0
    assert result['apple']['quantity'] == 2

from solution import ShoppingCart as _case3_ShoppingCart

def test_p5_empty_cart_total():
    """P5: Calculate total price on empty cart.

    Docstring quote: 'Calculate the total price of all items in the shopping list'.
    Input domain: brand-new ShoppingCart(), call total_price().
    Oracle: 0.0 (sum over empty collection).
    Fault hypothesis: raises exception or returns non-zero on empty cart.
    """
    cart = _case3_ShoppingCart()
    assert cart.total_price() == 0.0

from solution import ShoppingCart as _case4_ShoppingCart

def test_p6_sequential_modifications():
    """P6: View items reflects sequential modifications.

    Docstring quote: 'Return the current shopping list items'.
    Input domain: add_item('x', 10.0, 2), remove_item('x', 1), view_items().
    Oracle: {"x": {"price": 10.0, "quantity": 1}}.
    Fault hypothesis: view_items returns stale data or remove_item corrupts state.
    """
    cart = _case4_ShoppingCart()
    cart.add_item('x', 10.0, 2)
    cart.remove_item('x', 1)
    result = cart.view_items()
    assert isinstance(result, dict)
    assert 'x' in result
    assert result['x']['price'] == 10.0
    assert result['x']['quantity'] == 1

from solution import ShoppingCart as _case5_ShoppingCart

def test_p7_zero_quantity():
    """P7: Add item with zero quantity.

    Docstring quote: ':param quantity:int, The number of items, defaults to 1'.
    No explicit lower-bound precondition stated; zero is a valid integer.
    Input domain: add_item('water', 1.0, 0).
    Oracle: view_items() == {'water': {'price': 1.0, 'quantity': 0}}.
    Fault hypothesis: silently drops zero-quantity items or raises ValueError.
    """
    cart = _case5_ShoppingCart()
    cart.add_item('water', 1.0, 0)
    result = cart.view_items()
    assert isinstance(result, dict)
    assert 'water' in result
    assert result['water']['price'] == 1.0
    assert result['water']['quantity'] == 0
