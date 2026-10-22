# Suspected implementation bugs

## test_p6_tie_breaking_lower_index

- Plan P6: Tie-breaking rule for equal fractional remainders — input `allocate(1, [1, 1])`, expected `[1, 0]`
- Reviewer: Implementation violates the spec's tie-breaking rule ('ties go to the entry with the lower index'). The sort key (-remainders[i], -i) incorrectly prioritizes higher indices on ties.

```
[100%]
=================================== FAILURES ===================================
_______________________ test_p6_tie_breaking_lower_index _______________________
test_solution.py:13: in test_p6_tie_breaking_lower_index
    assert result == [1, 0]
E   assert [0, 1] == [1, 0]
E     
E     At index 0 diff: 0 != 1
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p6_tie_breaking_lower_index - assert [0, 1] == ...
1 failed in 0.01s
```

## test_p1_equal_weights_odd_remainder

- Plan P1: Equal weights with odd total requiring remainder distribution — input `allocate(100, [1, 1, 1])`, expected `[34, 33, 33]`
- Reviewer: Same tie-breaking bug as above; implementation gives the leftover unit to index 2 instead of index 0.

```
[100%]
=================================== FAILURES ===================================
_____________________ test_p1_equal_weights_odd_remainder ______________________
test_solution.py:13: in test_p1_equal_weights_odd_remainder
    assert result == [34, 33, 33]
E   assert [33, 33, 34] == [34, 33, 33]
E     
E     At index 0 diff: 33 != 34
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p1_equal_weights_odd_remainder - assert [33, 33...
1 failed in 0.01s
```

## test_extra_zero_weight_with_remainder

- Reviewer: Implementation violates the tie-breaking rule; gives the leftover unit to index 2 instead of index 1 due to the -i sort key.

```
[100%]
=================================== FAILURES ===================================
____________________ test_extra_zero_weight_with_remainder _____________________
test_solution.py:13: in test_extra_zero_weight_with_remainder
    assert result == [0, 6, 5]
E   assert [0, 5, 6] == [0, 6, 5]
E     
E     At index 1 diff: 5 != 6
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_extra_zero_weight_with_remainder - assert [0, 5...
1 failed in 0.01s
```

## test_p1_equal_weights_remainder

- Plan P1: Equal weights with odd total requiring remainder distribution — input `allocate(100, [1, 1, 1])`, expected `[34, 33, 33]`
- Reviewer: Test correctly follows the spec requirement that ties go to the lower index. The implementation's sorting key (-remainders[i], -i) incorrectly prioritizes higher indices, violating the specification.

```
[100%]
=================================== FAILURES ===================================
_______________________ test_p1_equal_weights_remainder ________________________
test_solution.py:13: in test_p1_equal_weights_remainder
    assert result == [34, 33, 33]
E   assert [33, 33, 34] == [34, 33, 33]
E     
E     At index 0 diff: 33 != 34
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p1_equal_weights_remainder - assert [33, 33, 34...
1 failed in 0.01s
```

## test_p6_tie_lower_index_wins

- Plan P6: Tie-breaking rule for equal fractional remainders — input `allocate(1, [1, 1])`, expected `[1, 0]`
- Reviewer: Test correctly implements the spec's tie-breaking rule. The implementation breaks ties by higher index instead of lower index, contradicting the specification.

```
F                                                                        [100%]
=================================== FAILURES ===================================
_________________________ test_p6_tie_lower_index_wins _________________________
test_solution.py:13: in test_p6_tie_lower_index_wins
    assert result == [1, 0]
E   assert [0, 1] == [1, 0]
E     
E     At index 0 diff: 0 != 1
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p6_tie_lower_index_wins - assert [0, 1] == [1, 0]
1 failed in 0.01s
```

## test_extra_zero_weight_with_remainder

- Reviewer: Test correctly validates the zero-weight guarantee and lower-index tie-breaking. The implementation fails both due to the incorrect tie-breaking sort key.

```
[100%]
=================================== FAILURES ===================================
____________________ test_extra_zero_weight_with_remainder _____________________
test_solution.py:13: in test_extra_zero_weight_with_remainder
    assert result == [1, 0, 0]
E   assert [0, 0, 1] == [1, 0, 0]
E     
E     At index 0 diff: 0 != 1
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_extra_zero_weight_with_remainder - assert [0, 0...
1 failed in 0.01s
```
