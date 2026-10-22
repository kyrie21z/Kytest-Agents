# Accepted by submit_tests; explanations in testgen_report.json.

# Accepted by submit_tests; explanations in testgen_report.json.

from solution import Warehouse as _case0_Warehouse

def test_add_product_duplicate_accumulates():
    """
    Contract quote: 'plus the quantity if it has existed in inventory'
    Input domain: product_id=42, name='gadget', first qty=3, second qty=5
    Expected result: Two add_product calls for same id yield total quantity 8.
    Fault hypothesis: If the else-branch that accumulates is broken, quantity stays at 3.
    """
    w = _case0_Warehouse()
    w.add_product(42, 'gadget', 3)
    w.add_product(42, 'gadget', 5)
    assert w.get_product_quantity(42) == 8

from solution import Warehouse as _case1_Warehouse

def test_get_product_quantity_missing_returns_false():
    """
    Contract quote: 'or False otherwise'
    Input domain: product_id=999 does not exist in inventory
    Expected result: get_product_quantity(999) returns False (boolean).
    Fault hypothesis: Returning None instead of False, or raising KeyError, would fail.
    """
    w = _case1_Warehouse()
    result = w.get_product_quantity(999)
    assert result is False
    assert isinstance(result, bool)

from solution import Warehouse as _case2_Warehouse

def test_add_product_and_get():
    """
    Contract quote: 'Add product to inventory and plus the quantity if it has existed in inventory.'
    Input domain: product_id=1, name='widget', quantity=7
    Expected result: After adding product 1 with qty 7, get_product_quantity(1) returns 7.
    Fault hypothesis: If add_product silently fails or stores wrong quantity,
      the returned value will differ from 7.
    """
    w = _case2_Warehouse()
    w.add_product(1, 'widget', 7)
    assert w.get_product_quantity(1) == 7

from solution import Warehouse as _case3_Warehouse

def test_create_order_full_flow():
    """
    Contract quote: "The default value of status is 'Shipped'."
    Input domain: add_product(10, 'bolt', 20); create_order(100, 10, 6)
    Expected result: Order 100 created with status 'Shipped'; inventory qty drops to 14.
    Fault hypothesis: If status defaults to something other than 'Shipped',
      or inventory is not decremented, the assertions catch it.
    """
    w = _case3_Warehouse()
    w.add_product(10, 'bolt', 20)
    w.create_order(100, 10, 6)
    assert w.orders[100]['status'] == 'Shipped'
    assert w.orders[100]['product_id'] == 10
    assert w.orders[100]['quantity'] == 6
    assert w.get_product_quantity(10) == 14

from solution import Warehouse as _case4_Warehouse

def test_create_order_insufficient_quantity():
    """
    Contract quote: 'return False: only if product_id is not in inventory or the quantity is not adequate'
    Input domain: add_product(20, 'nut', 3); create_order(200, 20, 10)
    Expected result: create_order returns False; inventory unchanged at 3.
    Fault hypothesis: If the function creates the order anyway despite insufficient stock,
      the assertion on inventory quantity will fail.
    """
    w = _case4_Warehouse()
    w.add_product(20, 'nut', 3)
    result = w.create_order(200, 20, 10)
    assert result is False
    assert w.get_product_quantity(20) == 3

from solution import Warehouse as _case5_Warehouse

def test_change_order_status_and_track():
    """
    Contract quote: 'Change the status of order if the input order_id is in self.orders.'
    Input domain: add_product(30, 'screw', 10); create_order(300, 30, 4);
                  change_order_status(300, 'delivered'); track_order(300)
    Expected result: track_order(300) returns 'delivered'.
    Fault hypothesis: If change_order_status does not persist the new status,
      track_order would still return the original 'Shipped'.
    """
    w = _case5_Warehouse()
    w.add_product(30, 'screw', 10)
    w.create_order(300, 30, 4)
    w.change_order_status(300, 'delivered')
    assert w.track_order(300) == 'delivered'


from solution import Warehouse as _new2e66e4640__case6_Warehouse

def test_update_product_quantity_modifies_existing():
    """
    Contract quote: 'According to product_id, add the quantity to the corresponding
                     product in inventory.'
    Input domain: add_product(50, 'item', 10); update_product_quantity(50, 5)
    Expected result: inventory quantity for product 50 becomes 15.
    Fault hypothesis: If update_product_quantity does not modify the quantity,
      the value remains 10 instead of becoming 15.
    """
    w = _new2e66e4640__case6_Warehouse()
    w.add_product(50, 'item', 10)
    w.update_product_quantity(50, 5)
    assert w.get_product_quantity(50) == 15

from solution import Warehouse as _new2e66e4641__case7_Warehouse

def test_change_order_status_nonexistent_returns_false():
    """
    Contract quote: "return False: only if the order_id is not in self.orders"
    Input domain: order_id=9999 does not exist in any order
    Expected result: change_order_status(9999, 'cancelled') returns False.
    Fault hypothesis: If the method silently ignores the call or returns None
      instead of False, this assertion catches it.
    """
    w = _new2e66e4641__case7_Warehouse()
    result = w.change_order_status(9999, 'cancelled')
    assert result is False

from solution import Warehouse as _new2e66e4642__case8_Warehouse

def test_track_order_nonexistent_returns_false():
    """
    Contract quote: "return False: only if the order_id is not in self.orders."
    Input domain: order_id=8888 does not exist in any order
    Expected result: track_order(8888) returns False.
    Fault hypothesis: If the method returns None or raises KeyError for missing
      orders, this assertion catches it.
    """
    w = _new2e66e4642__case8_Warehouse()
    result = w.track_order(8888)
    assert result is False

from solution import Warehouse as _new2e66e4643__case9_Warehouse

def test_create_order_nonexistent_product_returns_false():
    """
    Contract quote: "return False: only if product_id is not in inventory
                     or the quantity is not adequate"
    Input domain: no products in inventory; create_order(777, 666, 5)
    Expected result: create_order returns False without raising an exception.
    Fault hypothesis: The implementation calls get_product_quantity which returns
      False for missing products, then evaluates False >= 5, causing a TypeError.
      Per spec it should return False instead.
    """
    w = _new2e66e4643__case9_Warehouse()
    result = w.create_order(777, 666, 5)
    assert result is False
