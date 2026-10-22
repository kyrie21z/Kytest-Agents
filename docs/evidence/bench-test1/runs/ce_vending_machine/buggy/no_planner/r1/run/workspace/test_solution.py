# Accepted by submit_tests; explanations in testgen_report.json.

"""Test successful purchase when balance equals the item price."""
from solution import VendingMachine as _case0_VendingMachine

def test_purchase_success_exact_balance():
    vm = _case0_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    vm.balance = 1.25
    result = vm.purchase_item('Coke')
    assert result == 0.0
    assert vm.inventory['Coke']['quantity'] == 9

"""Test that insert_coin accumulates amounts across multiple calls."""
from solution import VendingMachine as _case1_VendingMachine

def test_insert_coin_accumulates():
    vm = _case1_VendingMachine()
    assert vm.insert_coin(0.25) == 0.25
    assert vm.insert_coin(0.5) == 0.75
    assert vm.insert_coin(1.0) == 1.75

"""Test that display_items returns False for an empty vending machine."""
from solution import VendingMachine as _case2_VendingMachine

def test_display_items_empty_returns_false():
    vm = _case2_VendingMachine()
    result = vm.display_items()
    assert result is False

"""Test that restock_item increments quantity for existing items."""
from solution import VendingMachine as _case3_VendingMachine

def test_restock_existing_increments_quantity():
    vm = _case3_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    result = vm.restock_item('Coke', 5)
    assert result is True
    assert vm.inventory['Coke']['quantity'] == 15
