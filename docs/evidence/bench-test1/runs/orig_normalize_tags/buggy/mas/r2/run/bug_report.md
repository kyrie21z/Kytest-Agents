# Suspected implementation bugs

## test_p1_standard_mixed

- Plan P1: Standard mixed case and whitespace handling with duplicates and empty slots — input `" Python, ML ,python,, Data "`, expected `['python', 'ml', 'data']`
- Reviewer: The specification explicitly requires preserving the original order of first occurrences after deduplication. The implementation incorrectly sorts the output alphabetically via `sorted(set(seen))`, violating this requirement.

```
[100%]
=================================== FAILURES ===================================
____________________________ test_p1_standard_mixed ____________________________
test_solution.py:4: in test_p1_standard_mixed
    assert result == ['python', 'ml', 'data']
E   AssertionError: assert ['data', 'ml', 'python'] == ['python', 'ml', 'data']
E     
E     At index 0 diff: 'data' != 'python'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p1_standard_mixed - AssertionError: assert ['da...
1 failed in 0.01s
```

## test_p5_order_preservation

- Plan P5: Preservation of original order with interleaved duplicates — input `"B, A, b, a"`, expected `['b', 'a']`
- Reviewer: Same issue: the implementation sorts the result, contradicting the specification's mandate to maintain the original order of normalized tags.

```
[100%]
=================================== FAILURES ===================================
__________________________ test_p5_order_preservation __________________________
test_solution.py:4: in test_p5_order_preservation
    assert result == ['b', 'a']
E   AssertionError: assert ['a', 'b'] == ['b', 'a']
E     
E     At index 0 diff: 'a' != 'b'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p5_order_preservation - AssertionError: assert ...
1 failed in 0.01s
```
