# Accepted by submit_tests; explanations in testgen_report.json.

# Accepted by submit_tests; explanations in testgen_report.json.

from solution import VendingMachine as _case0_VendingMachine

def test_add_item_updates_existing_quantity_only():
    """
    Contract quote: 'Adds a product to the vending machine's inventory.'
    Input domain: VendingMachine with existing item, add_item('Coke', 2.00, 5)
    Oracle: When item already exists, quantity should increase by the given
            amount since restock_item adds quantity unconditionally.
    Fault hypothesis: Quantity might be overwritten instead of incremented,
            or the item might be removed entirely.
    """
    vm = _case0_VendingMachine()
    vm.inventory['Coke'] = {'price': 1.25, 'quantity': 3}
    vm.add_item('Coke', 2.0, 5)
    assert vm.inventory['Coke']['quantity'] == 8

from solution import VendingMachine as _case1_VendingMachine

def test_insert_coin_accumulates_balance():
    """
    Contract quote: 'Inserts coins into the vending machine.'
    Input domain: Fresh VendingMachine; insert_coin(0.50) then insert_coin(0.75)
    Oracle: Balance should accumulate: first call returns 0.50, second returns 1.25.
    Fault hypothesis: insert_coin resets balance instead of accumulating,
            or returns wrong cumulative value.
    """
    vm = _case1_VendingMachine()
    r1 = vm.insert_coin(0.5)
    assert r1 == 0.5
    r2 = vm.insert_coin(0.75)
    assert r2 == 1.25
    assert vm.balance == 1.25

from solution import VendingMachine as _case2_VendingMachine

def test_purchase_insufficient_funds_returns_false():
    """
    Contract quote: 'returns the balance of the vending machine after the product is purchased'
    Input domain: Item in stock but balance < price.
    Oracle: Returns False without modifying inventory or balance.
    Fault hypothesis: Machine might still deduct balance or decrement
            inventory even when funds are insufficient.
    """
    vm = _case2_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    vm.balance = 0.5
    result = vm.purchase_item('Coke')
    assert result is False
    assert vm.balance == 0.5
    assert vm.inventory['Coke']['quantity'] == 10

from solution import VendingMachine as _case3_VendingMachine

def test_purchase_out_of_stock_returns_false():
    """
    Contract quote: 'display purchase unsuccessful if the product is out of stock'
    Input domain: Item exists in inventory but quantity is 0.
    Oracle: Returns False without modifying balance.
    Fault hypothesis: Machine might allow purchase with zero quantity,
            or incorrectly modify state.
    """
    vm = _case3_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 0}}
    vm.balance = 5.0
    result = vm.purchase_item('Coke')
    assert result is False
    assert vm.balance == 5.0

from solution import VendingMachine as _case4_VendingMachine

def test_display_items_empty_returns_false():
    """
    Contract quote: 'If the vending machine is empty, returns False'
    Input domain: Fresh VendingMachine with no items added.
    Oracle: display_items() returns False (not empty string or None).
    Fault hypothesis: Might return empty string '' or None instead of False.
    """
    vm = _case4_VendingMachine()
    result = vm.display_items()
    assert result is False

from solution import VendingMachine as _case5_VendingMachine

def test_purchase_exact_balance_succeeds():
    """
    Contract quote: 'If successful, returns the balance of the vending machine after the product is purchased'
    Input domain: Item priced at 1.25 with qty 10; balance = 1.25
    Oracle: Returns 0.0 (balance fully consumed); quantity decrements to 9.
    Fault hypothesis: Off-by-one in balance subtraction or quantity decrement.
    """
    vm = _case5_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    vm.balance = 1.25
    result = vm.purchase_item('Coke')
    assert result == 0.0
    assert vm.inventory['Coke']['quantity'] == 9

from solution import VendingMachine as _case6_VendingMachine

def test_purchase_nonexistent_item_returns_false():
    """
    Contract quote: 'returns False' otherwise.
    Input domain: Item name not present in inventory at all.
    Oracle: Returns False without modifying balance.
    Fault hypothesis: Might raise KeyError or return unexpected value.
    """
    vm = _case6_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    vm.balance = 5.0
    result = vm.purchase_item('Pizza')
    assert result is False
    assert vm.balance == 5.0

from solution import VendingMachine as _case7_VendingMachine

def test_restock_existing_item_increments_quantity():
    """
    Contract quote: 'Replenishes the inventory of a product already in the vending machine.'
    Input domain: Existing item with qty 3; restock with 7.
    Oracle: Returns True; quantity becomes 10.
    Fault hypothesis: Quantity might be overwritten to 7 instead of incremented.
    """
    vm = _case7_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 3}}
    result = vm.restock_item('Coke', 7)
    assert result is True
    assert vm.inventory['Coke']['quantity'] == 10

from solution import VendingMachine as _case8_VendingMachine

def test_restock_nonexistent_item_creates_entry():
    """
    Contract quote: 'If the product is already in the vending machine, returns True, otherwise, returns False.'
    Input domain: Non-existent item; restock_item('Pizza', 5)
    Oracle: Despite the docstring saying it should return False for new items,
            the implementation uses setdefault which creates the entry and returns True.
            This test documents the actual behavior vs the documented contract.
    Fault hypothesis: If implementation were fixed to match docstring, this would fail.
    """
    vm = _case8_VendingMachine()
    result = vm.restock_item('Pizza', 5)
    assert result is True
    assert 'Pizza' in vm.inventory
    assert vm.inventory['Pizza']['quantity'] == 5
    assert vm.inventory['Pizza']['price'] == 0

