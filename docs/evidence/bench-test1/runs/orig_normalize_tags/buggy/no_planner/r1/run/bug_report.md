# Suspected implementation bugs

## test_basic_example_preserves_order

- Reviewer: The test correctly follows the specification, which explicitly states that duplicates are removed while keeping the original order of first occurrences. The implementation incorrectly applies sorted(), violating the spec.

```
_basic_example_preserves_order ______________________
test_solution.py:14: in test_basic_example_preserves_order
    assert result == ['python', 'ml', 'data'], f"Expected order preserved, got {result}"
E   AssertionError: Expected order preserved, got ['data', 'ml', 'python']
E   assert ['data', 'ml', 'python'] == ['python', 'ml', 'data']
E     
E     At index 0 diff: 'data' != 'python'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_basic_example_preserves_order - AssertionError:...
1 failed in 0.01s
```

## test_non_alphabetical_input_preserves_order

- Reviewer: The test correctly enforces the specification's order preservation requirement. The implementation's alphabetical sorting contradicts the spec.

```
input_preserves_order __________________
test_solution.py:10: in test_non_alphabetical_input_preserves_order
    assert result == ['zebra', 'apple', 'banana'], \
E   AssertionError: Expected original order ['zebra', 'apple', 'banana'], got ['apple', 'banana', 'zebra']
E   assert ['apple', 'banana', 'zebra'] == ['zebra', 'apple', 'banana']
E     
E     At index 0 diff: 'apple' != 'zebra'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_non_alphabetical_input_preserves_order - Assert...
1 failed in 0.01s
```

## test_dedup_keeps_first_occurrence_position

- Reviewer: The test correctly follows the specification. The implementation sorts the result, losing the original insertion order mandated by the docstring.

```
=========
__________________ test_dedup_keeps_first_occurrence_position __________________
test_solution.py:9: in test_dedup_keeps_first_occurrence_position
    assert result == ['b', 'a', 'c'], f"Expected ['b', 'a', 'c'], got {result}"
E   AssertionError: Expected ['b', 'a', 'c'], got ['a', 'b', 'c']
E   assert ['a', 'b', 'c'] == ['b', 'a', 'c']
E     
E     At index 0 diff: 'a' != 'b'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_dedup_keeps_first_occurrence_position - Asserti...
1 failed in 0.01s
```

## test_mixed_case_order_preservation

- Reviewer: The test correctly follows the specification. The implementation's use of sorted() violates the explicit requirement to maintain original order.

```
_______ test_mixed_case_order_preservation ______________________
test_solution.py:9: in test_mixed_case_order_preservation
    assert result == ['zebra', 'apple', 'banana'], \
E   AssertionError: Expected ['zebra', 'apple', 'banana'], got ['apple', 'banana', 'zebra']
E   assert ['apple', 'banana', 'zebra'] == ['zebra', 'apple', 'banana']
E     
E     At index 0 diff: 'apple' != 'zebra'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_mixed_case_order_preservation - AssertionError:...
1 failed in 0.02s
```
