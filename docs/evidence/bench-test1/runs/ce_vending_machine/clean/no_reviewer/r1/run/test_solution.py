# Accepted by submit_tests; explanations in testgen_report.json.

"""Test P2: Insert coins and verify returned balance."""
from solution import VendingMachine as _case0_VendingMachine

def test_p2_insert_coin():
    vm = _case0_VendingMachine()
    ret = vm.insert_coin(2.5)
    assert ret == 2.5
    assert vm.balance == 2.5

"""Test P3: Purchase with sufficient funds and stock."""
from solution import VendingMachine as _case1_VendingMachine

def test_p3_purchase_sufficient_funds():
    vm = _case1_VendingMachine()
    vm.add_item('Coke', 1.25, 5)
    vm.insert_coin(2.0)
    ret = vm.purchase_item('Coke')
    assert ret == 0.75
    assert vm.balance == 0.75
    assert vm.inventory['Coke']['quantity'] == 4

"""Test P5: Display items on an empty machine."""
from solution import VendingMachine as _case2_VendingMachine

def test_p5_empty_display():
    vm = _case2_VendingMachine()
    ret = vm.display_items()
    assert ret is False

"""Test P1: Add a new product to inventory."""
from solution import VendingMachine as _case3_VendingMachine

def test_p1_add_item():
    vm = _case3_VendingMachine()
    result = vm.add_item('Coke', 1.25, 10)
    assert result is None
    assert vm.inventory == {'Coke': {'price': 1.25, 'quantity': 10}}

"""Test P4: Purchase with exact balance."""
from solution import VendingMachine as _case4_VendingMachine

def test_p4_exact_balance():
    vm = _case4_VendingMachine()
    vm.add_item('Coke', 1.25, 1)
    vm.insert_coin(1.25)
    ret = vm.purchase_item('Coke')
    assert ret == 0.0
    assert vm.balance == 0.0
    assert vm.inventory['Coke']['quantity'] == 0

"""Test P6: Sequential purchases depleting stock."""
from solution import VendingMachine as _case5_VendingMachine

def test_p6_sequential_depletion():
    vm = _case5_VendingMachine()
    vm.add_item('Soda', 1.0, 2)
    vm.insert_coin(3.0)
    r1 = vm.purchase_item('Soda')
    assert r1 == 2.0
    assert vm.inventory['Soda']['quantity'] == 1
    r2 = vm.purchase_item('Soda')
    assert r2 == 1.0
    assert vm.inventory['Soda']['quantity'] == 0
    r3 = vm.purchase_item('Soda')
    assert r3 is False

"""Test P7: Restock an existing product."""
from solution import VendingMachine as _case6_VendingMachine

def test_p7_restock_existing():
    vm = _case6_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 5}}
    ret = vm.restock_item('Coke', 10)
    assert ret is True
    assert vm.inventory['Coke']['quantity'] == 15

"""Test P8: Restock a non-existent product."""
from solution import VendingMachine as _case7_VendingMachine

def test_p8_restock_nonexistent():
    vm = _case7_VendingMachine()
    ret = vm.restock_item('Pizza', 10)
    assert ret is False
    assert 'Pizza' not in vm.inventory

"""Test P9: Display items with inventory present."""
from solution import VendingMachine as _case8_VendingMachine

def test_p9_display_with_inventory():
    vm = _case8_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    ret = vm.display_items()
    assert ret == 'Coke - $1.25 [10]'

"""Extra: Purchase with insufficient funds returns False."""
from solution import VendingMachine as _case9_VendingMachine

def test_extra_purchase_insufficient_funds():
    vm = _case9_VendingMachine()
    vm.add_item('Coke', 1.25, 5)
    vm.insert_coin(1.0)
    ret = vm.purchase_item('Coke')
    assert ret is False
    assert vm.balance == 1.0
    assert vm.inventory['Coke']['quantity'] == 5

"""Extra: Purchase non-existent item returns False."""
from solution import VendingMachine as _case10_VendingMachine

def test_extra_purchase_nonexistent_item():
    vm = _case10_VendingMachine()
    vm.insert_coin(5.0)
    ret = vm.purchase_item('NonExistent')
    assert ret is False
    assert vm.balance == 5.0

"""Extra: Display items with multiple products in inventory."""
from solution import VendingMachine as _case11_VendingMachine

def test_extra_multiple_items_display():
    vm = _case11_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}, 'Pepsi': {'price': 1.5, 'quantity': 5}}
    ret = vm.display_items()
    assert 'Coke' in ret
    assert 'Pepsi' in ret
    assert '$1.25' in ret
    assert '[10]' in ret
    assert '[5]' in ret
