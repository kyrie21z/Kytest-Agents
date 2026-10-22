# Suspected implementation bugs

## test_spec_example_simple

- Reviewer: The test input and expected output exactly match the specification's example. The implementation violates the specification by failing to push operators onto the stack, resulting in their omission from the output.

```
================= FAILURES ===================================
___________________________ test_spec_example_simple ___________________________
test_solution.py:4: in test_spec_example_simple
    assert result == [10, 5, '-', 2, '-']
E   AssertionError: assert [10, 5, 2] == [10, 5, '-', 2, '-']
E     
E     At index 2 diff: 2 != '-'
E     Right contains 2 more items, first extra item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_spec_example_simple - AssertionError: assert [1...
1 failed in 0.01s
```
