# Suspected implementation bugs

## test_add_item_sets_correct_price

- Reviewer: The test strictly follows the specification and its doctest example, which require add_item to store the provided price and quantity verbatim. The implementation incorrectly delegates to restock_item (which always returns True), preventing the price/quantity assignment and leaving the price at 0.

```
F                                                                        [100%]
=================================== FAILURES ===================================
_______________________ test_add_item_sets_correct_price _______________________
test_solution.py:7: in test_add_item_sets_correct_price
    assert vm.inventory['Sprite']['price'] == 2.00
E   assert 0 == 2.0
=========================== short test summary info ============================
FAILED test_solution.py::test_add_item_sets_correct_price - assert 0 == 2.0
1 failed in 0.01s
```

## test_restock_nonexistent_returns_false

- Reviewer: The specification explicitly mandates that restock_item returns False when the item is not already in the inventory, confirmed by a direct doctest. The implementation unconditionally returns True and auto-creates entries with default values, directly violating the stated contract.

```
F                                                                        [100%]
=================================== FAILURES ===================================
____________________ test_restock_nonexistent_returns_false ____________________
test_solution.py:7: in test_restock_nonexistent_returns_false
    assert result is False
E   assert True is False
=========================== short test summary info ============================
FAILED test_solution.py::test_restock_nonexistent_returns_false - assert True...
1 failed in 0.01s
```
