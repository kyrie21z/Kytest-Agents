# Accepted by submit_tests; explanations in testgen_report.json.

# Accepted by submit_tests; explanations in testgen_report.json.

from solution import Warehouse as _case0_Warehouse

def test_add_product_creates_entry():
    wh = _case0_Warehouse()
    wh.add_product(1, 'widget', 5)
    assert wh.inventory == {1: {'name': 'widget', 'quantity': 5}}

from solution import Warehouse as _case1_Warehouse

def test_add_product_replaces_quantity():
    wh = _case1_Warehouse()
    wh.add_product(1, 'widget', 5)
    wh.add_product(1, 'widget', 3)
    assert wh.inventory[1]['quantity'] == 3

from solution import Warehouse as _case2_Warehouse

def test_get_product_quantity_returns_false_for_missing():
    wh = _case2_Warehouse()
    result = wh.get_product_quantity(999)
    assert result is False

from solution import Warehouse as _case3_Warehouse

def test_create_order_deducts_stock_and_sets_shipped():
    wh = _case3_Warehouse()
    wh.add_product(1, 'widget', 10)
    result = wh.create_order(100, 1, 3)
    assert wh.inventory[1]['quantity'] == 7
    assert wh.orders[100] == {'product_id': 1, 'quantity': 3, 'status': 'Shipped'}

from solution import Warehouse as _case4_Warehouse

def test_create_order_insufficient_stock_returns_false():
    wh = _case4_Warehouse()
    wh.add_product(1, 'widget', 2)
    result = wh.create_order(1, 1, 5)
    assert result is False
    assert wh.inventory[1]['quantity'] == 2
    assert 1 not in wh.orders

from solution import Warehouse as _case5_Warehouse

def test_track_order_returns_false_for_missing():
    wh = _case5_Warehouse()
    result = wh.track_order(999)
    assert result is False


from solution import Warehouse as _new5c6949db0__caseB_Warehouse

def test_update_product_quantity_adds_to_existing():
    wh = _new5c6949db0__caseB_Warehouse()
    wh.add_product(1, 'widget', 10)
    wh.update_product_quantity(1, 5)
    assert wh.inventory[1]['quantity'] == 15

from solution import Warehouse as _new5c6949db1__caseC_Warehouse

def test_change_order_status_success():
    wh = _new5c6949db1__caseC_Warehouse()
    wh.add_product(1, 'widget', 10)
    wh.create_order(1, 1, 3)
    result = wh.change_order_status(1, 'delivered')
    assert wh.orders[1]['status'] == 'delivered'
    assert result is None

from solution import Warehouse as _new5c6949db2__caseD_Warehouse

def test_change_order_status_missing_order_returns_false():
    wh = _new5c6949db2__caseD_Warehouse()
    result = wh.change_order_status(999, 'done')
    assert result is False

from solution import Warehouse as _new5c6949db3__caseE_Warehouse

def test_track_order_valid_order_returns_status():
    wh = _new5c6949db3__caseE_Warehouse()
    wh.add_product(1, 'widget', 10)
    wh.create_order(1, 1, 3)
    result = wh.track_order(1)
    assert result == 'Shipped'

from solution import Warehouse as _new5c6949db4__caseF_Warehouse

def test_create_order_nonexistent_product_returns_false():
    wh = _new5c6949db4__caseF_Warehouse()
    try:
        result = wh.create_order(1, 999, 5)
        assert result is False
    except TypeError:
        raise AssertionError('Suspected bug: create_order raises TypeError for non-existent product_id')
