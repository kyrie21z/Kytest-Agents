# Accepted by submit_tests; explanations in testgen_report.json.

# Accepted by submit_tests; explanations in testgen_report.json.

def test_add_product_creates_entry():
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'widget', 5)
    assert w.inventory[1] == {'name': 'widget', 'quantity': 5}

def test_add_product_replaces_quantity_not_accumulates():
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'widget', 3)
    w.add_product(1, 'widget', 5)
    assert w.inventory[1]['quantity'] == 5

def test_update_product_quantity_positive_and_negative():
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'gadget', 10)
    w.update_product_quantity(1, 3)
    w.update_product_quantity(1, -4)
    assert w.inventory[1]['quantity'] == 9

def test_get_product_quantity_returns_false_for_missing():
    from solution import Warehouse
    w = Warehouse()
    result = w.get_product_quantity(999)
    assert result is False

def test_create_order_deducts_inventory_and_sets_shipped():
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'item', 10)
    w.create_order(100, 1, 3)
    assert w.inventory[1]['quantity'] == 7
    assert w.orders[100]['status'] == 'Shipped'
    assert w.orders[100]['product_id'] == 1
    assert w.orders[100]['quantity'] == 3

def test_create_order_fails_when_insufficient_stock():
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'scarce', 5)
    result = w.create_order(200, 1, 10)
    assert result is False
    assert w.inventory[1]['quantity'] == 5
    assert 200 not in w.orders

def test_change_order_status_updates_correctly():
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'thing', 20)
    w.create_order(1, 1, 5)
    w.change_order_status(1, 'Delivered')
    assert w.orders[1]['status'] == 'Delivered'

def test_track_order_returns_false_for_nonexistent():
    from solution import Warehouse
    w = Warehouse()
    result = w.track_order(999)
    assert result is False

def test_change_order_status_returns_false_for_missing_order():
    from solution import Warehouse
    w = Warehouse()
    result = w.change_order_status(999, 'Cancelled')
    assert result is False

def test_create_order_zero_quantity_boundary():
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'freebie', 5)
    result = w.create_order(300, 1, 0)
    assert result is not False
    assert w.orders[300]['quantity'] == 0
    assert w.inventory[1]['quantity'] == 5

def test_multiple_orders_same_product_cumulative_deduction():
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'bulk', 20)
    w.create_order(1, 1, 7)
    w.create_order(2, 1, 7)
    assert w.inventory[1]['quantity'] == 6

def test_track_order_returns_correct_status():
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'item', 10)
    w.create_order(1, 1, 3)
    assert w.track_order(1) == 'Shipped'
    w.change_order_status(1, 'Delivered')
    assert w.track_order(1) == 'Delivered'


def test_create_order_nonexistent_product_returns_false():
    """Test that create_order returns False for non-existent product_id."""
    from solution import Warehouse
    w = Warehouse()
    result = w.create_order(400, 999, 1)
    assert result is False

def test_add_product_preserves_name_on_update():
    """Test that add_product preserves the original name when updating an existing product."""
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'original_name', 3)
    w.add_product(1, 'different_name', 2)
    assert w.inventory[1]['name'] == 'original_name'

def test_create_order_exact_stock_boundary():
    """Test that create_order succeeds when requested quantity exactly equals available stock."""
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'exact', 5)
    result = w.create_order(500, 1, 5)
    assert result is not False
    assert w.orders[500]['quantity'] == 5
    assert w.inventory[1]['quantity'] == 0

def test_get_product_quantity_with_zero_stock():
    """Test that get_product_quantity returns 0 for a product with depleted stock, not False."""
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'depleted', 5)
    w.create_order(1, 1, 5)
    result = w.get_product_quantity(1)
    assert result == 0
    assert result is not False
