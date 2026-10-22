# Accepted by submit_tests; explanations in testgen_report.json.

from solution import Warehouse as _case0_Warehouse

def test_get_product_quantity_nonexistent():
    """Getting quantity of non-existent product returns False."""
    warehouse = _case0_Warehouse()
    result = warehouse.get_product_quantity(999)
    assert result is False

from solution import Warehouse as _case1_Warehouse

def test_create_order_decreases_inventory():
    """Creating an order should decrease inventory by the ordered quantity."""
    warehouse = _case1_Warehouse()
    warehouse.add_product(1, 'widget', 10)
    warehouse.create_order(1, 1, 3)
    assert warehouse.inventory[1]['quantity'] == 7
    assert warehouse.orders[1] == {'product_id': 1, 'quantity': 3, 'status': 'Shipped'}

from solution import Warehouse as _case2_Warehouse

def test_create_order_insufficient_quantity():
    """Ordering more than available should return False and not create order."""
    warehouse = _case2_Warehouse()
    warehouse.add_product(1, 'widget', 5)
    result = warehouse.create_order(1, 1, 10)
    assert result is False
    assert 1 not in warehouse.orders

from solution import Warehouse as _case3_Warehouse

def test_create_order_nonexistent_product():
    """Ordering a product not in inventory should return False."""
    warehouse = _case3_Warehouse()
    result = warehouse.create_order(1, 999, 5)
    assert result is False
    assert 1 not in warehouse.orders

from solution import Warehouse as _case4_Warehouse

def test_add_product_creates_entry():
    """Adding a new product creates correct entry in inventory."""
    warehouse = _case4_Warehouse()
    warehouse.add_product(1, 'widget', 10)
    assert warehouse.inventory[1]['name'] == 'widget'
    assert warehouse.inventory[1]['quantity'] == 10

from solution import Warehouse as _case5_Warehouse

def test_add_product_reuses_name_on_update():
    """Re-adding same product_id only updates quantity; name stays unchanged."""
    warehouse = _case5_Warehouse()
    warehouse.add_product(1, 'original_name', 10)
    warehouse.add_product(1, 'new_name', 5)
    assert warehouse.inventory[1]['name'] == 'original_name'
    assert warehouse.inventory[1]['quantity'] == 5

from solution import Warehouse as _case6_Warehouse

def test_change_order_status_missing_returns_false():
    """Changing status of non-existent order returns False."""
    warehouse = _case6_Warehouse()
    result = warehouse.change_order_status(999, 'done')
    assert result is False

from solution import Warehouse as _case7_Warehouse

def test_track_order_default_status():
    """Tracked order has default status 'Shipped'."""
    warehouse = _case7_Warehouse()
    warehouse.add_product(1, 'widget', 10)
    warehouse.create_order(1, 1, 3)
    status = warehouse.track_order(1)
    assert status == 'Shipped'

from solution import Warehouse as _case8_Warehouse

def test_update_product_quantity_negative():
    """Negative quantity delta decreases stock."""
    warehouse = _case8_Warehouse()
    warehouse.add_product(1, 'widget', 10)
    warehouse.update_product_quantity(1, -3)
    assert warehouse.inventory[1]['quantity'] == 7

from solution import Warehouse as _case9_Warehouse

def test_update_product_quantity_nonexistent_ignored():
    """Updating quantity of non-existent product silently does nothing."""
    warehouse = _case9_Warehouse()
    warehouse.update_product_quantity(999, 5)
    assert 999 not in warehouse.inventory
