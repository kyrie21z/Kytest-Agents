# Suspected implementation bugs

## test_p5_negative_ints

- Plan P5: Correctly orders and selects from negative integers — input `arr=[-5, -1, -3, 0], k=1`, expected `-3`
- Reviewer: The test correctly follows the specification (equivalent to sorted(arr)[k]). The implementation violates the spec because the recursive call for the 'above' partition incorrectly passes 'k' instead of 'k - num_lessoreq', causing it to misindex and return an incorrect element.

```
F                                                                        [100%]
=================================== FAILURES ===================================
____________________________ test_p5_negative_ints _____________________________
test_solution.py:12: in test_p5_negative_ints
    assert kth([-5, -1, -3, 0], 1) == -3
E   assert -1 == -3
E    +  where -1 = kth([-5, -1, -3, 0], 1)
=========================== short test summary info ============================
FAILED test_solution.py::test_p5_negative_ints - assert -1 == -3
1 failed in 0.01s
```
