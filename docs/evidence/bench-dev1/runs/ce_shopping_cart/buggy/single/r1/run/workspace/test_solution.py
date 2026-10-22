# Accepted by submit_tests; explanations in testgen_report.json.

def test_add_item_replaces_existing():
    """Test that add_item replaces the entry when item already exists."""
    from solution import ShoppingCart
    cart = ShoppingCart()
    cart.add_item('apple', 1.0, 5)
    cart.add_item('apple', 2.0, 3)
    items = cart.view_items()
    assert items['apple']['price'] == 2.0, f"Expected price 2.0, got {items['apple']['price']}"
    assert items['apple']['quantity'] == 3, f"Expected quantity 3, got {items['apple']['quantity']}"

def test_remove_item_nonexistent():
    """Test remove_item on an item that does not exist in cart."""
    from solution import ShoppingCart
    cart = ShoppingCart()
    cart.add_item('apple', 1.0, 5)
    cart.remove_item('orange', 2)
    items = cart.view_items()
    assert 'orange' not in items, f"Non-existent item 'orange' should not appear in cart"
    assert len(items) == 1, f'Cart should still have 1 item, got {len(items)}'
