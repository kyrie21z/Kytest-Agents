# Suspected implementation bugs

## test_p2_accumulate_quantity

- Plan P2: Accumulate quantity on an existing product — input `warehouse.add_product(1, "Widget", 5)`, expected `warehouse.inventory[1]['quantity'] == 15`
- Reviewer: The test correctly follows the specification which mandates accumulating quantity for existing products ('plus the quantity if it has existed in inventory'). The implementation incorrectly overwrites the quantity instead of adding to it.

```
F                                                                        [100%]
=================================== FAILURES ===================================
_________________________ test_p2_accumulate_quantity __________________________
test_solution.py:8: in test_p2_accumulate_quantity
    assert warehouse.inventory[1]["quantity"] == 15
E   assert 5 == 15
=========================== short test summary info ============================
FAILED test_solution.py::test_p2_accumulate_quantity - assert 5 == 15
1 failed in 0.01s
```
