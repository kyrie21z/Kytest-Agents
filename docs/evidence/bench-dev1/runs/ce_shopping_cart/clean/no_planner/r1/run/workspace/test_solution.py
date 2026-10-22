# Accepted by submit_tests; explanations in testgen_report.json.

"""Test: add_item stores item with correct price and quantity."""
from solution import ShoppingCart as _case0_ShoppingCart

def test_add_item_basic():
    """
    Contract quote: 'Add item information to the shopping list items,
    including price and quantity.'

    Input domain: new item name (str), positive float price, positive int quantity.

    Expected result: after add_item('apple', 1.5, 3), view_items() returns
    {'apple': {'price': 1.5, 'quantity': 3}}.

    Faulty behaviour detected: item not stored, or wrong price/quantity values.
    """
    cart = _case0_ShoppingCart()
    cart.add_item('apple', 1.5, 3)
    result = cart.view_items()
    assert isinstance(result, dict)
    assert 'apple' in result
    assert result['apple']['price'] == 1.5
    assert result['apple']['quantity'] == 3

"""Test: add_item overwrites existing entry instead of accumulating."""
from solution import ShoppingCart as _case1_ShoppingCart

def test_add_item_overwrites():
    """
    Contract quote: 'Add item information to the shopping list items,
    including price and quantity.'

    Input domain: same item added twice with different quantities.

    Expected result: second add_item completely replaces the first entry.
    After add_item('apple', 1, 5) then add_item('apple', 2, 3), the stored
    quantity is 3 (not 8) and price is 2 (not 1).

    Faulty behaviour detected: implementation that accumulates quantities
    across repeated add_item calls instead of replacing.
    """
    cart = _case1_ShoppingCart()
    cart.add_item('apple', 1, 5)
    cart.add_item('apple', 2, 3)
    result = cart.view_items()
    assert result['apple']['price'] == 2
    assert result['apple']['quantity'] == 3

"""Test: add_item defaults quantity to 1 when not specified."""
from solution import ShoppingCart as _case2_ShoppingCart

def test_add_item_default_quantity():
    """
    Contract quote: 'The default quantity is 1'

    Input domain: item added without specifying quantity.

    Expected result: quantity defaults to 1.

    Faulty behaviour detected: default quantity is not 1.
    """
    cart = _case2_ShoppingCart()
    cart.add_item('banana', 0.75)
    result = cart.view_items()
    assert result['banana']['quantity'] == 1
    assert result['banana']['price'] == 0.75

"""Test: remove_item correctly reduces quantity of an existing item."""
from solution import ShoppingCart as _case3_ShoppingCart

def test_remove_item_reduces_quantity():
    """
    Contract quote: 'Subtract the specified quantity of item from the shopping list items'

    Input domain: existing item with quantity greater than removal quantity.

    Expected result: quantity decreases by the removed amount.
    After add_item('apple', 1, 5) then remove_item('apple', 3), quantity is 2.

    Faulty behaviour detected: quantity unchanged or wrong subtraction.
    """
    cart = _case3_ShoppingCart()
    cart.add_item('apple', 1, 5)
    cart.remove_item('apple', 3)
    result = cart.view_items()
    assert result['apple']['quantity'] == 2

"""Test: total_price sums quantity*price for all items correctly."""
from solution import ShoppingCart as _case4_ShoppingCart

def test_total_price_multiple_items():
    """
    Contract quote: 'Calculate the total price of all items in the shopping list, which is the quantity of each item multiplied by the price'

    Input domain: two distinct items with known price x quantity products.

    Expected result: apple(1x5) + banana(2x3) = 11.0.

    Faulty behaviour detected: incorrect summation logic.
    """
    cart = _case4_ShoppingCart()
    cart.add_item('apple', 1, 5)
    cart.add_item('banana', 2, 3)
    total = cart.total_price()
    assert total == 11.0

"""Test: total_price on empty cart returns 0."""
from solution import ShoppingCart as _case5_ShoppingCart

def test_empty_cart_total_price():
    """
    Contract quote: ':return:float, the total price of all items in the shopping list'

    Input domain: cart with no items added.

    Expected result: total_price() returns 0 (the sum of an empty list).
    Note: Python's sum([]) returns int 0, not float 0.0, despite the
    return-type annotation -> float.

    Faulty behaviour detected: raises exception or returns non-zero value.
    """
    cart = _case5_ShoppingCart()
    total = cart.total_price()
    assert total == 0
