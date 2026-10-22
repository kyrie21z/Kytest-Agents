# Suspected implementation bugs

## test_p5_docstring_example

- Plan P5: Match provided docstring example — input `[4, 1, 5, 3, 7, 6, 2]`, expected `3`
- Reviewer: The test strictly follows the specification example. The implementation contains a logical flaw: the line 'longest = length + 1' executes whenever 'length == longest' OR 'val < arr[ends[length + 1]]'. When the second condition triggers (indicating a better tail for a shorter subsequence), 'longest' is incorrectly reassigned to a smaller value, violating the spec's requirement to return the maximum length.

```
F                                                                        [100%]
=================================== FAILURES ===================================
__________________________ test_p5_docstring_example ___________________________
test_solution.py:15: in test_p5_docstring_example
    assert result == 3
E   assert 2 == 3
=========================== short test summary info ============================
FAILED test_solution.py::test_p5_docstring_example - assert 2 == 3
1 failed in 0.02s
```

## test_p7_tuple_input

- Plan P7: Accept tuple sequences — input `(10, 20, 5, 30)`, expected `3`
- Reviewer: Tuples satisfy the 'sequence of ints' precondition. The failure stems from the same implementation bug where 'longest' is erroneously decreased during iteration, preventing the algorithm from correctly identifying the full increasing subsequence.

```
F                                                                        [100%]
=================================== FAILURES ===================================
_____________________________ test_p7_tuple_input ______________________________
test_solution.py:14: in test_p7_tuple_input
    assert result == 3
E   assert 2 == 3
=========================== short test summary info ============================
FAILED test_solution.py::test_p7_tuple_input - assert 2 == 3
1 failed in 0.02s
```

## test_extra_unique_precondition

- Reviewer: The input respects the uniqueness precondition and the expected output of 5 is mathematically correct. The implementation fails because its update logic shrinks the 'longest' counter when processing elements that improve shorter subsequences, resulting in an incorrect answer of 4.

```
F                                                                        [100%]
=================================== FAILURES ===================================
________________________ test_extra_unique_precondition ________________________
test_solution.py:14: in test_extra_unique_precondition
    assert result == 5
E   assert 4 == 5
=========================== short test summary info ============================
FAILED test_solution.py::test_extra_unique_precondition - assert 4 == 5
1 failed in 0.02s
```

## test_extra_ascending_then_drop

- Reviewer: The test correctly expects an LIS length of 5. The implementation incorrectly reduces 'longest' when encountering the drop to 0, as the conditional 'longest = length + 1' overwrites the actual maximum with a smaller value, yielding 3 instead of 5.

```
F                                                                        [100%]
=================================== FAILURES ===================================
________________________ test_extra_ascending_then_drop ________________________
test_solution.py:14: in test_extra_ascending_then_drop
    assert result == 5
E   assert 3 == 5
=========================== short test summary info ============================
FAILED test_solution.py::test_extra_ascending_then_drop - assert 3 == 5
1 failed in 0.01s
```
