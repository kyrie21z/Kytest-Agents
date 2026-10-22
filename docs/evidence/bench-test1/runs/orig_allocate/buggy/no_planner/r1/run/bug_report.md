# Suspected implementation bugs

## test_tie_breaking_lower_index

- Reviewer: The specification explicitly states that ties in fractional remainders go to the entry with the lower index. The test expects index 0 to receive the extra unit ([4, 3, 3]), which correctly follows the spec. The implementation's sorting key `(-remainders[i], -i)` inadvertently prioritizes higher indices during ties, violating the spec. Thus, the test is valid and the implementation is buggy.

```
=========== FAILURES ===================================
________________________ test_tie_breaking_lower_index _________________________
test_solution.py:5: in test_tie_breaking_lower_index
    assert result == [4, 3, 3], f"Expected [4, 3, 3] but got {result}"
E   AssertionError: Expected [4, 3, 3] but got [3, 3, 4]
E   assert [3, 3, 4] == [4, 3, 3]
E     
E     At index 0 diff: 3 != 4
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_tie_breaking_lower_index - AssertionError: Expe...
1 failed in 0.01s
```

## test_zero_weight_with_leftover

- Reviewer: The specification requires that zero-weight entries receive 0 and that ties go to the lower index. The test expects index 1 to receive the leftover unit ([0, 6, 5]), adhering to the spec. The implementation incorrectly assigns the unit to index 2 due to the same tie-breaking sorting flaw. The test correctly validates the specification.

```
========== FAILURES ===================================
________________________ test_zero_weight_with_leftover ________________________
test_solution.py:5: in test_zero_weight_with_leftover
    assert result == [0, 6, 5], f"Expected [0, 6, 5] but got {result}"
E   AssertionError: Expected [0, 6, 5] but got [0, 5, 6]
E   assert [0, 5, 6] == [0, 6, 5]
E     
E     At index 1 diff: 5 != 6
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_zero_weight_with_leftover - AssertionError: Exp...
1 failed in 0.01s
```
