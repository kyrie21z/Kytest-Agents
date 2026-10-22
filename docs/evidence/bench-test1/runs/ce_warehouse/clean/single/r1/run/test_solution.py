# Accepted by submit_tests; explanations in testgen_report.json.

from solution import Warehouse as _case0_Warehouse

def test_add_product_creates_entry():
    """Test that add_product correctly creates a new product entry in inventory."""
    warehouse = _case0_Warehouse()
    warehouse.add_product(1, 'widget', 5)
    assert 1 in warehouse.inventory
    assert warehouse.inventory[1]['name'] == 'widget'
    assert warehouse.inventory[1]['quantity'] == 5

from solution import Warehouse as _case1_Warehouse

def test_add_product_accumulates_quantity():
    """Test that adding the same product_id twice accumulates the quantity."""
    warehouse = _case1_Warehouse()
    warehouse.add_product(1, 'widget', 5)
    warehouse.add_product(1, 'widget', 3)
    assert warehouse.inventory[1]['quantity'] == 8
    assert warehouse.inventory[1]['name'] == 'widget'

from solution import Warehouse as _case2_Warehouse

def test_create_order_reduces_inventory():
    """Test that a successful create_order decrements inventory and records the order."""
    warehouse = _case2_Warehouse()
    warehouse.add_product(1, 'widget', 10)
    result = warehouse.create_order(100, 1, 3)
    assert result is None
    assert warehouse.inventory[1]['quantity'] == 7
    assert 100 in warehouse.orders
    assert warehouse.orders[100] == {'product_id': 1, 'quantity': 3, 'status': 'Shipped'}

from solution import Warehouse as _case3_Warehouse

def test_create_order_fails_on_insufficient_stock():
    """Test that create_order returns False when requested quantity exceeds available stock."""
    warehouse = _case3_Warehouse()
    warehouse.add_product(1, 'widget', 5)
    result = warehouse.create_order(200, 1, 10)
    assert result is False
    assert warehouse.inventory[1]['quantity'] == 5
    assert 200 not in warehouse.orders

from solution import Warehouse as _case4_Warehouse

def test_get_product_quantity_returns_false_for_missing():
    """Test that get_product_quantity returns False (not 0 or None) for a non-existent product."""
    warehouse = _case4_Warehouse()
    result = warehouse.get_product_quantity(999)
    assert result is False
    assert result is not None

from solution import Warehouse as _case5_Warehouse

def test_full_order_lifecycle():
    """Test the full lifecycle: create order, track it, change status, track again."""
    warehouse = _case5_Warehouse()
    warehouse.add_product(1, 'widget', 10)
    warehouse.create_order(1, 1, 2)
    assert warehouse.track_order(1) == 'Shipped'
    warehouse.change_order_status(1, 'delivered')
    assert warehouse.track_order(1) == 'delivered'
    assert warehouse.track_order(999) is False
    assert warehouse.change_order_status(999, 'done') is False
