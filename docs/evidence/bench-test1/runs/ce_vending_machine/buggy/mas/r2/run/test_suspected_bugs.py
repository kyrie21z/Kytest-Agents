# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

from solution import VendingMachine

def test_p2_add_new_item():
    """
    Contract quote: 'Adds a product to the vending machine\'s inventory.'
    Input domain: A fresh VendingMachine; call add_item('Coke', 1.25, 10).
    Oracle: Returns None; inventory becomes {'Coke': {'price': 1.25, 'quantity': 10}}.
    Fault hypothesis: If add_item silently fails or overwrites with wrong price/quantity,
      the inventory dict will not match the expected structure.
    """
    vm = VendingMachine()
    result = vm.add_item('Coke', 1.25, 10)
    assert result is None
    assert vm.inventory == {'Coke': {'price': 1.25, 'quantity': 10}}

from solution import VendingMachine

def test_p7_restock_not_in_inventory():
    """
    Contract quote: ':return: If the product is already in the vending machine, returns True, otherwise, returns False.'
    Input domain: VM with empty inventory; call restock_item('Water', 5).
    Oracle: Returns False.
    Fault hypothesis: If restock_item always returns True (as the buggy implementation does via
      setdefault), this test will catch the deviation from the spec.
    """
    vm = VendingMachine()
    vm.inventory = {}
    result = vm.restock_item('Water', 5)
    assert result is False

from solution import VendingMachine

def test_p9_display_single_item():
    """
    Contract quote: ':return: If the vending machine is empty, returns False, otherwise, returns a list of the products in the vending machine, str.'
    Input domain: VM with inventory={'Soda':{'price':1.50,'quantity':3}}; call display_items().
    Oracle: Returns 'Soda - $1.50 [3]'.
    Fault hypothesis: If display_items formats the string incorrectly (wrong separator, wrong order),
      the assertion will catch it.
    """
    vm = VendingMachine()
    vm.inventory = {'Soda': {'price': 1.50, 'quantity': 3}}
    result = vm.display_items()
    assert result == 'Soda - $1.50 [3]'
