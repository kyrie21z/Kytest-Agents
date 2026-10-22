# Accepted by submit_tests; explanations in testgen_report.json.

def test_add_product_accumulates_quantity():
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'widget', 3)
    w.add_product(1, 'widget', 7)
    assert w.inventory[1]['quantity'] == 10
    assert w.inventory[1]['name'] == 'widget'

def test_get_product_quantity_returns_false_for_missing():
    from solution import Warehouse
    w = Warehouse()
    result = w.get_product_quantity(999)
    assert result is False

def test_create_order_deducts_inventory():
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'widget', 20)
    w.create_order(100, 1, 7)
    assert w.inventory[1]['quantity'] == 13
    assert w.orders[100]['status'] == 'Shipped'
    assert w.orders[100]['product_id'] == 1
    assert w.orders[100]['quantity'] == 7

def test_create_order_fails_on_insufficient_stock():
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'widget', 3)
    result = w.create_order(100, 1, 10)
    assert result is False
    assert 100 not in w.orders
    assert w.inventory[1]['quantity'] == 3

def test_change_order_status_and_track():
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'widget', 5)
    w.create_order(1, 1, 2)
    w.change_order_status(1, 'delivered')
    assert w.track_order(1) == 'delivered'
    result = w.change_order_status(999, 'done')
    assert result is False
    assert w.track_order(999) is False

def test_add_product_creates_entry():
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'widget', 5)
    assert 1 in w.inventory
    assert w.inventory[1]['name'] == 'widget'
    assert w.inventory[1]['quantity'] == 5

def test_update_product_quantity_negative():
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'widget', 10)
    w.update_product_quantity(1, -3)
    assert w.inventory[1]['quantity'] == 7

def test_get_product_quantity_returns_actual_value():
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'widget', 0)
    result = w.get_product_quantity(1)
    assert result == 0
    assert isinstance(result, int)

def test_update_nonexistent_product_no_effect():
    from solution import Warehouse
    w = Warehouse()
    w.update_product_quantity(999, 5)
    assert 999 not in w.inventory

def test_create_order_with_nonexistent_product():
    from solution import Warehouse
    w = Warehouse()
    result = w.create_order(100, 999, 5)
    assert result is False
    assert 100 not in w.orders

def test_track_order_returns_shipped_by_default():
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'widget', 10)
    w.create_order(1, 1, 3)
    status = w.track_order(1)
    assert status == 'Shipped'
    assert isinstance(status, str)

def test_create_order_exact_quantity():
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'widget', 5)
    result = w.create_order(1, 1, 5)
    assert result is None
    assert w.inventory[1]['quantity'] == 0
    assert 1 in w.orders

def test_change_then_track_reflects_update():
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'widget', 5)
    w.create_order(1, 1, 2)
    w.change_order_status(1, 'delivered')
    assert w.track_order(1) == 'delivered'
    w.change_order_status(1, 'cancelled')
    assert w.track_order(1) == 'cancelled'
