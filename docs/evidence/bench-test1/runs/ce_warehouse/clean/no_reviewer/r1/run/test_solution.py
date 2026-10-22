# Accepted by submit_tests; explanations in testgen_report.json.

def test_p1_add_new_product():
    from solution import Warehouse
    warehouse = Warehouse()
    warehouse.add_product(1, 'A', 5)
    assert warehouse.inventory[1] == {'name': 'A', 'quantity': 5}

def test_p2_accumulate_quantity():
    from solution import Warehouse
    warehouse = Warehouse()
    warehouse.add_product(1, 'A', 5)
    warehouse.add_product(1, 'A', 3)
    assert warehouse.inventory[1]['quantity'] == 8

def test_p4_nonexistent_product_quantity():
    from solution import Warehouse
    warehouse = Warehouse()
    result = warehouse.get_product_quantity(999)
    assert result is False

def test_p5_nonexistent_product_order():
    from solution import Warehouse
    warehouse = Warehouse()
    result = warehouse.create_order(10, 999, 2)
    assert result is False
