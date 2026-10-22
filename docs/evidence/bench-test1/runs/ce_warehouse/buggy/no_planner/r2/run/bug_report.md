# Suspected implementation bugs

## test_add_product_adds_quantity_on_existing

- Reviewer: The test correctly follows the specification requirement to 'plus the quantity if it has existed in inventory'. The implementation incorrectly replaces the quantity instead of incrementing it.

```
F                                                                        [100%]
=================================== FAILURES ===================================
__________________ test_add_product_adds_quantity_on_existing __________________
test_solution.py:13: in test_add_product_adds_quantity_on_existing
    assert wh.inventory[1]['quantity'] == 8
E   assert 3 == 8
=========================== short test summary info ============================
FAILED test_solution.py::test_add_product_adds_quantity_on_existing - assert ...
1 failed in 0.01s
```
