# Accepted by submit_tests; explanations in testgen_report.json.

def test_add_item_basic():
    """Verify that adding an item stores it correctly with given price and quantity."""
    from solution import ShoppingCart
    cart = ShoppingCart()
    cart.add_item('apple', 1.5, 5)
    result = cart.view_items()
    assert isinstance(result, dict)
    assert 'apple' in result
    assert result['apple']['price'] == 1.5
    assert result['apple']['quantity'] == 5

def test_add_item_default_quantity():
    """Verify that omitting quantity defaults to 1."""
    from solution import ShoppingCart
    cart = ShoppingCart()
    cart.add_item('banana', 2.0)
    result = cart.view_items()
    assert result['banana']['quantity'] == 1
    assert result['banana']['price'] == 2.0

def test_add_item_overwrite():
    """Adding the same item twice should overwrite, not accumulate quantity."""
    from solution import ShoppingCart
    cart = ShoppingCart()
    cart.add_item('apple', 1.0, 3)
    cart.add_item('apple', 2.0, 5)
    result = cart.view_items()
    assert result['apple']['price'] == 2.0
    assert result['apple']['quantity'] == 5
    assert len(result) == 1

def test_remove_item_reduces_quantity():
    """Removing a quantity should subtract from existing quantity."""
    from solution import ShoppingCart
    cart = ShoppingCart()
    cart.add_item('apple', 1.0, 5)
    cart.remove_item('apple', 3)
    result = cart.view_items()
    assert result['apple']['quantity'] == 2
    assert result['apple']['price'] == 1.0

def test_remove_item_nonexistent_no_error():
    """Removing a non-existent item should not raise an error."""
    from solution import ShoppingCart
    cart = ShoppingCart()
    cart.add_item('apple', 1.0, 3)
    cart.remove_item('orange', 1)
    result = cart.view_items()
    assert 'orange' not in result
    assert 'apple' in result
    assert result['apple']['quantity'] == 3

def test_total_price_empty_cart():
    """Total price of an empty cart should be 0."""
    from solution import ShoppingCart
    cart = ShoppingCart()
    total = cart.total_price()
    assert total == 0

def test_total_price_single_item():
    """Total price equals quantity * price for a single item."""
    from solution import ShoppingCart
    cart = ShoppingCart()
    cart.add_item('apple', 2.5, 4)
    total = cart.total_price()
    assert total == 10.0

def test_total_price_multiple_items():
    """Total price sums across multiple items correctly."""
    from solution import ShoppingCart
    cart = ShoppingCart()
    cart.add_item('apple', 1.0, 5)
    cart.add_item('banana', 2.0, 3)
    total = cart.total_price()
    assert total == 11.0

def test_remove_item_negative_quantity():
    """Removing more than available produces negative quantity (no guard in implementation)."""
    from solution import ShoppingCart
    cart = ShoppingCart()
    cart.add_item('apple', 1.0, 2)
    cart.remove_item('apple', 5)
    result = cart.view_items()
    assert result['apple']['quantity'] == -3
    assert 'apple' in result

def test_view_items_returns_dict():
    """view_items returns a dict with correct structure."""
    from solution import ShoppingCart
    cart = ShoppingCart()
    cart.add_item('cherry', 3.0, 2)
    result = cart.view_items()
    assert isinstance(result, dict)
    assert len(result) == 1
    assert 'cherry' in result
    inner = result['cherry']
    assert isinstance(inner, dict)
    assert 'price' in inner
    assert 'quantity' in inner

def test_add_then_remove_then_total():
    """After adding and removing, total reflects remaining quantity."""
    from solution import ShoppingCart
    cart = ShoppingCart()
    cart.add_item('milk', 4.0, 10)
    cart.remove_item('milk', 7)
    total = cart.total_price()
    assert total == 12.0
