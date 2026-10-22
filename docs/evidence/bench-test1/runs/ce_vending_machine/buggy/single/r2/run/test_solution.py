# Accepted by submit_tests; explanations in testgen_report.json.

from solution import VendingMachine as _case0_VendingMachine

def test_init_empty():
    """Verify a fresh VendingMachine starts with empty inventory and zero balance."""
    vm = _case0_VendingMachine()
    assert vm.inventory == {}
    assert vm.balance == 0

from solution import VendingMachine as _case1_VendingMachine

def test_insert_coin_accumulates():
    """Verify insert_coin returns cumulative balance after multiple inserts."""
    vm = _case1_VendingMachine()
    r1 = vm.insert_coin(0.25)
    r2 = vm.insert_coin(0.75)
    assert r1 == 0.25
    assert r2 == 1.0
    assert vm.balance == 1.0

from solution import VendingMachine as _case2_VendingMachine

def test_purchase_success():
    """Verify a successful purchase returns remaining balance and decrements quantity."""
    vm = _case2_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    vm.balance = 1.25
    result = vm.purchase_item('Coke')
    assert result == 0.0
    assert vm.inventory['Coke']['quantity'] == 9

from solution import VendingMachine as _case3_VendingMachine

def test_purchase_insufficient_funds():
    """Verify purchase returns False when balance is less than item price."""
    vm = _case3_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    vm.balance = 1.0
    result = vm.purchase_item('Coke')
    assert result is False
    assert vm.balance == 1.0
    assert vm.inventory['Coke']['quantity'] == 10

from solution import VendingMachine as _case4_VendingMachine

def test_display_empty():
    """Verify display_items returns False when inventory is empty."""
    vm = _case4_VendingMachine()
    result = vm.display_items()
    assert result is False

from solution import VendingMachine as _case5_VendingMachine

def test_display_single_item():
    """Verify display_items formats a single item correctly."""
    vm = _case5_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    result = vm.display_items()
    assert result == 'Coke - $1.25 [10]'

from solution import VendingMachine as _case6_VendingMachine

def test_purchase_out_of_stock():
    """Verify purchase returns False when item quantity is zero even if balance suffices."""
    vm = _case6_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 0}}
    vm.balance = 5.0
    result = vm.purchase_item('Coke')
    assert result is False
    assert vm.balance == 5.0
    assert vm.inventory['Coke']['quantity'] == 0

from solution import VendingMachine as _case7_VendingMachine

def test_insert_coin_zero():
    """Verify insert_coin handles zero amount correctly."""
    vm = _case7_VendingMachine()
    r = vm.insert_coin(0)
    assert r == 0
    assert vm.balance == 0

from solution import VendingMachine as _case8_VendingMachine

def test_purchase_exact_balance():
    """Verify purchase succeeds when balance exactly equals item price."""
    vm = _case8_VendingMachine()
    vm.inventory = {'Water': {'price': 1.0, 'quantity': 3}}
    vm.balance = 1.0
    result = vm.purchase_item('Water')
    assert result == 0.0
    assert vm.inventory['Water']['quantity'] == 2
