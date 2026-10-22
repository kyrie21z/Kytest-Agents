# Suspected implementation bugs

## test_tie_breaking_lower_index

- Reviewer: The implementation sorts ties using `-i` in the key function, which causes higher indices to be prioritized. The specification explicitly states that 'ties go to the entry with the lower index.' The test correctly expects lower indices to receive the leftover units first, confirming the implementation violates the specification.

```
[100%]
=================================== FAILURES ===================================
________________________ test_tie_breaking_lower_index _________________________
test_solution.py:5: in test_tie_breaking_lower_index
    assert result == [2, 2, 1]
E   assert [1, 2, 2] == [2, 2, 1]
E     
E     At index 0 diff: 1 != 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_tie_breaking_lower_index - assert [1, 2, 2] == ...
1 failed in 0.01s
```
