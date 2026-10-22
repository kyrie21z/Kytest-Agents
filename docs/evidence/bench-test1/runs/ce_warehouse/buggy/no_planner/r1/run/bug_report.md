# Suspected implementation bugs

## test_add_product_accumulates_quantity_on_existing

- Reviewer: The specification explicitly states that add_product should 'plus the quantity if it has existed in inventory', meaning quantities must be accumulated. The test correctly expects the quantity to increase from 3 to 5. The implementation overwrites the existing quantity instead of adding to it, directly violating the specification.

```
F                                                                        [100%]
=================================== FAILURES ===================================
______________ test_add_product_accumulates_quantity_on_existing _______________
test_solution.py:7: in test_add_product_accumulates_quantity_on_existing
    assert w.inventory[1]['quantity'] == 5
E   assert 2 == 5
=========================== short test summary info ============================
FAILED test_solution.py::test_add_product_accumulates_quantity_on_existing - ...
1 failed in 0.01s
```
