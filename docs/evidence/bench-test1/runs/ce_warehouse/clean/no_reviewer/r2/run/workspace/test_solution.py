# Accepted by submit_tests; explanations in testgen_report.json.

from solution import Warehouse as _case0_Warehouse

def test_p1_add_new_product():
    """Add a new product to inventory."""
    warehouse = _case0_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    assert warehouse.inventory == {1: {'name': 'Widget', 'quantity': 10}}

from solution import Warehouse as _case1_Warehouse

def test_p2_accumulate_quantity():
    """Accumulate quantity when adding an existing product."""
    warehouse = _case1_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    warehouse.add_product(1, 'Widget', 5)
    assert warehouse.inventory[1]['quantity'] == 15

from solution import Warehouse as _case2_Warehouse

def test_p3_negative_update():
    """Update product quantity with a negative value."""
    warehouse = _case2_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    warehouse.update_product_quantity(1, -3)
    assert warehouse.inventory[1]['quantity'] == 7

from solution import Warehouse as _case3_Warehouse

def test_p4_zero_quantity():
    """Initialize product with zero quantity."""
    warehouse = _case3_Warehouse()
    warehouse.add_product(2, 'EmptyBox', 0)
    assert warehouse.inventory[2]['quantity'] == 0

from solution import Warehouse as _case4_Warehouse

def test_p5_nonexistent_product():
    """Retrieve quantity for a non-existent product."""
    warehouse = _case4_Warehouse()
    result = warehouse.get_product_quantity(999)
    assert result is False

from solution import Warehouse as _case5_Warehouse

def test_p6_exceed_inventory():
    """Create an order exceeding available inventory."""
    warehouse = _case5_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    result = warehouse.create_order(102, 1, 11)
    assert result is False

from solution import Warehouse as _case6_Warehouse

def test_p7_change_order_status():
    """Change status of an existing order."""
    warehouse = _case6_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    warehouse.create_order(101, 1, 5)
    warehouse.change_order_status(101, 'Delivered')
    assert warehouse.orders[101]['status'] == 'Delivered'

from solution import Warehouse as _case7_Warehouse

def test_extra_create_order_success():
    """Create a valid order and verify inventory deduction."""
    warehouse = _case7_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    result = warehouse.create_order(200, 1, 3)
    assert result is None
    assert warehouse.orders[200] == {'product_id': 1, 'quantity': 3, 'status': 'Shipped'}
    assert warehouse.inventory[1]['quantity'] == 7

from solution import Warehouse as _case8_Warehouse

def test_extra_get_existing_product():
    """Retrieve quantity for an existing product."""
    warehouse = _case8_Warehouse()
    warehouse.add_product(42, 'Gadget', 25)
    result = warehouse.get_product_quantity(42)
    assert result == 25

from solution import Warehouse as _case9_Warehouse

def test_extra_update_nonexistent_product():
    """Update quantity for a non-existent product should do nothing."""
    warehouse = _case9_Warehouse()
    warehouse.update_product_quantity(999, -5)
    assert 999 not in warehouse.inventory

from solution import Warehouse as _case10_Warehouse

def test_extra_track_nonexistent_order():
    """Track a non-existent order returns False."""
    warehouse = _case10_Warehouse()
    result = warehouse.track_order(999)
    assert result is False

from solution import Warehouse as _case11_Warehouse

def test_p8_track_order():
    """Track status of an existing order."""
    warehouse = _case11_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    warehouse.create_order(101, 1, 5)
    result = warehouse.track_order(101)
    assert result == 'Shipped'
