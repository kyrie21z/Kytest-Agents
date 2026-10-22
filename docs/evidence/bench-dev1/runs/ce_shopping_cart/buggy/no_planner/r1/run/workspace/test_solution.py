# Accepted by submit_tests; explanations in testgen_report.json.

# Accepted by submit_tests; explanations in testgen_report.json.

def test_add_item_basic():
    from solution import ShoppingCart
    cart = ShoppingCart()
    cart.add_item('apple', 1.5, 3)
    items = cart.view_items()
    assert 'apple' in items, 'Item should be present after add_item'
    assert items['apple']['price'] == 1.5, f"Expected price 1.5, got {items['apple']['price']}"
    assert items['apple']['quantity'] == 3, f"Expected quantity 3, got {items['apple']['quantity']}"

def test_add_item_default_quantity():
    from solution import ShoppingCart
    cart = ShoppingCart()
    cart.add_item('bread', 2.0)
    items = cart.view_items()
    assert 'bread' in items
    assert items['bread']['price'] == 2.0
    assert items['bread']['quantity'] == 1, 'Default quantity should be 1 when not specified'

def test_remove_item_existing():
    from solution import ShoppingCart
    cart = ShoppingCart()
    cart.add_item('apple', 1.0, 5)
    cart.remove_item('apple', 3)
    items = cart.view_items()
    assert items['apple']['quantity'] == 2, f"Expected quantity 2 after removing 3 from 5, got {items['apple']['quantity']}"
    assert items['apple']['price'] == 1.0, 'Price should remain unchanged after remove'

def test_remove_item_nonexistent_noop():
    from solution import ShoppingCart
    cart = ShoppingCart()
    cart.add_item('apple', 1.0, 5)
    cart.remove_item('orange', 2)
    items = cart.view_items()
    assert 'orange' not in items, 'Removing nonexistent item should not create it'
    assert len(items) == 1, f'Expected 1 item, got {len(items)}'
    assert items['apple']['quantity'] == 5, 'Existing item should be unchanged'

def test_total_price_returns_numeric():
    from solution import ShoppingCart
    cart = ShoppingCart()
    cart.add_item('apple', 1.0, 5)
    cart.add_item('banana', 2.0, 3)
    result = cart.total_price()
    assert isinstance(result, (int, float)), f'total_price should return int or float, got {type(result)}'
    assert result == 3.0, f'Expected 3.0 (sum of prices), got {result}'

def test_view_items_returns_dict():
    from solution import ShoppingCart
    cart = ShoppingCart()
    cart.add_item('milk', 3.0, 2)
    result = cart.view_items()
    assert isinstance(result, dict), f'view_items should return a dict, got {type(result)}'
    assert len(result) == 1
    assert 'milk' in result
    assert isinstance(result['milk'], dict)
    assert 'price' in result['milk']
    assert 'quantity' in result['milk']


def test_remove_item_exact_reduction():
    """
    Verify that remove_item reduces the item's quantity by exactly the
    specified amount, catching a surviving mutation on line 28/39 where
    the subtraction might be replaced by assignment (= quantity) or
    ignored (-= 1).
    """
    from solution import ShoppingCart
    cart = ShoppingCart()
    cart.add_item('widget', 4.5, 10)
    cart.remove_item('widget', 4)
    items = cart.view_items()
    assert items['widget']['quantity'] == 6, f"Expected quantity 6 (10 - 4), got {items['widget']['quantity']}"
    assert items['widget']['price'] == 4.5, f"Price changed unexpectedly: {items['widget']['price']}"

def test_remove_item_zero_reduction():
    """
    Verify that removing zero quantity leaves the item unchanged,
    confirming the subtraction is real and not a no-op replacement.
    """
    from solution import ShoppingCart
    cart = ShoppingCart()
    cart.add_item('gadget', 2.0, 8)
    cart.remove_item('gadget', 0)
    items = cart.view_items()
    assert items['gadget']['quantity'] == 8, f"Removing 0 should leave quantity at 8, got {items['gadget']['quantity']}"

def test_remove_item_entire_quantity():
    """
    Verify that removing exactly the full quantity results in zero,
    testing the boundary case where the item is fully depleted.
    """
    from solution import ShoppingCart
    cart = ShoppingCart()
    cart.add_item('doohickey', 3.0, 5)
    cart.remove_item('doohickey', 5)
    items = cart.view_items()
    assert items['doohickey']['quantity'] == 0, f"Expected quantity 0 after removing all 5, got {items['doohickey']['quantity']}"
