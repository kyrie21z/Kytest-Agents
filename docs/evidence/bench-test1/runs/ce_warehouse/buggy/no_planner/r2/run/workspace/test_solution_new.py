# New test candidates for solution.py revision.

from solution import Warehouse as _caseA_Warehouse


def test_add_product_adds_quantity_on_existing():
    """
    Contract quote: 'Add product to inventory and plus the quantity if it has
    existed in inventory.'
    Input domain: product_id=1 already exists with quantity 5; add_product(1,
    'widget', 3) is called again.
    Oracle: Per the spec, the existing quantity should be incremented by the new
    quantity: 5 + 3 = 8.
    Fault hypothesis: The implementation replaces the quantity instead of adding
    it (line 31: `quantity = quantity`), so the test detects the bug where the
    result would be 3 instead of 8.
    """
    wh = _caseA_Warehouse()
    wh.add_product(1, 'widget', 5)
    wh.add_product(1, 'widget', 3)
    assert wh.inventory[1]['quantity'] == 8


from solution import Warehouse as _caseB_Warehouse


def test_update_product_quantity_adds_to_existing():
    """
    Contract quote: 'According to product_id, add the quantity to the
    corresponding product in inventory.'
    Input domain: product_id=1 exists with quantity 10; update_product_quantity(1, 5)
    is called.
    Oracle: The quantity should increase by 5: 10 + 5 = 15.
    Fault hypothesis: If the implementation used assignment instead of +=, the
    quantity would become 5 instead of 15.
    """
    wh = _caseB_Warehouse()
    wh.add_product(1, 'widget', 10)
    wh.update_product_quantity(1, 5)
    assert wh.inventory[1]['quantity'] == 15


from solution import Warehouse as _caseC_Warehouse


def test_update_product_quantity_negative_decreases():
    """
    Contract quote: 'According to product_id, add the quantity to the
    corresponding product in inventory.'
    Input domain: product_id=1 exists with quantity 10; update_product_quantity(1, -3)
    is called.
    Oracle: Adding a negative quantity decreases it: 10 + (-3) = 7.
    Fault hypothesis: If the implementation ignored the sign or used absolute value,
    the result would be incorrect.
    """
    wh = _caseC_Warehouse()
    wh.add_product(1, 'widget', 10)
    wh.update_product_quantity(1, -3)
    assert wh.inventory[1]['quantity'] == 7


from solution import Warehouse as _caseD_Warehouse


def test_change_order_status_success():
    """
    Contract quote: 'Change the status of order if the input order_id is in
    self.orders.'
    Input domain: Create an order with id=1, then call change_order_status(1, 'delivered').
    Oracle: The order's status field should be updated to 'delivered'.
    Fault hypothesis: If the implementation failed to update the status or did not
    find the order, the status would remain unchanged.
    """
    wh = _caseD_Warehouse()
    wh.add_product(1, 'widget', 10)
    wh.create_order(1, 1, 3)
    result = wh.change_order_status(1, 'delivered')
    assert wh.orders[1]['status'] == 'delivered'
    assert result is None  # No return value documented for success path


from solution import Warehouse as _caseE_Warehouse


def test_change_order_status_missing_order_returns_false():
    """
    Contract quote: 'return False: only if the order_id is not in self.orders'
    Input domain: No orders exist; call change_order_status(999, 'done').
    Oracle: Should return False because order_id 999 is not in self.orders.
    Fault hypothesis: If the implementation silently skipped the check or returned
    a truthy value, the test would catch it.
    """
    wh = _caseE_Warehouse()
    result = wh.change_order_status(999, 'done')
    assert result is False


from solution import Warehouse as _caseF_Warehouse


def test_track_order_valid_order_returns_status():
    """
    Contract quote: 'Get the status of specific order.'
    Input domain: Create an order with id=1, then call track_order(1).
    Oracle: Should return the status string 'Shipped' (the default status set by
    create_order).
    Fault hypothesis: If the implementation returned the wrong field or raised an
    exception, the test would detect it.
    """
    wh = _caseF_Warehouse()
    wh.add_product(1, 'widget', 10)
    wh.create_order(1, 1, 3)
    result = wh.track_order(1)
    assert result == 'Shipped'


from solution import Warehouse as _caseG_Warehouse


def test_create_order_nonexistent_product_returns_false():
    """
    Contract quote: 'return False: only if product_id is not in inventory or
    the quantity is not adequate'
    Input domain: No products in inventory; call create_order(1, 999, 5).
    Oracle: Should return False because product_id 999 is not in inventory.
    Fault hypothesis: The implementation calls get_product_quantity(999) which
    returns False; comparing False >= 5 involves bool-int comparison. In some
    Python versions or contexts this could raise TypeError. Flagged as a suspected
    bug in the implementation.
    """
    wh = _caseG_Warehouse()
    try:
        result = wh.create_order(1, 999, 5)
        assert result is False
    except TypeError:
        # Suspected bug: comparing bool (from get_product_quantity) with int
        raise AssertionError("Suspected bug: create_order raises TypeError for non-existent product_id")
