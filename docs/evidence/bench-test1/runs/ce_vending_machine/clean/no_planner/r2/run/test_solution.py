# Accepted by submit_tests; explanations in testgen_report.json.

from solution import VendingMachine as _case0_VendingMachine

def test_init_empty():
    vm = _case0_VendingMachine()
    assert vm.inventory == {}
    assert vm.balance == 0

from solution import VendingMachine as _case1_VendingMachine

def test_add_item_new():
    vm = _case1_VendingMachine()
    vm.add_item('Coke', 1.25, 10)
    assert vm.inventory == {'Coke': {'price': 1.25, 'quantity': 10}}

from solution import VendingMachine as _case2_VendingMachine

def test_add_item_existing_restocks():
    vm = _case2_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    vm.add_item('Coke', 1.5, 5)
    assert vm.inventory['Coke']['quantity'] == 15
    assert vm.inventory['Coke']['price'] == 1.25

from solution import VendingMachine as _case3_VendingMachine

def test_insert_coin_accumulates():
    vm = _case3_VendingMachine()
    r1 = vm.insert_coin(0.25)
    assert r1 == 0.25
    r2 = vm.insert_coin(0.5)
    assert r2 == 0.75
    r3 = vm.insert_coin(1.0)
    assert r3 == 1.75
    assert vm.balance == 1.75

from solution import VendingMachine as _case4_VendingMachine

def test_purchase_success():
    vm = _case4_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    vm.balance = 1.25
    result = vm.purchase_item('Coke')
    assert result == 0.0
    assert vm.balance == 0.0
    assert vm.inventory['Coke']['quantity'] == 9

from solution import VendingMachine as _case5_VendingMachine

def test_purchase_insufficient_balance():
    vm = _case5_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    vm.balance = 1.0
    result = vm.purchase_item('Coke')
    assert result is False
    assert vm.balance == 1.0
    assert vm.inventory['Coke']['quantity'] == 10

from solution import VendingMachine as _case6_VendingMachine

def test_purchase_out_of_stock():
    vm = _case6_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 0}}
    vm.balance = 5.0
    result = vm.purchase_item('Coke')
    assert result is False
    assert vm.balance == 5.0
    assert vm.inventory['Coke']['quantity'] == 0

from solution import VendingMachine as _case7_VendingMachine

def test_purchase_nonexistent_item():
    vm = _case7_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    vm.balance = 5.0
    result = vm.purchase_item('Pizza')
    assert result is False
    assert vm.balance == 5.0
    assert vm.inventory == {'Coke': {'price': 1.25, 'quantity': 10}}

from solution import VendingMachine as _case8_VendingMachine

def test_restock_existing():
    vm = _case8_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    result = vm.restock_item('Coke', 10)
    assert result is True
    assert vm.inventory['Coke']['quantity'] == 20
    assert vm.inventory['Coke']['price'] == 1.25

from solution import VendingMachine as _case9_VendingMachine

def test_restock_nonexistent():
    vm = _case9_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    result = vm.restock_item('Pizza', 10)
    assert result is False
    assert vm.inventory == {'Coke': {'price': 1.25, 'quantity': 10}}

from solution import VendingMachine as _case10_VendingMachine

def test_display_empty():
    vm = _case10_VendingMachine()
    result = vm.display_items()
    assert result is False

from solution import VendingMachine as _case11_VendingMachine

def test_display_single_item():
    vm = _case11_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    result = vm.display_items()
    assert result == 'Coke - $1.25 [10]'

from solution import VendingMachine as _case12_VendingMachine

def test_purchase_exact_balance():
    vm = _case12_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 1}}
    vm.balance = 1.25
    result = vm.purchase_item('Coke')
    assert result == 0.0
    assert vm.balance == 0.0
    assert vm.inventory['Coke']['quantity'] == 0

from solution import VendingMachine as _case13_VendingMachine

def test_insert_coin_negative():
    vm = _case13_VendingMachine()
    vm.insert_coin(5.0)
    r = vm.insert_coin(-1.0)
    assert r == 4.0
    assert vm.balance == 4.0

from solution import VendingMachine as _case14_VendingMachine

def test_zero_quantity_add():
    vm = _case14_VendingMachine()
    vm.add_item('Water', 0.75, 0)
    assert vm.inventory == {'Water': {'price': 0.75, 'quantity': 0}}
