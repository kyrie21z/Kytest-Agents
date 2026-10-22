# Accepted by submit_tests; explanations in testgen_report.json.

from solution import VendingMachine as _case0_VendingMachine

def test_p2_add_new_product():
    """P2: Add a new product to inventory with correct structure."""
    v = _case0_VendingMachine()
    result = v.add_item('Coke', 1.25, 10)
    assert result is None
    assert v.inventory['Coke'] == {'price': 1.25, 'quantity': 10}

from solution import VendingMachine as _case1_VendingMachine

def test_p4_purchase_exact_balance():
    """P4: Purchase item with exact balance — balance should become 0.0."""
    v = _case1_VendingMachine()
    v.inventory = {'Coke': {'price': 1.25, 'quantity': 5}}
    v.balance = 1.25
    result = v.purchase_item('Coke')
    assert result == 0.0

from solution import VendingMachine as _case2_VendingMachine

def test_p5_out_of_stock_purchase():
    """P5: Attempt purchase when out of stock — should return False."""
    v = _case2_VendingMachine()
    v.inventory = {'Soda': {'price': 1.0, 'quantity': 0}}
    v.balance = 1.0
    assert v.purchase_item('Soda') is False

from solution import VendingMachine as _case3_VendingMachine

def test_p6_restock_existing_item():
    """P6: Restock an existing item — returns True and increments quantity."""
    v = _case3_VendingMachine()
    v.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    result = v.restock_item('Coke', 5)
    assert result is True
    assert v.inventory['Coke']['quantity'] == 15

from solution import VendingMachine as _case4_VendingMachine

def test_p1_init_state():
    """P1: Initialize machine state — inventory is empty dict and balance is 0."""
    v = _case4_VendingMachine()
    assert v.inventory == {}
    assert v.balance == 0

from solution import VendingMachine as _case5_VendingMachine

def test_p3_insert_coin_returns_balance():
    """P3: Insert coins and verify returned balance matches inserted amount."""
    v = _case5_VendingMachine()
    assert v.insert_coin(2.5) == 2.5

from solution import VendingMachine as _case6_VendingMachine

def test_p7_display_empty_inventory():
    """P7: Display items when inventory is empty — returns False."""
    v = _case6_VendingMachine()
    assert v.display_items() is False

from solution import VendingMachine as _case7_VendingMachine

def test_p8_display_single_item():
    """P8: Display items when inventory has one product — formatted string."""
    v = _case7_VendingMachine()
    v.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    assert v.display_items() == 'Coke - $1.25 [10]'

from solution import VendingMachine as _case8_VendingMachine

def test_p9_transaction_sequence_invariant():
    """P9: Transaction sequence invariant — balance and quantity stay consistent."""
    v = _case8_VendingMachine()
    v.add_item('X', 5.0, 2)
    v.insert_coin(5.0)
    v.purchase_item('X')
    assert v.balance == 0.0
    assert v.inventory['X']['quantity'] == 1

from solution import VendingMachine as _case9_VendingMachine

def test_p10_insert_zero_coin():
    """P10: Insert zero-value coin — returns current balance (0.0)."""
    v = _case9_VendingMachine()
    assert v.insert_coin(0.0) == 0.0

from solution import VendingMachine as _case10_VendingMachine

def test_extra_purchase_insufficient_funds():
    """Extra: Purchase fails when balance is less than price even if in stock."""
    v = _case10_VendingMachine()
    v.inventory = {'Coke': {'price': 1.25, 'quantity': 5}}
    v.balance = 1.0
    assert v.purchase_item('Coke') is False

from solution import VendingMachine as _case11_VendingMachine

def test_extra_purchase_nonexistent_item():
    """Extra: Purchase of item not in inventory returns False."""
    v = _case11_VendingMachine()
    v.inventory = {'Coke': {'price': 1.25, 'quantity': 5}}
    v.balance = 10.0
    assert v.purchase_item('Pizza') is False

from solution import VendingMachine as _case12_VendingMachine

def test_extra_restock_nonexistent_item():
    """Extra: Restocking a non-existent item returns False."""
    v = _case12_VendingMachine()
    v.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    assert v.restock_item('Pizza', 5) is False

from solution import VendingMachine as _case13_VendingMachine

def test_extra_multiple_purchases_decrement_quantity():
    """Extra: Multiple purchases decrement quantity correctly."""
    v = _case13_VendingMachine()
    v.add_item('Coke', 1.25, 3)
    v.insert_coin(5.0)
    v.purchase_item('Coke')
    v.purchase_item('Coke')
    v.purchase_item('Coke')
    assert v.inventory['Coke']['quantity'] == 0
    assert v.balance == 5.0 - 1.25 * 3

from solution import VendingMachine as _case14_VendingMachine

def test_extra_display_multiple_items():
    """Extra: Display multiple items returns newline-separated strings."""
    v = _case14_VendingMachine()
    v.inventory = {'Coke': {'price': 1.25, 'quantity': 10}, 'Pepsi': {'price': 1.5, 'quantity': 5}}
    result = v.display_items()
    assert isinstance(result, str)
    assert 'Coke - $1.25 [10]' in result
    assert 'Pepsi - $1.5 [5]' in result

from solution import VendingMachine as _case15_VendingMachine

def test_extra_add_item_to_existing_updates_quantity_only():
    """Extra: Adding an item that already exists only restocks quantity, not price."""
    v = _case15_VendingMachine()
    v.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    v.add_item('Coke', 2.0, 5)
    assert v.inventory['Coke']['price'] == 1.25
    assert v.inventory['Coke']['quantity'] == 15
