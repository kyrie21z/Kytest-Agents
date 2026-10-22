# Accepted by submit_tests; explanations in testgen_report.json.

from solution import VendingMachine as _case0_VendingMachine

def test_p2_insert_coin():
    """P2: Insert coins and update balance."""
    vm = _case0_VendingMachine()
    result = vm.insert_coin(5.0)
    assert result == 5.0
    assert vm.balance == 5.0

from solution import VendingMachine as _case1_VendingMachine

def test_p3_successful_purchase():
    """P3: Successful purchase deducts balance and updates state."""
    vm = _case1_VendingMachine()
    vm.inventory = {'A': {'price': 2.0, 'quantity': 1}}
    vm.balance = 2.0
    result = vm.purchase_item('A')
    assert result == 0.0
    assert vm.balance == 0.0
    assert vm.inventory['A']['quantity'] == 0

from solution import VendingMachine as _case2_VendingMachine

def test_p4_out_of_stock():
    """P4: Purchase attempt when quantity is zero."""
    vm = _case2_VendingMachine()
    vm.inventory = {'B': {'price': 1.0, 'quantity': 0}}
    vm.balance = 5.0
    result = vm.purchase_item('B')
    assert result is False

from solution import VendingMachine as _case3_VendingMachine

def test_p5_restock_existing():
    """P5: Restock existing product increases quantity."""
    vm = _case3_VendingMachine()
    vm.inventory = {'C': {'price': 1.5, 'quantity': 2}}
    result = vm.restock_item('C', 3)
    assert result is True
    assert vm.inventory['C']['quantity'] == 5

from solution import VendingMachine as _case4_VendingMachine

def test_p7_empty_display():
    """P7: Display items when inventory is empty."""
    vm = _case4_VendingMachine()
    result = vm.display_items()
    assert result is False

from solution import VendingMachine as _case5_VendingMachine

def test_p8_display_formatted():
    """P8: Display formatted product string."""
    vm = _case5_VendingMachine()
    vm.inventory = {'E': {'price': 3.5, 'quantity': 4}}
    result = vm.display_items()
    assert result == 'E - $3.5 [4]'

from solution import VendingMachine as _case6_VendingMachine

def test_extra_multiple_items_display():
    """Extra: Display multiple items produces multi-line string."""
    vm = _case6_VendingMachine()
    vm.inventory = {'A': {'price': 1.0, 'quantity': 5}, 'B': {'price': 2.0, 'quantity': 3}}
    result = vm.display_items()
    assert isinstance(result, str)
    lines = result.split('\n')
    assert len(lines) == 2
    assert 'A - $1.0 [5]' in result
    assert 'B - $2.0 [3]' in result

from solution import VendingMachine as _case7_VendingMachine

def test_extra_purchase_insufficient_balance():
    """Extra: Purchase fails when balance is insufficient."""
    vm = _case7_VendingMachine()
    vm.inventory = {'X': {'price': 5.0, 'quantity': 1}}
    vm.balance = 3.0
    result = vm.purchase_item('X')
    assert result is False
    assert vm.balance == 3.0
    assert vm.inventory['X']['quantity'] == 1

from solution import VendingMachine as _case8_VendingMachine

def test_extra_purchase_unknown_item():
    """Extra: Purchase fails for unknown item name."""
    vm = _case8_VendingMachine()
    vm.inventory = {'Y': {'price': 1.0, 'quantity': 1}}
    vm.balance = 10.0
    result = vm.purchase_item('Z')
    assert result is False
    assert vm.balance == 10.0
    assert vm.inventory == {'Y': {'price': 1.0, 'quantity': 1}}

from solution import VendingMachine as _case9_VendingMachine

def test_extra_cumulative_balance():
    """Extra: Multiple coin inserts accumulate balance."""
    vm = _case9_VendingMachine()
    r1 = vm.insert_coin(1.0)
    r2 = vm.insert_coin(2.5)
    r3 = vm.insert_coin(0.5)
    assert r1 == 1.0
    assert r2 == 3.5
    assert r3 == 4.0
    assert vm.balance == 4.0
