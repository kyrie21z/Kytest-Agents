# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

"""Test that add_item correctly stores the price for a new item."""
from solution import VendingMachine

def test_add_item_sets_correct_price():
    vm = VendingMachine()
    vm.add_item('Sprite', 2.00, 20)
    assert vm.inventory['Sprite']['price'] == 2.00
    assert vm.inventory['Sprite']['quantity'] == 20

"""Test that restock_item returns False for non-existent items."""
from solution import VendingMachine

def test_restock_nonexistent_returns_false():
    vm = VendingMachine()
    result = vm.restock_item('Water', 15)
    assert result is False
