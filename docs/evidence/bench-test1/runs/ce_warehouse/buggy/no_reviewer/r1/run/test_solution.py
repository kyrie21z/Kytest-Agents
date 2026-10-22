# Accepted by submit_tests; explanations in testgen_report.json.

"""Add a new product to inventory."""
from solution import Warehouse as _case0_Warehouse

def test_p1_add_new_product():
    """
    Add a new product to inventory.
    Docstring quote: "Add product to inventory and plus the quantity if it has
      existed in inventory. Or just add new product to dict otherwise."
    Input domain: warehouse.add_product(1, 'A', 10) on empty warehouse.
    Expected: warehouse.inventory == {1: {'name': 'A', 'quantity': 10}}
    Fault hypothesis: New product is not added or stored with wrong name/quantity.
    """
    wh = _case0_Warehouse()
    wh.add_product(1, 'A', 10)
    assert wh.inventory == {1: {'name': 'A', 'quantity': 10}}

"""Decrease product quantity using negative update."""
from solution import Warehouse as _case1_Warehouse

def test_p3_decrease_quantity_negative():
    """
    Decrease product quantity using negative update.
    Docstring quote: example shows update_product_quantity(1, -1) reduces quantity.
    Input domain: add_product(1,'A',5); update_product_quantity(1, -2).
    Expected: warehouse.inventory[1]['quantity'] == 3
    Fault hypothesis: Negative update does not decrease quantity correctly.
    """
    wh = _case1_Warehouse()
    wh.add_product(1, 'A', 5)
    wh.update_product_quantity(1, -2)
    assert wh.inventory[1]['quantity'] == 3

"""Retrieve quantity for missing product returns False."""
from solution import Warehouse as _case2_Warehouse

def test_p4_get_missing_product():
    """
    Retrieve quantity for missing product returns False.
    Docstring quote: "if the product_id is in inventory then return the
      corresponding quantity, or False otherwise."
    Input domain: get_product_quantity(99) on empty warehouse.
    Expected: result is False (not None, not 0, not KeyError).
    Fault hypothesis: Returns None, raises KeyError, or returns 0 instead of False.
    """
    wh = _case2_Warehouse()
    result = wh.get_product_quantity(99)
    assert result is False

"""Create order with sufficient inventory."""
from solution import Warehouse as _case3_Warehouse

def test_p5_create_order_sufficient_inventory():
    """
    Create order with sufficient inventory.
    Docstring quote: default value of status is 'Shipped'.
    Input domain: add_product(1,'A',10); create_order(101, 1, 5).
    Expected: warehouse.orders == {101: {'product_id': 1, 'quantity': 5, 'status': 'Shipped'}}
    Fault hypothesis: Order not created, status not 'Shipped', or fields incorrect.
    """
    wh = _case3_Warehouse()
    wh.add_product(1, 'A', 10)
    wh.create_order(101, 1, 5)
    assert wh.orders == {101: {'product_id': 1, 'quantity': 5, 'status': 'Shipped'}}

"""Create order with insufficient inventory returns False."""
from solution import Warehouse as _case4_Warehouse

def test_p6_create_order_insufficient_inventory():
    """
    Create order with insufficient inventory returns False.
    Docstring quote: ":return False: only if product_id is not in inventory
      or the quantity is not adequate"
    Input domain: add_product(1,'A',2); create_order(102, 1, 5).
    Expected: result is False.
    Fault hypothesis: Returns True/order created despite insufficient stock.
    """
    wh = _case4_Warehouse()
    wh.add_product(1, 'A', 2)
    result = wh.create_order(102, 1, 5)
    assert result is False
