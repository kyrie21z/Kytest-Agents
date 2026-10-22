# Suspected implementation bugs

## test_to_base_docstring_example

- Reviewer: The test correctly expects standard base-n representation ('1F') per the specification. The implementation appends remainders without reversing, producing reversed output ('F1').

```
F                                                                        [100%]
=================================== FAILURES ===================================
________________________ test_to_base_docstring_example ________________________
test_solution.py:11: in test_to_base_docstring_example
    assert to_base(31, 16) == '1F'
E   AssertionError: assert 'F1' == '1F'
E     
E     - 1F
E     + F1
=========================== short test summary info ============================
FAILED test_solution.py::test_to_base_docstring_example - AssertionError: ass...
1 failed in 0.01s
```

## test_to_base_binary_conversion

- Reviewer: The test correctly expects standard binary representation ('1010') per the specification. The implementation produces reversed output ('0101') due to a missing reversal step.

```
[100%]
=================================== FAILURES ===================================
________________________ test_to_base_binary_conversion ________________________
test_solution.py:11: in test_to_base_binary_conversion
    assert to_base(10, 2) == '1010'
E   AssertionError: assert '0101' == '1010'
E     
E     - 1010
E     ?    -
E     + 0101
E     ? +
=========================== short test summary info ============================
FAILED test_solution.py::test_to_base_binary_conversion - AssertionError: ass...
1 failed in 0.01s
```

## test_to_base_non_palindrome_hex

- Reviewer: The test correctly expects standard hex representation ('64') per the specification. The implementation produces reversed output ('46') due to a missing reversal step.

```
F                                                                        [100%]
=================================== FAILURES ===================================
_______________________ test_to_base_non_palindrome_hex ________________________
test_solution.py:11: in test_to_base_non_palindrome_hex
    assert to_base(100, 16) == '64'
E   AssertionError: assert '46' == '64'
E     
E     - 64
E     + 46
=========================== short test summary info ============================
FAILED test_solution.py::test_to_base_non_palindrome_hex - AssertionError: as...
1 failed in 0.01s
```
