# Accepted by submit_tests; explanations in testgen_report.json.

# Accepted by submit_tests; explanations in testgen_report.json.

from solution import Warehouse as _case0_Warehouse

def test_p1_new_product():
    """Register a new product in inventory with initial quantity."""
    warehouse = _case0_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    assert warehouse.inventory == {1: {'name': 'Widget', 'quantity': 10}}

from solution import Warehouse as _case1_Warehouse

def test_p2_accumulate_quantity():
    """Accumulate quantity when adding an existing product ID."""
    warehouse = _case1_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    warehouse.add_product(1, 'Widget', 5)
    assert warehouse.inventory[1]['quantity'] == 15

from solution import Warehouse as _case2_Warehouse

def test_p3_negative_delta():
    """Adjust product quantity using a negative delta."""
    warehouse = _case2_Warehouse()
    warehouse.add_product(1, 'Widget', 15)
    warehouse.update_product_quantity(1, -3)
    assert warehouse.inventory[1]['quantity'] == 12

from solution import Warehouse as _case3_Warehouse

def test_p5_nonexistent_product():
    """Return sentinel False when querying a non-existent product."""
    warehouse = _case3_Warehouse()
    result = warehouse.get_product_quantity(999)
    assert result is False

from solution import Warehouse as _case4_Warehouse

def test_p6_create_order_success():
    """Create an order with default status when stock is sufficient."""
    warehouse = _case4_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    warehouse.create_order(101, 1, 2)
    assert warehouse.orders == {101: {'product_id': 1, 'quantity': 2, 'status': 'Shipped'}}

from solution import Warehouse as _case5_Warehouse

def test_p9_order_status_tracking():
    """Update order status and verify subsequent tracking reflects the change."""
    warehouse = _case5_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    warehouse.create_order(101, 1, 2)
    warehouse.change_order_status(101, 'Delivered')
    result = warehouse.track_order(101)
    assert result == 'Delivered'


from solution import Warehouse as _newd8dcd8fd0_Warehouse

def test_p4_existing_product_quantity():
    """Verify that get_product_quantity returns the correct integer quantity for an existing product ID."""
    warehouse = _newd8dcd8fd0_Warehouse()
    warehouse.add_product(1, 'Gadget', 7)
    result = warehouse.get_product_quantity(1)
    assert result == 7
    assert isinstance(result, int)

from solution import Warehouse as _newd8dcd8fd1_Warehouse

def test_p7_insufficient_stock():
    """Verify that create_order returns False when the requested quantity exceeds the available stock."""
    warehouse = _newd8dcd8fd1_Warehouse()
    warehouse.add_product(1, 'Gizmo', 5)
    result = warehouse.create_order(200, 1, 10)
    assert result is False
    assert warehouse.inventory[1]['quantity'] == 5
    assert 200 not in warehouse.orders

from solution import Warehouse as _newd8dcd8fd2_Warehouse

def test_p8_exact_stock_boundary():
    """Verify that create_order successfully creates the order and deducts the exact available stock when quantities match."""
    warehouse = _newd8dcd8fd2_Warehouse()
    warehouse.add_product(1, 'Thingamajig', 20)
    result = warehouse.create_order(300, 1, 20)
    assert result is None
    assert 300 in warehouse.orders
    assert warehouse.orders[300] == {'product_id': 1, 'quantity': 20, 'status': 'Shipped'}
    assert warehouse.inventory[1]['quantity'] == 0

from solution import Warehouse as _newd8dcd8fd3_Warehouse

def test_p10_zero_quantity_product():
    """Verify that add_product correctly registers a product with a zero quantity without errors."""
    warehouse = _newd8dcd8fd3_Warehouse()
    warehouse.add_product(2, 'EmptyBox', 0)
    assert 2 in warehouse.inventory
    assert warehouse.inventory[2]['name'] == 'EmptyBox'
    assert warehouse.inventory[2]['quantity'] == 0
    assert isinstance(warehouse.inventory[2]['quantity'], int)
