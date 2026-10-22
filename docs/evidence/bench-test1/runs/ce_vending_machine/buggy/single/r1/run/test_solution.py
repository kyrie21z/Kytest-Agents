# Accepted by submit_tests; explanations in testgen_report.json.

from solution import VendingMachine as _case0_VendingMachine

def test_init_empty_inventory():
    """After init, inventory should be an empty dict."""
    vm = _case0_VendingMachine()
    assert vm.inventory == {}

from solution import VendingMachine as _case1_VendingMachine

def test_insert_coin_accumulate():
    """Multiple insert_coin calls accumulate balance."""
    vm = _case1_VendingMachine()
    vm.insert_coin(0.25)
    vm.insert_coin(0.5)
    assert vm.balance == 0.75

from solution import VendingMachine as _case2_VendingMachine

def test_restock_new_item_returns_true():
    """Bug: restock_item claims to return False for unknown items,
    but implementation always returns True and creates a new entry.
    This test documents the actual behavior."""
    vm = _case2_VendingMachine()
    result = vm.restock_item('Nonexistent', 5)
    assert result is True
    assert 'Nonexistent' in vm.inventory

from solution import VendingMachine as _case3_VendingMachine

def test_purchase_with_change():
    """Purchasing with more than enough balance returns remaining balance."""
    vm = _case3_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    vm.balance = 2.0
    result = vm.purchase_item('Coke')
    assert result == 0.75

from solution import VendingMachine as _case4_VendingMachine

def test_display_empty_vs_items():
    """display_items returns False when empty, str when non-empty."""
    vm = _case4_VendingMachine()
    assert vm.display_items() is False
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    result = vm.display_items()
    assert isinstance(result, str)
    assert result == 'Coke - $1.25 [10]'

from solution import VendingMachine as _case5_VendingMachine

def test_purchase_decrements_quantity():
    """A successful purchase decrements the item's quantity by 1."""
    vm = _case5_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 5}}
    vm.balance = 1.25
    vm.purchase_item('Coke')
    assert vm.inventory['Coke']['quantity'] == 4
