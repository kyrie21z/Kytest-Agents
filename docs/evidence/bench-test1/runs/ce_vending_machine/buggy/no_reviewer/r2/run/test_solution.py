# Accepted by submit_tests; explanations in testgen_report.json.

from solution import VendingMachine as _case0_VendingMachine

def test_p2_insert_coin_cumulative():
    v = _case0_VendingMachine()
    assert v.balance == 0
    r1 = v.insert_coin(1.25)
    assert r1 == 1.25
    assert v.balance == 1.25
    r2 = v.insert_coin(2.5)
    assert r2 == 3.75
    assert v.balance == 3.75

from solution import VendingMachine as _case1_VendingMachine

def test_p3_purchase_deduct():
    v = _case1_VendingMachine()
    v.inventory = {'Chips': {'price': 2.0, 'quantity': 5}}
    v.balance = 5.0
    result = v.purchase_item('Chips')
    assert result == 3.0
    assert v.balance == 3.0
    assert v.inventory['Chips']['quantity'] == 4

from solution import VendingMachine as _case2_VendingMachine

def test_p4_display_empty():
    v = _case2_VendingMachine()
    result = v.display_items()
    assert result is False

from solution import VendingMachine as _case3_VendingMachine

def test_p5_purchase_unavailable():
    v = _case3_VendingMachine()
    v.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    result = v.purchase_item('GhostItem')
    assert result is False
    assert v.balance == 0
    assert v.inventory['Coke']['quantity'] == 10

from solution import VendingMachine as _case4_VendingMachine

def test_p6_restock_existing():
    v = _case4_VendingMachine()
    v.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    result = v.restock_item('Coke', 10)
    assert result is True
    assert v.inventory['Coke']['quantity'] == 20
