# Accepted by submit_tests; explanations in testgen_report.json.

from solution import VendingMachine as _case0_VendingMachine

def test_p3_purchase_exact_funds():
    v = _case0_VendingMachine()
    v.inventory = {'A': {'price': 1.0, 'quantity': 1}}
    v.balance = 1.0
    result = v.purchase_item('A')
    assert result == 0.0
    assert v.inventory['A']['quantity'] == 0

from solution import VendingMachine as _case1_VendingMachine

def test_p4_display_empty():
    v = _case1_VendingMachine()
    result = v.display_items()
    assert result is False

from solution import VendingMachine as _case2_VendingMachine

def test_p5_purchase_nonexistent():
    v = _case2_VendingMachine()
    v.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    result = v.purchase_item('Missing')
    assert result is False
    assert v.inventory == {'Coke': {'price': 1.25, 'quantity': 10}}

from solution import VendingMachine as _case3_VendingMachine

def test_p7_restock_existing():
    v = _case3_VendingMachine()
    v.inventory = {'B': {'price': 2.0, 'quantity': 3}}
    result = v.restock_item('B', 4)
    assert result is True
    assert v.inventory['B']['quantity'] == 7

from solution import VendingMachine as _case4_VendingMachine

def test_p2_insert_coin_accumulates():
    v = _case4_VendingMachine()
    result = v.insert_coin(2.5)
    assert result == 2.5
    assert v.balance == 2.5

from solution import VendingMachine as _case5_VendingMachine

def test_p6_insert_coin_zero():
    v = _case5_VendingMachine()
    result = v.insert_coin(0.0)
    assert result == 0.0
    assert v.balance == 0

from solution import VendingMachine as _case6_VendingMachine

def test_p8_insufficient_funds():
    v = _case6_VendingMachine()
    v.inventory = {'C': {'price': 5.0, 'quantity': 1}}
    v.balance = 2.0
    result = v.purchase_item('C')
    assert result is False
    assert v.balance == 2.0
