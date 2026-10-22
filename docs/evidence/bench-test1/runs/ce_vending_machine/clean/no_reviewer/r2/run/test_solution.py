# Accepted by submit_tests; explanations in testgen_report.json.

"""Test P1: Adds a new product to inventory."""
from solution import VendingMachine as _case0_VendingMachine

def test_p1_add_new_product():
    vm = _case0_VendingMachine()
    result = vm.add_item('Soda', 2.0, 5)
    assert result is None
    assert 'Soda' in vm.inventory
    soda = vm.inventory['Soda']
    assert soda['price'] == 2.0
    assert soda['quantity'] == 5

"""Test P2: Accumulates inserted coin value to balance."""
from solution import VendingMachine as _case1_VendingMachine

def test_p2_insert_coin_balance():
    vm = _case1_VendingMachine()
    returned = vm.insert_coin(0.5)
    assert isinstance(returned, float)
    assert returned == 0.5
    assert vm.balance == 0.5

"""Test P4: Returns false indicator when inventory is empty."""
from solution import VendingMachine as _case2_VendingMachine

def test_p4_empty_display_returns_false():
    vm = _case2_VendingMachine()
    result = vm.display_items()
    assert result is False

"""Test P3: Deducts price and decrements stock on successful purchase."""
from solution import VendingMachine as _case3_VendingMachine

def test_p3_purchase_decrements_stock():
    vm = _case3_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    vm.balance = 1.25
    returned = vm.purchase_item('Coke')
    assert returned == 0.0
    assert vm.inventory['Coke']['quantity'] == 9

"""Test P5: Handles missing or out-of-stock products gracefully."""
from solution import VendingMachine as _case4_VendingMachine

def test_p5_missing_product_returns_false():
    vm = _case4_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    vm.balance = 5.0
    result = vm.purchase_item('NonExistent')
    assert result is False

"""Test P6: Increases stock for existing items."""
from solution import VendingMachine as _case5_VendingMachine

def test_p6_restock_existing_increments():
    vm = _case5_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 5}}
    result = vm.restock_item('Coke', 10)
    assert result is True
    assert vm.inventory['Coke']['quantity'] == 15
