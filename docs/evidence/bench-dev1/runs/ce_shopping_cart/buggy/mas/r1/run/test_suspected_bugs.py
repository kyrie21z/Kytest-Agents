# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

from solution import ShoppingCart

def test_p3_total_price_multiple_items():
    """P3: Calculate total price across multiple items.

    Docstring quote: 'Calculate the total price of all items in the shopping list, which is the quantity of each item multiplied by the price' / example: 11.0
    Input domain: cart with add_item('a', 1.0, 5) then add_item('b', 2.0, 3).
    Oracle: total_price() == 11.0  (1*5 + 2*3 = 11).
    Fault hypothesis: implementation forgets to multiply by quantity (only sums prices).
    """
    cart = ShoppingCart()
    cart.add_item("a", 1.0, 5)
    cart.add_item("b", 2.0, 3)
    assert cart.total_price() == 11.0

from solution import ShoppingCart

def test_p8_total_with_zero_qty():
    """P8: Total price arithmetic consistency with zero-quantity items.

    Docstring quote: 'the quantity of each item multiplied by the price'.
    Input domain: add_item('a', 5.0, 0) then add_item('b', 2.0, 3).
    Oracle: total_price() == 6.0  ((0*5)+(3*2) = 6).
    Fault hypothesis: ignores quantity entirely (would return 7.0 = 5+2).
    """
    cart = ShoppingCart()
    cart.add_item("a", 5.0, 0)
    cart.add_item("b", 2.0, 3)
    assert cart.total_price() == 6.0
