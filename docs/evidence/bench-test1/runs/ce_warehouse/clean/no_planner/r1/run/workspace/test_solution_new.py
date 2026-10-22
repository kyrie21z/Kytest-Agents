# New test candidates for review by submit_tests.

from solution import Warehouse as _case6_Warehouse

def test_update_product_quantity_modifies_existing():
    """
    Contract quote: 'According to product_id, add the quantity to the corresponding
                     product in inventory.'
    Input domain: add_product(50, 'item', 10); update_product_quantity(50, 5)
    Expected result: inventory quantity for product 50 becomes 15.
    Fault hypothesis: If update_product_quantity does not modify the quantity,
      the value remains 10 instead of becoming 15.
    """
    w = _case6_Warehouse()
    w.add_product(50, 'item', 10)
    w.update_product_quantity(50, 5)
    assert w.get_product_quantity(50) == 15


from solution import Warehouse as _case7_Warehouse

def test_change_order_status_nonexistent_returns_false():
    """
    Contract quote: "return False: only if the order_id is not in self.orders"
    Input domain: order_id=9999 does not exist in any order
    Expected result: change_order_status(9999, 'cancelled') returns False.
    Fault hypothesis: If the method silently ignores the call or returns None
      instead of False, this assertion catches it.
    """
    w = _case7_Warehouse()
    result = w.change_order_status(9999, 'cancelled')
    assert result is False


from solution import Warehouse as _case8_Warehouse

def test_track_order_nonexistent_returns_false():
    """
    Contract quote: "return False: only if the order_id is not in self.orders."
    Input domain: order_id=8888 does not exist in any order
    Expected result: track_order(8888) returns False.
    Fault hypothesis: If the method returns None or raises KeyError for missing
      orders, this assertion catches it.
    """
    w = _case8_Warehouse()
    result = w.track_order(8888)
    assert result is False


from solution import Warehouse as _case9_Warehouse

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
    w = _case9_Warehouse()
    result = w.create_order(777, 666, 5)
    assert result is False
