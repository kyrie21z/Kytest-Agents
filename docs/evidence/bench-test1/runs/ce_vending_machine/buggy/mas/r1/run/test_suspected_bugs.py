# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

from solution import VendingMachine

def test_p1_add_item_structure():
    v = VendingMachine()
    v.add_item('Coke', 1.25, 10)
    assert v.inventory == {'Coke': {'price': 1.25, 'quantity': 10}}

from solution import VendingMachine as _case7_VendingMachine

def test_p1_add_item_populates():
    """
P1: add_item populates inventory with correct structure.

Contract quote: "Adds a product to the vending machine's inventory.\n        :param item_name: The name of the product to be added, str.\n        :param price: The price of the product to be added, float.\n        :param quantity: The quantity of the product to be added, int.\n        :return: None\n        >>> vendingMachine = VendingMachine()\n        >>> vendingMachine.add_item('Coke', 1.25, 10)\n        >>> vendingMachine.inventory\n        {'Coke': {'price': 1.25, 'quantity': 10}}"

Input domain: Fresh VendingMachine instance; call add_item with a new item name,
valid float price, and positive int quantity.

Oracle: After add_item('Coke', 1.25, 10), the inventory dict must contain the key
'Coke' mapping to {'price': 1.25, 'quantity': 10}. The spec example explicitly
shows this expected state.

Fault hypothesis: The current implementation calls restock_item first; since
restock_item always returns True (due to setdefault creating a new entry),
the condition `if not self.restock_item(...)` is never satisfied, so the
assignment on line 27 is never reached. New items are silently not added.
"""
    v = _case7_VendingMachine()
    v.add_item('Coke', 1.25, 10)
    assert v.inventory == {'Coke': {'price': 1.25, 'quantity': 10}}

from solution import VendingMachine as _case8_VendingMachine

def test_extra_restock_nonexistent():
    """Extra: restock_item returns False when the item is not in inventory.

Contract quote: "Replenishes the inventory of a product already in the vending machine.\n        :param item_name: The name of the product to be replenished, str.\n        :param quantity: The quantity of the product to be replenished, int.\n        :return: If the product is already in the vending machine, returns True, otherwise, returns False.\n        >>> vendingMachine = VendingMachine()\n        >>> vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}\n        >>> vendingMachine.restock_item('Coke', 10)\n        True\n        >>> vendingMachine.restock_item('Pizza', 10)\n        False"

Input domain: Fresh VendingMachine instance; call restock_item with a name that
is not present in inventory.

Oracle: The method must return False for a non-existent item per the explicit
docstring example showing restock_item('Pizza', 10) returning False.

Fault hypothesis: The implementation uses setdefault to create a new entry
with price=0 and quantity=0, then adds the quantity, and unconditionally
returns True. This violates the contract and also silently adds the item
to inventory with price=0.
"""
    v = _case8_VendingMachine()
    # Ensure inventory is empty / no 'Pizza' exists
    v.inventory = {}
    result = v.restock_item('Pizza', 10)
    assert result is False