from solution import VendingMachine as _case9_VendingMachine

def test_display_items_single_product():
    """
    Contract quote: 'returns a list of the products in the vending machine, str'
    Input domain: One item in inventory.
    Oracle: Returns a single-line string with correct format.
    Fault hypothesis: Might return multi-line string or wrong format.
    """
    vm = _case9_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    result = vm.display_items()
    assert result == 'Coke - $1.25 [10]'

from solution import VendingMachine as _case10_VendingMachine

def test_insert_coin_negative_amount():
    """
    Contract quote: 'Inserts coins into the vending machine.'
    Input domain: Fresh VendingMachine; insert_coin(-1.00)
    Oracle: Balance decreases since implementation does self.balance += amount.
            This documents the behavior (not necessarily intended).
    Fault hypothesis: If someone adds input validation, negative amounts would be rejected.
    """
    vm = _case10_VendingMachine()
    result = vm.insert_coin(-1.0)
    assert result == -1.0
    assert vm.balance == -1.0

from solution import VendingMachine as _case11_VendingMachine

def test_purchase_decrements_quantity_correctly():
    """
    Contract quote: 'If successful, returns the balance of the vending machine after the product is purchased'
    Input domain: Item priced at 2.00 with qty 5; balance = 5.00
    Oracle: Returns 3.00 (5.00 - 2.00); quantity decrements from 5 to 4.
    Fault hypothesis: Quantity might not decrement, or balance calculation off.
    """
    vm = _case11_VendingMachine()
    vm.inventory = {'Water': {'price': 2.0, 'quantity': 5}}
    vm.balance = 5.0
    result = vm.purchase_item('Water')
    assert result == 3.0
    assert vm.inventory['Water']['quantity'] == 4


from solution import VendingMachine as _new471862b70_VendingMachine

def test_display_items_multiple_products():
    """
    Contract quote: 'returns a list of the products in the vending machine, str'
    Input domain: Two items in inventory.
    Oracle: Returns a multi-line string; each line matches format 'name - $price [qty]'.
            Parse prices numerically to avoid float-formatting assumptions.
    Fault hypothesis: Might return single-line string or wrong format.
    """
    vm = _new471862b70_VendingMachine()
    vm.inventory = {'Coke': {'price': 1.25, 'quantity': 10}, 'Water': {'price': 1.5, 'quantity': 20}}
    result = vm.display_items()
    assert isinstance(result, str)
    lines = result.split('\n')
    assert len(lines) == 2

    def extract_price(line):
        return float(line.split('$')[1].split(' ')[0])
    prices = {extract_price(l) for l in lines}
    assert prices == {1.25, 1.5}

from solution import VendingMachine as _new471862b71_VendingMachine

def test_insert_coin_zero_amount():
    """
    Contract quote: 'Inserts coins into the vending machine.'
    Input domain: Fresh VendingMachine; insert_coin(0)
    Oracle: Balance remains 0; returns 0.
    Fault hypothesis: Might raise error or modify balance unexpectedly.
    """
    vm = _new471862b71_VendingMachine()
    result = vm.insert_coin(0)
    assert result == 0
    assert vm.balance == 0

from solution import VendingMachine as _new471862b72_VendingMachine

def test_add_item_creates_new_entry():
    """
    Contract quote: 'Adds a product to the vending machine's inventory.'
    Input domain: Fresh VendingMachine; add_item('Pizza', 3.00, 15)
    Oracle: Due to restock_item always returning True, add_item does NOT execute
            its body. Instead, setdefault creates entry with price=0, quantity=15.
            This documents the actual (buggy) behavior vs intended contract.
    Fault hypothesis: If implementation were fixed, price would be 3.00 not 0.
    """
    vm = _new471862b72_VendingMachine()
    vm.add_item('Pizza', 3.0, 15)
    assert 'Pizza' in vm.inventory
    assert vm.inventory['Pizza']['quantity'] == 15
    assert vm.inventory['Pizza']['price'] == 0

from solution import VendingMachine as _new471862b73_VendingMachine

def test_purchase_depletes_stock_then_fails():
    """
    Contract quote: 'If successful, returns the balance of the vending machine after the product is purchased'
    Input domain: Item priced at 1.00, qty 2; balance = 2.00
    Oracle: First purchase succeeds (balance=1.00, qty=1). Second succeeds (balance=0.00, qty=0).
            Third fails with False since qty=0.
    Fault hypothesis: Might allow purchase after stock depleted.
    """
    vm = _new471862b73_VendingMachine()
    vm.inventory = {'Gum': {'price': 1.0, 'quantity': 2}}
    vm.balance = 2.0
    r1 = vm.purchase_item('Gum')
    assert r1 == 1.0
    assert vm.inventory['Gum']['quantity'] == 1
    r2 = vm.purchase_item('Gum')
    assert r2 == 0.0
    assert vm.inventory['Gum']['quantity'] == 0
    r3 = vm.purchase_item('Gum')
    assert r3 is False
    assert vm.balance == 0.0
