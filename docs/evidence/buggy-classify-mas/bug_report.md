# Suspected implementation bugs

## test_p5_upper_bound

- Plan P5: Value equals upper bound — input `classify(10, 1, 10)`, expected `0`
- Reviewer: The test correctly expects 0 for an inclusive upper bound per the specification. The implementation incorrectly uses `value >= high`, returning 1 instead of 0. This indicates a bug in the implementation.

```
[100%]
=================================== FAILURES ===================================
_____________________________ test_p5_upper_bound ______________________________
test_solution.py:19: in test_p5_upper_bound
    assert result == 0, f"Value 10 at upper bound of [1, 10] should return 0, got {result}"
E   AssertionError: Value 10 at upper bound of [1, 10] should return 0, got 1
E   assert 1 == 0
=========================== short test summary info ============================
FAILED test_solution.py::test_p5_upper_bound - AssertionError: Value 10 at up...
1 failed in 0.01s
```

## test_p6_degenerate_interval

- Plan P6: Degenerate interval where low equals high — input `classify(5, 5, 5)`, expected `0`
- Reviewer: The test correctly expects 0 when value equals both low and high in a degenerate interval. The implementation's `value >= high` condition triggers prematurely, returning 1. This confirms the same off-by-one bug in the implementation.

```
[100%]
=================================== FAILURES ===================================
_________________________ test_p6_degenerate_interval __________________________
test_solution.py:19: in test_p6_degenerate_interval
    assert result == 0, f"Value 5 in degenerate interval [5, 5] should return 0, got {result}"
E   AssertionError: Value 5 in degenerate interval [5, 5] should return 0, got 1
E   assert 1 == 0
=========================== short test summary info ============================
FAILED test_solution.py::test_p6_degenerate_interval - AssertionError: Value ...
1 failed in 0.01s
```
