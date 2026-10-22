# Accepted by submit_tests; explanations in testgen_report.json.

def test_p1_new_product():
    """Register a new product in inventory.

    Docstring quote: 'Add product to inventory and plus the quantity if it has existed in inventory. Or just add new product to dict otherwise.'

    Input domain: product_id=1 (int), name='Widget' (str), quantity=10 (int), warehouse freshly initialized.

    Expected result: warehouse.inventory == {1: {'name': 'Widget', 'quantity': 10}}

    Rationale: Docstring example explicitly demonstrates the exact dictionary structure created for a new product.

    Faulty behavior detected: If the method fails to create the correct dictionary structure with 'name' and 'quantity' keys, or uses wrong values.
    """
    from solution import Warehouse
    warehouse = Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    assert warehouse.inventory == {1: {'name': 'Widget', 'quantity': 10}}

def test_p3_get_existing():
    """Retrieve quantity for an existing product.

    Docstring quote: 'if the product_id is in inventory then return the corresponding quantity'

    Input domain: product_id=1 exists in inventory with quantity 15.

    Expected result: warehouse.get_product_quantity(1) == 15

    Rationale: Specification states: 'if the product_id is in inventory then return the corresponding quantity'

    Faulty behavior detected: If the method returns a wrong value or raises an exception for a valid product_id.
    """
    from solution import Warehouse
    warehouse = Warehouse()
    warehouse.add_product(1, 'Widget', 15)
    assert warehouse.get_product_quantity(1) == 15

def test_p4_nonexistent_product():
    """Signal failure when querying non-existent product.

    Docstring quote: 'or False otherwise.'

    Input domain: product_id=999 does not exist in inventory.

    Expected result: warehouse.get_product_quantity(999) == False

    Rationale: Specification states: 'or False otherwise.'

    Faulty behavior detected: If the method returns None, raises KeyError, or returns any truthy value for a non-existent product.
    """
    from solution import Warehouse
    warehouse = Warehouse()
    assert warehouse.get_product_quantity(999) is False

def test_p5_create_order():
    """Create a valid order with default status.

    Docstring quote: 'The default value of status is 'Shipped'.'

    Input domain: product_id=1 exists with quantity 10, order_id=101, quantity=5.

    Expected result: warehouse.orders == {101: {'product_id': 1, 'quantity': 5, 'status': 'Shipped'}}

    Rationale: Docstring example shows order creation populating the orders dict with product info and default status 'Shipped'.

    Faulty behavior detected: If the order is not created, or the status is not 'Shipped', or the order dict structure is incorrect.
    """
    from solution import Warehouse
    warehouse = Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    warehouse.create_order(101, 1, 5)
    assert warehouse.orders == {101: {'product_id': 1, 'quantity': 5, 'status': 'Shipped'}}

def test_p6_insufficient_inventory():
    """Reject order with insufficient inventory.

    Docstring quote: 'only if product_id is not in inventory or the quantity is not adequate'

    Input domain: product_id=1 exists with quantity 10, order_id=102, quantity=20 (more than available).

    Expected result: warehouse.create_order(102, 1, 20) == False

    Rationale: Specification states return False 'only if ... the quantity is not adequate'.

    Faulty behavior detected: If the method returns True, None, or creates an order despite insufficient inventory.
    """
    from solution import Warehouse
    warehouse = Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    result = warehouse.create_order(102, 1, 20)
    assert result is False

def test_p7_change_status():
    """Update status of an existing order.

    Docstring quote: 'Change the status of order if the input order_id is in self.orders.'

    Input domain: order_id=101 exists with status 'Shipped', then change_order_status(101, 'Delivered').

    Expected result: warehouse.orders[101]['status'] == 'Delivered'

    Rationale: Specification states: 'Change the status of order if the input order_id is in self.orders.'

    Faulty behavior detected: If the status is not updated, or if the method returns False when it should succeed.
    """
    from solution import Warehouse
    warehouse = Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    warehouse.create_order(101, 1, 5)
    warehouse.change_order_status(101, 'Delivered')
    assert warehouse.orders[101]['status'] == 'Delivered'

def test_p8_negative_adjustment():
    """Apply negative quantity adjustment.

    Docstring quote: 'According to product_id, add the quantity to the corresponding product in inventory.'

    Input domain: product_id=1 exists with quantity 10, then update_product_quantity(1, -3).

    Expected result: warehouse.inventory[1]['quantity'] == 7

    Rationale: Docstring example explicitly uses a negative value (-1) to reduce quantity, indicating simple arithmetic addition is performed without clamping.

    Faulty behavior detected: If the method clamps negative values to zero, raises an error, or does not perform arithmetic addition.
    """
    from solution import Warehouse
    warehouse = Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    warehouse.update_product_quantity(1, -3)
    assert warehouse.inventory[1]['quantity'] == 7

def test_extra_track_order():
    """Track order status for an existing order.

    Docstring quote: 'Get the status of specific order.'

    Input domain: order_id=1 exists with status 'Shipped' after create_order.

    Expected result: warehouse.track_order(1) == 'Shipped'

    Rationale: Docstring example shows track_order returns the current status of an existing order.

    Faulty behavior detected: If the method returns wrong status, None, or raises exception.
    """
    from solution import Warehouse
    warehouse = Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    warehouse.create_order(1, 1, 5)
    assert warehouse.track_order(1) == 'Shipped'

def test_extra_track_nonexistent():
    """Return False when tracking non-existent order.

    Docstring quote: 'return False: only if the order_id is not in self.orders.'

    Input domain: order_id=999 does not exist in orders.

    Expected result: warehouse.track_order(999) == False

    Rationale: Specification states return False when order_id is not found.

    Faulty behavior detected: If the method returns None, raises KeyError, or returns any truthy value.
    """
    from solution import Warehouse
    warehouse = Warehouse()
    assert warehouse.track_order(999) is False
