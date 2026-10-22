# Accepted by submit_tests; explanations in testgen_report.json.

# Accepted by submit_tests; explanations in testgen_report.json.

"""Test that a fresh VendingMachine starts with empty inventory and zero balance."""
from solution import VendingMachine as _case0_VendingMachine

def test_init_empty():
    """
    Contract quote: 'Initializes the vending machine's inventory and balance.'
    Input domain: Default constructor with no arguments.
    Expected result: vm.inventory == {} and vm.balance == 0.
    Faulty behavior: If __init__ fails to set self.inventory = {} or self.balance = 0.
    """
    vm = _case0_VendingMachine()
    assert vm.inventory == {}
    assert vm.balance == 0

"""Test that add_item correctly creates an inventory entry for a new item."""
from solution import VendingMachine as _case1_VendingMachine

def test_add_item_creates_entry():
    """
    Contract quote: "{'Coke': {'price': 1.25, 'quantity': 10}}"
    Input domain: Fresh VendingMachine, add_item('Coke', 1.25, 10).
    Expected result: vm.inventory == {'Coke': {'price': 1.25, 'quantity': 10}}.
    Faulty behavior: If add_item does not create the correct nested dictionary structure.
    """
    vm = _case1_VendingMachine()
    vm.add_item('Coke', 1.25, 10)
    assert vm.inventory == {'Coke': {'price': 1.25, 'quantity': 10}}

"""Test that purchase_item succeeds when there is enough balance and stock."""
from solution import VendingMachine as _case2_VendingMachine

def test_purchase_sufficient_funds():
    """
    Contract quote: 'If successful, returns the balance of the vending machine after the product is purchased'
    Input domain: VM with Coke ($1.25, qty 10), balance 1.25, purchase_item('Coke').
    Expected result: Returns 0.0, item quantity decrements from 10 to 9.
    Faulty behavior: If purchase does not decrement quantity or returns wrong balance.
    """
    vm = _case2_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    vm.balance = 1.25
    result = vm.purchase_item('Coke')
    assert result == 0.0
    assert vm.inventory['Coke']['quantity'] == 9

"""Test that purchase_item returns False when balance is insufficient."""
from solution import VendingMachine as _case3_VendingMachine

def test_purchase_insufficient_funds():
    """
    Contract quote: 'otherwise, returns False'
    Input domain: VM with Coke ($1.25, qty 10), balance 1.00, purchase_item('Coke').
    Expected result: Returns False, balance remains 1.00, quantity unchanged.
    Faulty behavior: If purchase proceeds despite insufficient funds or modifies state incorrectly.
    """
    vm = _case3_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    vm.balance = 1.0
    result = vm.purchase_item('Coke')
    assert result is False
    assert vm.balance == 1.0
    assert vm.inventory['Coke']['quantity'] == 10

"""Test that insert_coin accumulates correctly across multiple calls."""
from solution import VendingMachine as _case4_VendingMachine

def test_insert_coin_accumulates():
    """
    Contract quote: 'The balance of the vending machine after the coins are inserted, float.'
    Input domain: Fresh VM, insert 1.25 then 2.50.
    Expected result: Second call returns 3.75, balance is 3.75.
    Faulty behavior: If insert_coin overwrites balance instead of accumulating.
    """
    vm = _case4_VendingMachine()
    vm.insert_coin(1.25)
    r2 = vm.insert_coin(2.5)
    assert r2 == 3.75
    assert vm.balance == 3.75

"""Test that restock_item adds quantity to an existing item and returns True."""
from solution import VendingMachine as _case5_VendingMachine

def test_restock_existing_item():
    """
    Contract quote: 'Replenishes the inventory of a product already in the vending machine.'
    Input domain: VM with Coke ($1.25, qty 10), restock_item('Coke', 5).
    Expected result: Returns True, quantity becomes 15.
    Faulty behavior: If restock does not add to existing quantity or returns wrong value.
    """
    vm = _case5_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    result = vm.restock_item('Coke', 5)
    assert result is True
    assert vm.inventory['Coke']['quantity'] == 15

"""Test that restock_item returns False for items not in inventory."""
from solution import VendingMachine as _case6_VendingMachine

def test_restock_nonexistent_item():
    """
    Contract quote: 'If the product is already in the vending machine, returns True, otherwise, returns False.'
    Input domain: Empty VM, restock_item('Pizza', 10).
    Expected result: Returns False, inventory remains empty.
    Faulty behavior: If restock creates a new entry for unknown items.
    """
    vm = _case6_VendingMachine()
    result = vm.restock_item('Pizza', 10)
    assert result is False
    assert vm.inventory == {}

"""Test that display_items returns False when inventory is empty."""
from solution import VendingMachine as _case7_VendingMachine

def test_display_items_empty():
    """
    Contract quote: 'If the vending machine is empty, returns False'
    Input domain: Fresh VendingMachine, display_items().
    Expected result: Returns False.
    Faulty behavior: If display_items returns empty string or raises error on empty inventory.
    """
    vm = _case7_VendingMachine()
    result = vm.display_items()
    assert result is False

"""Test that display_items formats a single item correctly."""
from solution import VendingMachine as _case8_VendingMachine

def test_display_items_single():
    """
    Contract quote: "'Coke - $1.25 [10]'"
    Input domain: VM with Coke ($1.25, qty 10), display_items().
    Expected result: Returns 'Coke - $1.25 [10]'.
    Faulty behavior: If format string is wrong or missing components.
    """
    vm = _case8_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    result = vm.display_items()
    assert result == 'Coke - $1.25 [10]'


"""Test that purchase_item succeeds when the item has exactly 1 unit in stock."""
from solution import VendingMachine as _new76547e570_VendingMachine

def test_purchase_last_unit():
    """
    Contract quote: 'If successful, returns the balance of the vending machine after the product is purchased'
    Input domain: VM with Coke ($1.25, qty 1), balance 1.25, purchase_item('Coke').
    Expected result: Returns 0.0, item quantity decrements from 1 to 0.
    Faulty behavior: If the condition at line 58 uses '> 1' instead of '> 0', the purchase would incorrectly return False when only 1 unit remains, failing to decrement stock.
    """
    vm = _new76547e570_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 1}}
    vm.balance = 1.25
    result = vm.purchase_item('Coke')
    assert result == 0.0
    assert vm.inventory['Coke']['quantity'] == 0

"""Test that purchase_item returns False when the item does not exist in inventory."""
from solution import VendingMachine as _new76547e571_VendingMachine

def test_purchase_nonexistent_item():
    """
    Contract quote: "vendingMachine.purchase_item('Pizza')"
    Input domain: VM with Coke ($1.25, qty 10), balance 1.25, purchase_item('Pizza') where 'Pizza' is not in inventory.
    Expected result: Returns False, balance remains unchanged, inventory unchanged.
    Faulty behavior: If purchase_item does not check item existence and falls through incorrectly, or returns a wrong value instead of False on line 65.
    """
    vm = _new76547e571_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    vm.balance = 1.25
    result = vm.purchase_item('Pizza')
    assert result is False
    assert vm.balance == 1.25
    assert 'Pizza' not in vm.inventory
