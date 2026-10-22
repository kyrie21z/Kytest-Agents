# Suspected implementation bugs

## test_p1_uniform_weights

- Plan P1: Returns equal-ish distribution when weights are uniform and total is not evenly divisible by count. — input `(100, [1, 1, 1])`, expected `[34, 33, 33]`
- Reviewer: The implementation sorts by (-remainders[i], -i), which prioritizes higher indices on ties. This contradicts the specification stating 'ties go to the entry with the lower index'.

```
[100%]
=================================== FAILURES ===================================
___________________________ test_p1_uniform_weights ____________________________
test_solution.py:6: in test_p1_uniform_weights
    assert result == [34, 33, 33]
E   assert [33, 33, 34] == [34, 33, 33]
E     
E     At index 0 diff: 33 != 34
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p1_uniform_weights - assert [33, 33, 34] == [34...
1 failed in 0.01s
```

## test_p4_tie_breaking

- Plan P4: Applies tie-breaking rule when multiple entries share the largest fractional remainder. — input `(5, [1, 1])`, expected `[3, 2]`
- Reviewer: Same tie-breaking bug: the sort key prioritizes higher indices, causing the extra unit to be assigned to index 1 instead of index 0, violating the spec.

```
F                                                                        [100%]
=================================== FAILURES ===================================
_____________________________ test_p4_tie_breaking _____________________________
test_solution.py:6: in test_p4_tie_breaking
    assert result == [3, 2]
E   assert [2, 3] == [3, 2]
E     
E     At index 0 diff: 2 != 3
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p4_tie_breaking - assert [2, 3] == [3, 2]
1 failed in 0.01s
```

## test_p1_uniform_weights

- Plan P1: Returns equal-ish distribution when weights are uniform and total is not evenly divisible by count. — input `(100, [1, 1, 1])`, expected `[34, 33, 33]`
- Reviewer: The test correctly implements the specification requirement that ties in fractional remainder go to the lower index. The implementation violates the spec because its sort key uses `-i`, which incorrectly prioritizes higher indices for tie-breaking.

```
[100%]
=================================== FAILURES ===================================
___________________________ test_p1_uniform_weights ____________________________
test_solution.py:7: in test_p1_uniform_weights
    assert result == [34, 33, 33]
E   assert [33, 33, 34] == [34, 33, 33]
E     
E     At index 0 diff: 33 != 34
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p1_uniform_weights - assert [33, 33, 34] == [34...
1 failed in 0.02s
```

## test_p4_tie_breaking

- Plan P4: Applies tie-breaking rule when multiple entries share the largest fractional remainder. — input `(5, [1, 1])`, expected `[3, 2]`
- Reviewer: The test correctly implements the specification requirement that ties in fractional remainder go to the lower index. The implementation violates the spec because its sort key uses `-i`, which incorrectly prioritizes higher indices for tie-breaking.

```
F                                                                        [100%]
=================================== FAILURES ===================================
_____________________________ test_p4_tie_breaking _____________________________
test_solution.py:7: in test_p4_tie_breaking
    assert result == [3, 2]
E   assert [2, 3] == [3, 2]
E     
E     At index 0 diff: 2 != 3
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p4_tie_breaking - assert [2, 3] == [3, 2]
1 failed in 0.02s
```
