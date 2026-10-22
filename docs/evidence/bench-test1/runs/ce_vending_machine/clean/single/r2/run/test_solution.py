# Accepted by submit_tests; explanations in testgen_report.json.

def test_insert_coin_cumulative():
    """
    insert_coin should accumulate amounts and return the running total,
    not just the last inserted amount.
    """
    from solution import VendingMachine
    vm = VendingMachine()
    r1 = vm.insert_coin(1.25)
    assert r1 == 1.25
    r2 = vm.insert_coin(0.75)
    assert r2 == 2.0
    assert vm.balance == 2.0

def test_init_empty_state():
    """
    A freshly created VendingMachine should start with an empty inventory
    dictionary and a zero balance.
    """
    from solution import VendingMachine
    vm = VendingMachine()
    assert vm.inventory == {}
    assert vm.balance == 0

def test_add_item_creates_entry():
    """
    Adding a new item should create an inventory entry with the correct
    price and quantity, and add_item must return None.
    """
    from solution import VendingMachine
    vm = VendingMachine()
    result = vm.add_item('Coke', 1.25, 10)
    assert result is None
    assert vm.inventory == {'Coke': {'price': 1.25, 'quantity': 10}}

def test_add_item_restocks_existing():
    """
    Adding an item that already exists should restock (increase quantity)
    rather than overwrite the entry. Price must remain unchanged.
    """
    from solution import VendingMachine
    vm = VendingMachine()
    vm.add_item('Coke', 1.25, 10)
    vm.add_item('Coke', 1.5, 5)
    assert vm.inventory['Coke']['quantity'] == 15
    assert vm.inventory['Coke']['price'] == 1.25

def test_purchase_decrements_both():
    """
    A successful purchase must decrease both the machine's balance and
    the item's quantity by exactly one unit.
    """
    from solution import VendingMachine
    vm = VendingMachine()
    vm.inventory = {'Pepsi': {'price': 2.0, 'quantity': 3}}
    vm.balance = 5.0
    result = vm.purchase_item('Pepsi')
    assert result == 3.0
    assert vm.balance == 3.0
    assert vm.inventory['Pepsi']['quantity'] == 2

def test_display_items_multi_line():
    """
    With multiple items, display_items returns a single string with each
    item on its own line, formatted as 'Name - $Price [Qty]'.
    """
    from solution import VendingMachine
    vm = VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}, 'Pepsi': {'price': 1.5, 'quantity': 5}}
    result = vm.display_items()
    lines = result.split('\n')
    assert len(lines) == 2
    assert 'Coke - $1.25 [10]' in lines
    assert 'Pepsi - $1.5 [5]' in lines
    assert isinstance(result, str)
