# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

def test_total_price_with_single_item():
    from solution import ShoppingCart
    cart = ShoppingCart()
    cart.add_item("apple", 2.5, 4)
    # Contract: total_price returns sum of (price * quantity) for all items.
    # One item: price=2.5, quantity=4 => expected = 10.0
    result = cart.total_price()
    assert isinstance(result, float), "total_price should return a float"
    assert result == 10.0, f"Expected 10.0 (2.5*4), got {result}"

def test_total_price_empty_cart():
    from solution import ShoppingCart
    cart = ShoppingCart()
    # Empty cart: no items => total should be 0.0
    result = cart.total_price()
    assert isinstance(result, float), "total_price should return a float even for empty cart"
    assert result == 0.0, f"Expected 0.0 for empty cart, got {result}"
