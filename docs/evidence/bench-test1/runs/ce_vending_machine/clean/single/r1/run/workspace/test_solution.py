# Accepted by submit_tests; explanations in testgen_report.json.

def test_add_item_creates_entry():
    """
    Contract quote: "{'Coke': {'price': 1.25, 'quantity': 10}}"
    Input domain: Add a new item 'Coke' with price 1.25 and quantity 10.
    Expected result: inventory contains 'Coke' with price 1.25 and quantity 10.
    Fault hypothesis: The price or quantity could be stored incorrectly (swapped, truncated, or missing).
    """
    from solution import VendingMachine
    vm = VendingMachine()
    vm.add_item('Coke', 1.25, 10)
    assert vm.inventory['Coke']['price'] == 1.25
    assert vm.inventory['Coke']['quantity'] == 10

def test_display_items_format():
    """
    Contract quote: "'Coke - $1.25 [10]'"
    Input domain: Inventory with one item having price 1.25 and quantity 10.
    Expected result: Returns the string 'Coke - $1.25 [10]'.
    Fault hypothesis: The format string might be incorrect (wrong separators, missing fields, etc.).
    """
    from solution import VendingMachine
    vm = VendingMachine()
    vm.inventory['Coke'] = {'price': 1.25, 'quantity': 10}
    result = vm.display_items()
    assert result == 'Coke - $1.25 [10]'

def test_init_empty_state():
    """
    Contract quote: 'Initializes the vending machine's inventory and balance.'
    Input domain: Instantiate VendingMachine with no arguments.
    Expected result: inventory is an empty dict and balance is 0.
    Fault hypothesis: A faulty __init__ might initialize inventory with default items or balance with a non-zero value.
    """
    from solution import VendingMachine
    vm = VendingMachine()
    assert vm.inventory == {}
    assert vm.balance == 0

def test_purchase_successful():
    """
    Contract quote: 'If successful, returns the balance of the vending machine after the product is purchased, float,otherwise,returns False.'
    Input domain: Item exists with quantity > 0 and balance >= price.
    Expected result: Balance is reduced by the item's price, quantity is decremented by 1, and the new balance is returned.
    Fault hypothesis: The balance might not be reduced, quantity might not be decremented, or the wrong value might be returned.
    """
    from solution import VendingMachine
    vm = VendingMachine()
    vm.inventory['Coke'] = {'price': 1.25, 'quantity': 10}
    vm.balance = 5.0
    result = vm.purchase_item('Coke')
    assert result == 3.75
    assert vm.inventory['Coke']['quantity'] == 9
    assert vm.balance == 3.75

def test_restock_existing_increases_quantity():
    """
    Contract quote: 'Replenishes the inventory of a product already in the vending machine.'
    Input domain: Restock an existing item with a positive quantity.
    Expected result: The item's quantity is increased by the restock amount, and True is returned.
    Fault hypothesis: The quantity might not be incremented, or the method might return False incorrectly.
    """
    from solution import VendingMachine
    vm = VendingMachine()
    vm.inventory['Coke'] = {'price': 1.25, 'quantity': 10}
    result = vm.restock_item('Coke', 5)
    assert result is True
    assert vm.inventory['Coke']['quantity'] == 15

def test_add_item_existing_unchanged():
    """
    Contract quote: 'Adds a product to the vending machine's inventory.'
    Input domain: Add an item that already exists with different price and quantity.
    Expected result: The existing item's price remains unchanged, but quantity is increased by restock amount via restock_item.
    Fault hypothesis: A buggy implementation might overwrite both price and quantity instead of just restocking.
    """
    from solution import VendingMachine
    vm = VendingMachine()
    vm.inventory['Coke'] = {'price': 1.25, 'quantity': 10}
    vm.add_item('Coke', 2.0, 5)
    assert vm.inventory['Coke']['price'] == 1.25
    assert vm.inventory['Coke']['quantity'] == 15

def test_purchase_insufficient_funds():
    """
    Contract quote: 'If successful, returns the balance of the vending machine after the product is purchased, float,otherwise,returns False.'
    Input domain: Item exists with sufficient quantity but balance < price.
    Expected result: Returns False without modifying balance or quantity.
    Fault hypothesis: The purchase might succeed despite insufficient funds, or the balance might be incorrectly modified.
    """
    from solution import VendingMachine
    vm = VendingMachine()
    vm.inventory['Coke'] = {'price': 1.25, 'quantity': 10}
    vm.balance = 1.0
    result = vm.purchase_item('Coke')
    assert result is False
    assert vm.balance == 1.0
    assert vm.inventory['Coke']['quantity'] == 10

def test_purchase_out_of_stock():
    """
    Contract quote: 'If successful, returns the balance of the vending machine after the product is purchased, float,otherwise,returns False.'
    Input domain: Item exists but quantity is 0, balance >= price.
    Expected result: Returns False without modifying balance.
    Fault hypothesis: The purchase might proceed even when quantity is zero.
    """
    from solution import VendingMachine
    vm = VendingMachine()
    vm.inventory['Coke'] = {'price': 1.25, 'quantity': 0}
    vm.balance = 5.0
    result = vm.purchase_item('Coke')
    assert result is False
    assert vm.balance == 5.0

def test_purchase_nonexistent_item():
    """
    Contract quote: 'If successful, returns the balance of the vending machine after the product is purchased, float,otherwise,returns False.'
    Input domain: Item does not exist in inventory.
    Expected result: Returns False.
    Fault hypothesis: The method might raise KeyError or return a non-False value for nonexistent items.
    """
    from solution import VendingMachine
    vm = VendingMachine()
    vm.inventory['Coke'] = {'price': 1.25, 'quantity': 10}
    vm.balance = 5.0
    result = vm.purchase_item('Pizza')
    assert result is False

def test_display_items_empty():
    """
    Contract quote: 'If the vending machine is empty, returns False'
    Input domain: Inventory is empty.
    Expected result: Returns False.
    Fault hypothesis: The method might return an empty string or raise an error instead of False.
    """
    from solution import VendingMachine
    vm = VendingMachine()
    result = vm.display_items()
    assert result is False

def test_restock_nonexistent_returns_false():
    """
    Contract quote: 'If the product is already in the vending machine, returns True, otherwise, returns False.'
    Input domain: Attempt to restock an item that does not exist in inventory.
    Expected result: Returns False and inventory is unchanged.
    Fault hypothesis: The method might create a new entry or raise an error for nonexistent items.
    """
    from solution import VendingMachine
    vm = VendingMachine()
    vm.inventory['Coke'] = {'price': 1.25, 'quantity': 10}
    result = vm.restock_item('Pizza', 5)
    assert result is False
    assert 'Pizza' not in vm.inventory
