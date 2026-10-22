# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

from solution import VendingMachine

def test_add_item_creates_new_entry():
    """
    Contract quote: 'Adds a product to the vending machine\'s inventory.'
    Input domain: Fresh VendingMachine, add_item('Coke', 1.25, 10)
    Oracle: After adding a new item, inventory must contain that item with
            the exact price and quantity provided.
    Fault hypothesis: restock_item always returns True via setdefault,
            so the new-item branch in add_item never executes; price may be
            left at default 0 instead of the supplied value.
    """
    vm = VendingMachine()
    vm.add_item('Coke', 1.25, 10)
    assert 'Coke' in vm.inventory
    assert vm.inventory['Coke']['price'] == 1.25
    assert vm.inventory['Coke']['quantity'] == 10
