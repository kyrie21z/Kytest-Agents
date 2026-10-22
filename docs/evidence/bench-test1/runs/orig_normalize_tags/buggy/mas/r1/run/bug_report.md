# Suspected implementation bugs

## test_p1_mixed_case_whitespace

- Plan P1: Validates the documented example with mixed case, extra whitespace, and consecutive commas. — input `" Python, ML ,python,, Data "`, expected `["python", "ml", "data"]`
- Reviewer: The test correctly expects order preservation per the specification. The implementation incorrectly applies sorted() to the result, violating the 'keep their original order' requirement.

```
=================================== FAILURES ===================================
________________________ test_p1_mixed_case_whitespace _________________________
test_solution.py:5: in test_p1_mixed_case_whitespace
    assert result == ["python", "ml", "data"]
E   AssertionError: assert ['data', 'ml', 'python'] == ['python', 'ml', 'data']
E     
E     At index 0 diff: 'data' != 'python'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p1_mixed_case_whitespace - AssertionError: asse...
1 failed in 0.01s
```

## test_p6_order_preservation

- Plan P6: Verifies that original order is preserved and only the first occurrence of each tag survives. — input `"cherry, banana, cherry, date, banana"`, expected `["cherry", "banana", "date"]`
- Reviewer: The test correctly expects order preservation per the specification. The implementation incorrectly applies sorted() to the result, violating the 'keep their original order' requirement.

```
======================== FAILURES ===================================
__________________________ test_p6_order_preservation __________________________
test_solution.py:5: in test_p6_order_preservation
    assert result == ["cherry", "banana", "date"]
E   AssertionError: assert ['banana', 'cherry', 'date'] == ['cherry', 'banana', 'date']
E     
E     At index 0 diff: 'banana' != 'cherry'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p6_order_preservation - AssertionError: assert ...
1 failed in 0.01s
```

## test_p8_internal_spaces_and_punctuation

- Plan P8: Tests preservation of internal spaces and punctuation within tags. — input `"hello world, foo-bar!"`, expected `["hello world", "foo-bar!"]`
- Reviewer: The test correctly expects order preservation per the specification. The implementation incorrectly applies sorted() to the result, violating the 'keep their original order' requirement.

```
====== FAILURES ===================================
___________________ test_p8_internal_spaces_and_punctuation ____________________
test_solution.py:21: in test_p8_internal_spaces_and_punctuation
    assert result == ["hello world", "foo-bar!"]
E   AssertionError: assert ['foo-bar!', 'hello world'] == ['hello world', 'foo-bar!']
E     
E     At index 0 diff: 'foo-bar!' != 'hello world'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p8_internal_spaces_and_punctuation - AssertionE...
1 failed in 0.02s
```

## test_extra_duplicate_removal_first_kept

- Reviewer: The test correctly expects order preservation per the specification. The implementation incorrectly applies sorted() to the result, violating the 'keep their original order' requirement.

```
[100%]
=================================== FAILURES ===================================
___________________ test_extra_duplicate_removal_first_kept ____________________
test_solution.py:22: in test_extra_duplicate_removal_first_kept
    assert result == ["zebra", "apple"]
E   AssertionError: assert ['apple', 'zebra'] == ['zebra', 'apple']
E     
E     At index 0 diff: 'apple' != 'zebra'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_extra_duplicate_removal_first_kept - AssertionE...
1 failed in 0.02s
```
