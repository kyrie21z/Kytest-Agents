# Suspected implementation bugs

## test_p2_accumulate_existing

- Plan P2: Accumulate quantity for an existing product — input `warehouse.add_product(1, 'Widget', 5)`, expected `warehouse.inventory[1]['quantity'] == 15`
- Reviewer: The specification explicitly states to 'plus the quantity if it has existed in inventory', which requires arithmetic accumulation. The test correctly expects the new quantity to be added to the existing stock (10 + 5 = 15). The implementation incorrectly overwrites the quantity field instead of adding to it, directly violating the specification.

```
F                                                                        [100%]
=================================== FAILURES ===================================
_________________________ test_p2_accumulate_existing __________________________
test_solution.py:18: in test_p2_accumulate_existing
    assert warehouse.inventory[1]['quantity'] == 15
E   assert 5 == 15
=========================== short test summary info ============================
FAILED test_solution.py::test_p2_accumulate_existing - assert 5 == 15
1 failed in 0.01s
```
