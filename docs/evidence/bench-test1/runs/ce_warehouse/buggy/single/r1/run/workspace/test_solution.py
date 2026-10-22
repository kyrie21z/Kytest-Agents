# Accepted by submit_tests; explanations in testgen_report.json.

def test_add_product_updates_existing_quantity():
    """
    Contract quote: 'Add product to inventory and plus the quantity if it has
    existed in inventory.'
    Input domain: product already exists, add_product called again with same id.
    Expected result: quantity is replaced (not accumulated) per the else-branch
    which sets quantity directly.
    Fault hypothesis: bug that accumulates quantities instead of replacing them.
    """
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'widget', 3)
    w.add_product(1, 'widget', 7)
    assert w.inventory[1]['quantity'] == 7

def test_create_order_fails_on_insufficient_stock():
    """
    Contract quote: 'return False: only if ... the quantity is not adequate'.
    Input domain: request more than available inventory.
    Expected result: returns False, inventory unchanged.
    Fault hypothesis: allows order despite insufficient stock.
    """
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'scarce', 2)
    result = w.create_order(200, 1, 5)
    assert result is False
    assert w.inventory[1]['quantity'] == 2

def test_get_product_quantity_returns_int_or_false():
    """
    Contract quote: 'if the product_id is in inventory then return the
    corresponding quantity, or False otherwise.'
    Input domain: query existing and non-existing product ids.
    Expected result: existing id returns int >= 0; non-existing returns False.
    Fault hypothesis: returns None instead of False, or raises KeyError.
    """
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'gadget', 10)
    assert w.get_product_quantity(1) == 10
    assert w.get_product_quantity(999) is False

def test_update_product_quantity_nonexistent_ignored():
    """
    Contract quote: 'if product_id in self.inventory' guard before update.
    Input domain: product_id not in inventory.
    Expected result: no change, no error raised.
    Fault hypothesis: raises KeyError for missing product.
    """
    from solution import Warehouse
    w = Warehouse()
    w.update_product_quantity(999, 5)
    assert 999 not in w.inventory

def test_change_order_status_returns_false_for_missing():
    """
    Contract quote: 'return False: only if the order_id is not in self.orders'.
    Input domain: order_id that was never created.
    Expected result: returns False.
    Fault hypothesis: returns None instead of False.
    """
    from solution import Warehouse
    w = Warehouse()
    result = w.change_order_status(999, 'done')
    assert result is False

def test_full_workflow():
    """
    Contract quote: end-to-end usage of all methods.
    Input domain: realistic sequence of operations.
    Expected result: inventory and orders reflect all changes correctly.
    Fault hypothesis: state inconsistency across method calls.
    """
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'A', 20)
    w.add_product(2, 'B', 10)
    w.update_product_quantity(1, -5)
    assert w.get_product_quantity(1) == 15
    w.create_order(10, 1, 3)
    w.create_order(11, 2, 4)
    assert w.track_order(10) == 'Shipped'
    w.change_order_status(10, 'delivered')
    assert w.track_order(10) == 'delivered'
    assert w.track_order(11) == 'Shipped'
    assert w.get_product_quantity(2) == 6
