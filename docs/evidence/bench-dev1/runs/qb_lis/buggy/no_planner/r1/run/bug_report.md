# Suspected implementation bugs

## test_docstring_example

- Reviewer: The test correctly asserts the example provided in the specification, which explicitly states that lis([4, 1, 5, 3, 7, 6, 2]) should return 3. The implementation returns 2, violating the specification. This indicates a fault in the implementation logic rather than an issue with the test.

```
F                                                                        [100%]
=================================== FAILURES ===================================
____________________________ test_docstring_example ____________________________
test_solution.py:5: in test_docstring_example
    assert result == 3
E   assert 2 == 3
=========================== short test summary info ============================
FAILED test_solution.py::test_docstring_example - assert 2 == 3
1 failed in 0.01s
```
