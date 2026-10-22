# Suspected implementation bugs

## test_add_item_creates_new_entry

- Reviewer: The implementation's restock_item always returns True, causing add_item to skip the initialization branch for new items. Consequently, the price defaults to 0 instead of being set to the provided value (1.25). This directly contradicts the specification's doctest example which requires the price to be stored correctly upon adding a new item.

```
F                                                                        [100%]
=================================== FAILURES ===================================
_______________________ test_add_item_creates_new_entry ________________________
test_solution.py:16: in test_add_item_creates_new_entry
    assert vm.inventory['Coke']['price'] == 1.25
E   assert 0 == 1.25
=========================== short test summary info ============================
FAILED test_solution.py::test_add_item_creates_new_entry - assert 0 == 1.25
1 failed in 0.01s
```
