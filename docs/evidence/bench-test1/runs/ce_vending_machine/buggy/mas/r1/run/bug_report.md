# Suspected implementation bugs

## test_p1_add_item_structure

- Plan P1: add_item populates inventory with correct structure — input `v.add_item('Coke', 1.25, 10)`, expected `v.inventory == {'Coke': {'price': 1.25, 'quantity': 10}}`
- Reviewer: The test correctly follows the specification and docstring example. The implementation violates the spec: `restock_item` unconditionally returns `True` and uses `setdefault` to initialize missing items with `price: 0`. As a result, `add_item`'s guard `if not self.restock_item(...)` is always false, preventing the correct price from being stored. The spec explicitly requires `add_item` to set the provided price and `restock_item` to return `False` for non-existent items.

```
_____ test_p1_add_item_structure __________________________
test_solution.py:6: in test_p1_add_item_structure
    assert v.inventory == {'Coke': {'price': 1.25, 'quantity': 10}}
E   AssertionError: assert {'Coke': {'pr...uantity': 10}} == {'Coke': {'pr...uantity': 10}}
E     
E     Differing items:
E     {'Coke': {'price': 0, 'quantity': 10}} != {'Coke': {'price': 1.25, 'quantity': 10}}
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p1_add_item_structure - AssertionError: assert ...
1 failed in 0.01s
```

## test_p1_add_item_populates

- Plan P1: add_item populates inventory with correct structure — input `v.add_item('Coke', 1.25, 10)`, expected `v.inventory == {'Coke': {'price': 1.25, 'quantity': 10}}`
- Reviewer: The test correctly expects the inventory to contain the specified price and quantity per the docstring example. The implementation incorrectly initializes new items with price=0 because restock_item unconditionally returns True via setdefault, bypassing the assignment of the correct price.

```
____ test_p1_add_item_populates __________________________
test_solution.py:23: in test_p1_add_item_populates
    assert v.inventory == {'Coke': {'price': 1.25, 'quantity': 10}}
E   AssertionError: assert {'Coke': {'pr...uantity': 10}} == {'Coke': {'pr...uantity': 10}}
E     
E     Differing items:
E     {'Coke': {'price': 0, 'quantity': 10}} != {'Coke': {'price': 1.25, 'quantity': 10}}
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p1_add_item_populates - AssertionError: assert ...
1 failed in 0.01s
```

## test_extra_restock_nonexistent

- Reviewer: The test correctly expects False for a non-existent item per the explicit docstring contract. The implementation violates this by using setdefault to create the item and unconditionally returning True.

```
F                                                                        [100%]
=================================== FAILURES ===================================
________________________ test_extra_restock_nonexistent ________________________
test_solution.py:23: in test_extra_restock_nonexistent
    assert result is False
E   assert True is False
=========================== short test summary info ============================
FAILED test_solution.py::test_extra_restock_nonexistent - assert True is False
1 failed in 0.01s
```
