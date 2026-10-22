# Accepted by submit_tests; explanations in testgen_report.json.

"""Verify initial inventory and balance are empty/zero upon construction.

Docstring quote: 'Initializes the vending machine's inventory and balance.'
Implementation: self.inventory = {}; self.balance = 0
Input domain: VendingMachine() with no arguments.
Expected result: inventory is an empty dict and balance is integer 0.
Fault hypothesis: If __init__ failed to set either attribute, or set
  balance to a non-zero default, this assertion would catch it.
"""
import solution as _case0_solution

def test_p1_initial_state():
    vm = _case0_solution.VendingMachine()
    assert vm.inventory == {}
    assert vm.balance == 0

"""Add a new product to the inventory with correct nested-dict structure.

Docstring quote: "Adds a product to the vending machine's inventory."
Doctest example: add_item('Coke', 1.25, 10) -> {'Coke': {'price': 1.25, 'quantity': 10}}
Input domain: fresh VendingMachine, call add_item('Water', 2.0, 5).
Expected result: inventory maps 'Water' to {'price': 2.0, 'quantity': 5}.
Fault hypothesis: If add_item replaced the whole dict or stored flat keys,
  the nested structure assertion would fail.
"""
import solution as _case1_solution

def test_p2_add_new_product():
    vm = _case1_solution.VendingMachine()
    vm.add_item('Water', 2.0, 5)
    assert vm.inventory == {'Water': {'price': 2.0, 'quantity': 5}}

"""Successful purchase deducts price from balance and reduces stock.

Docstring quote: 'If successful, returns the balance of the vending
  machine after the product is purchased, float'.
Input domain: inventory={'A':{'price':2.0,'quantity':1}}, balance=5.0;
  call purchase_item('A').
Expected result: returns 3.0 (5.0 - 2.0); quantity drops to 0;
  balance becomes 3.0.
Fault hypothesis: If the method failed to subtract price or decrement
  quantity, the returned balance or stock count would be wrong.
"""
import solution as _case2_solution

def test_p4_successful_purchase():
    vm = _case2_solution.VendingMachine()
    vm.inventory = {'A': {'price': 2.0, 'quantity': 1}}
    vm.balance = 5.0
    result = vm.purchase_item('A')
    assert result == 3.0
    assert vm.inventory['A']['quantity'] == 0
    assert vm.balance == 3.0

"""Accumulate balance across multiple coin insertions.

Docstring quote: 'Inserts coins into the vending machine.'
Input domain: fresh VendingMachine, insert_coin(0.75) then insert_coin(0.25).
Expected result: cumulative balance is 1.0; first call returns 0.75,
  second returns 1.0.
Fault hypothesis: If insert_coin overwrote balance instead of adding,
  the final balance would be 0.25 rather than 1.0.
"""
import solution as _case3_solution

def test_p3_accumulate_balance():
    vm = _case3_solution.VendingMachine()
    r1 = vm.insert_coin(0.75)
    r2 = vm.insert_coin(0.25)
    assert vm.balance == 1.0
    assert r1 == 0.75
    assert r2 == 1.0

"""Attempt to purchase when item quantity is zero - must return False.

Docstring quote: 'display purchase unsuccessful if the product is out of stock.'
Input domain: inventory={'B':{'price':1.0,'quantity':0}}, balance=5.0;
  call purchase_item('B').
Expected result: returns False because quantity is 0.
Fault hypothesis: If the method ignored quantity and allowed the purchase,
  it would return a float instead of False.
"""
import solution as _case4_solution

def test_p5_out_of_stock_purchase():
    vm = _case4_solution.VendingMachine()
    vm.inventory = {'B': {'price': 1.0, 'quantity': 0}}
    vm.balance = 5.0
    result = vm.purchase_item('B')
    assert result is False

"""Replenish quantity of an existing item - additive update.

Docstring quote: 'Replenishes the inventory of a product already in the vending machine.'
Input domain: inventory={'C':{'price':3.0,'quantity':2}};
  call restock_item('C', 5).
Expected result: returns True; quantity becomes 2 + 5 = 7.
Fault hypothesis: If restock_item replaced quantity instead of adding,
  the quantity would be 5 instead of 7.
"""
import solution as _case5_solution

def test_p6_replenish_existing():
    vm = _case5_solution.VendingMachine()
    vm.inventory = {'C': {'price': 3.0, 'quantity': 2}}
    result = vm.restock_item('C', 5)
    assert result is True
    assert vm.inventory['C']['quantity'] == 7

"""Display format matches documented example for a single item.

Docstring quote: doctest shows 'Coke - $1.25 [10]'.
Input domain: inventory={'D':{'price':4.5,'quantity':1}};
  call display_items().
Expected result: returns the exact string 'D - $4.5 [1]'.
Fault hypothesis: If formatting used different delimiters, omitted the
  dollar sign, or swapped fields, the string comparison would fail.
"""
import solution as _case6_solution

def test_p8_display_format():
    vm = _case6_solution.VendingMachine()
    vm.inventory = {'D': {'price': 4.5, 'quantity': 1}}
    result = vm.display_items()
    assert result == 'D - $4.5 [1]'

"""Display items when inventory is empty - must return False.

Docstring quote: 'If the vending machine is empty, returns False, otherwise,
  returns a list of the products in the vending machine, str.'
Input domain: fresh VendingMachine (empty inventory); call display_items().
Expected result: returns False.
Fault hypothesis: If the method returned an empty string or list instead
  of False, this assertion would catch it.
"""
import solution as _case7_solution

def test_p7_empty_display():
    vm = _case7_solution.VendingMachine()
    result = vm.display_items()
    assert result is False

"""Purchase a non-existent item - must return False.

Docstring quote: 'Purchases a product from the vending machine and returns
  the balance after the purchase and display purchase unsuccessful if the
  product is out of stock.'
Input domain: fresh VendingMachine; call purchase_item('Ghost').
Expected result: returns False because 'Ghost' is not in inventory.
Fault hypothesis: If the method raised KeyError or returned a sentinel
  other than False, this assertion would fail.
"""
import solution as _case8_solution

def test_p9_nonexistent_purchase():
    vm = _case8_solution.VendingMachine()
    result = vm.purchase_item('Ghost')
    assert result is False

"""Restock an item not currently in inventory - must return False.

Docstring quote: 'Replenishes the inventory of a product already in the
  vending machine.'
Input domain: fresh VendingMachine; call restock_item('Ghost', 10).
Expected result: returns False.
Fault hypothesis: If the method silently created a new entry instead of
  returning False, the inventory would change unexpectedly.
"""
import solution as _case9_solution

def test_p10_nonexistent_restock():
    vm = _case9_solution.VendingMachine()
    result = vm.restock_item('Ghost', 10)
    assert result is False
