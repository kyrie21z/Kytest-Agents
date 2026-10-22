# Suspected implementation bugs

## test_p2_add_new_item

- Plan P2: Add a new product to the inventory. — input `v.add_item('Coke', 1.25, 10)`, expected `Returns None; v.inventory == {'Coke': {'price': 1.25, 'quantity': 10}}`
- Reviewer: The test follows the spec docstring example requiring the inventory to store the exact price provided. The implementation's restock_item incorrectly initializes missing items with price 0 and always returns True, preventing add_item from storing the correct price.

```
____________ test_p2_add_new_item _____________________________
test_solution.py:14: in test_p2_add_new_item
    assert vm.inventory == {'Coke': {'price': 1.25, 'quantity': 10}}
E   AssertionError: assert {'Coke': {'pr...uantity': 10}} == {'Coke': {'pr...uantity': 10}}
E     
E     Differing items:
E     {'Coke': {'price': 0, 'quantity': 10}} != {'Coke': {'price': 1.25, 'quantity': 10}}
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p2_add_new_item - AssertionError: assert {'Coke...
1 failed in 0.01s
```

## test_p7_restock_not_in_inventory

- Plan P7: Attempt to restock a product not currently in inventory. — input `v.inventory={}, v.restock_item('Water', 5)`, expected `Returns False`
- Reviewer: The spec explicitly requires restock_item to return False for items not currently in inventory. The implementation uses setdefault which creates the item entry and unconditionally returns True, directly violating the specification.

```
F                                                                        [100%]
=================================== FAILURES ===================================
_______________________ test_p7_restock_not_in_inventory _______________________
test_solution.py:14: in test_p7_restock_not_in_inventory
    assert result is False
E   assert True is False
=========================== short test summary info ============================
FAILED test_solution.py::test_p7_restock_not_in_inventory - assert True is False
1 failed in 0.01s
```

## test_p9_display_single_item

- Plan P9: Display status for a single product. — input `v.inventory={'Soda':{'price':1.50,'quantity':3}}, v.display_items()`, expected `Returns 'Soda - $1.50 [3]'`
- Reviewer: The spec's docstring example demonstrates currency formatted to two decimal places ($1.25). The test correctly expects this standard formatting ($1.50), but the implementation uses Python's default float representation ($1.5), failing to match the specified display format.

```
[100%]
=================================== FAILURES ===================================
_________________________ test_p9_display_single_item __________________________
test_solution.py:14: in test_p9_display_single_item
    assert result == 'Soda - $1.50 [3]'
E   AssertionError: assert 'Soda - $1.5 [3]' == 'Soda - $1.50 [3]'
E     
E     - Soda - $1.50 [3]
E     ?            -
E     + Soda - $1.5 [3]
=========================== short test summary info ============================
FAILED test_solution.py::test_p9_display_single_item - AssertionError: assert...
1 failed in 0.01s
```
