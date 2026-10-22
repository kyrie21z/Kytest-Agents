# Accepted by submit_tests; explanations in testgen_report.json.

# Accepted by submit_tests; explanations in testgen_report.json.

"""Test adding a new product to empty inventory."""
from solution import Warehouse as _case0_Warehouse

def test_add_new_product():
    wh = _case0_Warehouse()
    wh.add_product(1, 'Apple', 10)
    assert wh.inventory[1]['name'] == 'Apple'
    assert wh.inventory[1]['quantity'] == 10
    assert len(wh.inventory) == 1

"""Adding same product_id should increase quantity by given amount."""
from solution import Warehouse as _case1_Warehouse

def test_add_existing_increments_quantity():
    wh = _case1_Warehouse()
    wh.add_product(1, 'Apple', 5)
    wh.add_product(1, 'Apple', 3)
    assert wh.inventory[1]['quantity'] == 8
    assert wh.inventory[1]['name'] == 'Apple'

"""Quote: 'return False otherwise' for missing product_id."""
from solution import Warehouse as _case2_Warehouse

def test_get_product_quantity_missing_returns_false():
    wh = _case2_Warehouse()
    result = wh.get_product_quantity(999)
    assert result is False
    assert type(result) is bool

"""Quote: 'return False: only if ... the quantity is not adequate'"""
from solution import Warehouse as _case3_Warehouse

def test_create_order_fails_insufficient_stock():
    wh = _case3_Warehouse()
    wh.add_product(1, 'Apple', 5)
    result = wh.create_order(1, 1, 10)
    assert result is False
    assert wh.inventory[1]['quantity'] == 5
    assert len(wh.orders) == 0


"""Quote: 'add the quantity to the corresponding product in inventory.'"""
from solution import Warehouse as _newf32b24be0__case4_Warehouse

def test_update_product_quantity_success():
    wh = _newf32b24be0__case4_Warehouse()
    wh.add_product(1, 'Widget', 10)
    wh.update_product_quantity(1, 5)
    assert wh.inventory[1]['quantity'] == 15
    assert wh.inventory[1]['name'] == 'Widget'

"""Quote: 'if the product_id is in inventory then return the corresponding quantity'"""
from solution import Warehouse as _newf32b24be1__case5_Warehouse

def test_get_product_quantity_present():
    wh = _newf32b24be1__case5_Warehouse()
    wh.add_product(42, 'Gadget', 7)
    result = wh.get_product_quantity(42)
    assert result == 7
    assert type(result) is int

"""Quote: 'The default value of status is Shipped' and 'put the new order into self.orders.'"""
from solution import Warehouse as _newf32b24be2__case6_Warehouse

def test_create_order_success():
    wh = _newf32b24be2__case6_Warehouse()
    wh.add_product(1, 'Widget', 10)
    result = wh.create_order(100, 1, 3)
    assert result is None
    assert len(wh.orders) == 1
    assert 100 in wh.orders
    assert wh.orders[100]['product_id'] == 1
    assert wh.orders[100]['quantity'] == 3
    assert wh.orders[100]['status'] == 'Shipped'
    assert wh.inventory[1]['quantity'] == 7

"""Quote: 'Change the status of order if the input order_id is in self.orders.'"""
from solution import Warehouse as _newf32b24be3__case7_Warehouse

def test_change_order_status_success():
    wh = _newf32b24be3__case7_Warehouse()
    wh.add_product(1, 'Widget', 10)
    wh.create_order(100, 1, 3)
    result = wh.change_order_status(100, 'Delivered')
    assert result is None
    assert wh.orders[100]['status'] == 'Delivered'

"""Quote: 'Get the status of specific order.'"""
from solution import Warehouse as _newf32b24be4__case8_Warehouse

def test_track_order_success():
    wh = _newf32b24be4__case8_Warehouse()
    wh.add_product(1, 'Widget', 10)
    wh.create_order(200, 1, 5)
    status = wh.track_order(200)
    assert status == 'Shipped'
    assert type(status) is str
