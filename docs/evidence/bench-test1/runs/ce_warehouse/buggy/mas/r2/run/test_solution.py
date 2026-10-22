# Accepted by submit_tests; explanations in testgen_report.json.

"""Test P1: Add a new product to inventory."""
from solution import Warehouse as _case0_Warehouse

def test_p1_new_product():
    warehouse = _case0_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    assert warehouse.inventory == {1: {'name': 'Widget', 'quantity': 10}}

"""Test P3: Update quantity with a negative decrement."""
from solution import Warehouse as _case1_Warehouse

def test_p3_negative_decrement():
    warehouse = _case1_Warehouse()
    warehouse.add_product(1, 'Widget', 15)
    warehouse.update_product_quantity(1, -3)
    assert warehouse.inventory[1]['quantity'] == 12

"""Test P4: Retrieve quantity for a non-existent product."""
from solution import Warehouse as _case2_Warehouse

def test_p4_nonexistent_product():
    warehouse = _case2_Warehouse()
    result = warehouse.get_product_quantity(99)
    assert result is False

"""Test P5: Create an order with adequate stock."""
from solution import Warehouse as _case3_Warehouse

def test_p5_create_order_adequate_stock():
    warehouse = _case3_Warehouse()
    warehouse.add_product(1, 'product1', 10)
    warehouse.create_order(101, 1, 5)
    assert warehouse.orders == {101: {'product_id': 1, 'quantity': 5, 'status': 'Shipped'}}

"""Test P6: Create an order with inadequate stock."""
from solution import Warehouse as _case4_Warehouse

def test_p6_create_order_inadequate_stock():
    warehouse = _case4_Warehouse()
    warehouse.add_product(1, 'product1', 10)
    result = warehouse.create_order(102, 1, 100)
    assert result is False

"""Test P7: Change status of an existing order."""
from solution import Warehouse as _case5_Warehouse

def test_p7_change_order_status():
    warehouse = _case5_Warehouse()
    warehouse.add_product(1, 'product1', 10)
    warehouse.create_order(101, 1, 5)
    warehouse.change_order_status(101, 'Delivered')
    assert warehouse.orders[101]['status'] == 'Delivered'

"""Test P8: Track a non-existent order."""
from solution import Warehouse as _case6_Warehouse

def test_p8_track_nonexistent_order():
    warehouse = _case6_Warehouse()
    result = warehouse.track_order(999)
    assert result is False

"""Extra: Track an existing order returns its status string."""
from solution import Warehouse as _case7_Warehouse

def test_extra_track_existing_order():
    warehouse = _case7_Warehouse()
    warehouse.add_product(1, 'product1', 10)
    warehouse.create_order(101, 1, 5)
    result = warehouse.track_order(101)
    assert result == 'Shipped'

"""Extra: Updating quantity of a non-existent product should be a no-op."""
from solution import Warehouse as _case8_Warehouse

def test_extra_update_nonexistent_product():
    warehouse = _case8_Warehouse()
    warehouse.update_product_quantity(99, 5)
    assert 99 not in warehouse.inventory

"""Extra: Get quantity of an existing product returns the integer quantity."""
from solution import Warehouse as _case9_Warehouse

def test_extra_get_existing_product():
    warehouse = _case9_Warehouse()
    warehouse.add_product(1, 'Widget', 7)
    result = warehouse.get_product_quantity(1)
    assert result == 7
    assert isinstance(result, int)
