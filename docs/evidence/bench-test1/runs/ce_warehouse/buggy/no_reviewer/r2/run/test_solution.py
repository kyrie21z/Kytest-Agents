# Accepted by submit_tests; explanations in testgen_report.json.

from solution import Warehouse as _case0_Warehouse

def test_p1_add_product_new():
    """P1: add_product creates a new product entry with initial quantity.
    Docstring example: warehouse.add_product(1, "product1", 3) -> inventory == {1: {'name': 'product1', 'quantity': 3}}."""
    warehouse = _case0_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    assert warehouse.inventory == {1: {'name': 'Widget', 'quantity': 10}}

from solution import Warehouse as _case1_Warehouse

def test_p3_get_product_quantity():
    """P3: get_product_quantity returns correct quantity for existing product.
    Docstring example: warehouse.get_product_quantity(1) -> 3 after adding product with qty 3."""
    warehouse = _case1_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    assert warehouse.get_product_quantity(1) == 10

from solution import Warehouse as _case2_Warehouse

def test_p4_get_product_quantity_missing():
    """P4: get_product_quantity returns False for missing product.
    Spec: 'or False otherwise.'"""
    warehouse = _case2_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    assert warehouse.get_product_quantity(99) is False

from solution import Warehouse as _case3_Warehouse

def test_p5_create_order_default_status():
    """P5: create_order initializes order with default status 'Shipped'.
    Docstring example: warehouse.create_order(1, 1, 2) -> orders == {1: {'product_id': 1, 'quantity': 2, 'status': 'Shipped'}}."""
    warehouse = _case3_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    warehouse.create_order(101, 1, 2)
    assert warehouse.orders[101] == {'product_id': 1, 'quantity': 2, 'status': 'Shipped'}

from solution import Warehouse as _case4_Warehouse

def test_p6_create_order_nonexistent_product():
    """P6: create_order rejects non-existent product.
    Spec: 'return False: only if product_id is not in inventory'."""
    warehouse = _case4_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    result = warehouse.create_order(102, 99, 1)
    assert result is False

from solution import Warehouse as _case5_Warehouse

def test_p7_create_order_inadequate_quantity():
    """P7: create_order rejects inadequate quantity.
    Spec: 'or the quantity is not adequate'."""
    warehouse = _case5_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    result = warehouse.create_order(103, 1, 100)
    assert result is False

from solution import Warehouse as _case6_Warehouse

def test_p8_change_order_status():
    """P8: change_order_status updates status and track_order reflects change.
    Docstring examples demonstrate mutating order status and subsequently retrieving it via tracking."""
    warehouse = _case6_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    warehouse.create_order(101, 1, 2)
    warehouse.change_order_status(101, 'Delivered')
    assert warehouse.orders[101]['status'] == 'Delivered'
    assert warehouse.track_order(101) == 'Delivered'

from solution import Warehouse as _case7_Warehouse

def test_p9_update_product_quantity_negative():
    """P9: update_product_quantity adjusts stock using negative delta.
    Docstring example: warehouse.update_product_quantity(1, -1) reduces quantity by 1."""
    warehouse = _case7_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    warehouse.update_product_quantity(1, -2)
    assert warehouse.inventory[1]['quantity'] == 8

from solution import Warehouse as _case8_Warehouse

def test_p10_create_order_zero_quantity():
    """P10: create_order accepts zero quantity as a boundary value.
    Spec does not explicitly forbid zero quantity, so it should succeed."""
    warehouse = _case8_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    warehouse.create_order(104, 1, 0)
    assert warehouse.orders[104] == {'product_id': 1, 'quantity': 0, 'status': 'Shipped'}

from solution import Warehouse as _case9_Warehouse

def test_extra_track_order_missing():
    """Extra: track_order returns False for non-existent order.
    Spec: 'return False: only if the order_id is not in self.orders.'"""
    warehouse = _case9_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    warehouse.create_order(101, 1, 2)
    assert warehouse.track_order(999) is False

from solution import Warehouse as _case10_Warehouse

def test_extra_change_order_status_missing():
    """Extra: change_order_status returns False for non-existent order.
    Spec: 'return False: only if the order_id is not in self.orders'."""
    warehouse = _case10_Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    result = warehouse.change_order_status(999, 'Delivered')
    assert result is False
