# Suspected implementation bugs

## test_p1_standard_decimal

- Plan P1: Verify standard decimal conversion remains unchanged. — input `to_base(123, 10)`, expected `'123'`
- Reviewer: The test expects standard positional notation per the specification. The implementation appends digits from least significant to most significant without reversing the result, producing '321' instead of '123', which violates the spec.

```
F                                                                        [100%]
=================================== FAILURES ===================================
___________________________ test_p1_standard_decimal ___________________________
test_solution.py:5: in test_p1_standard_decimal
    assert to_base(123, 10) == '123'
E   AssertionError: assert '321' == '123'
E     
E     - 123
E     + 321
=========================== short test summary info ============================
FAILED test_solution.py::test_p1_standard_decimal - AssertionError: assert '3...
1 failed in 0.01s
```

## test_p6_base_rollover

- Plan P6: Verify base rollover behavior where num equals the base. — input `to_base(36, 36)`, expected `'10'`
- Reviewer: The test expects standard base-36 representation '10' per the specification. The implementation returns '01' due to the same missing reversal bug, violating the spec.

```
F                                                                        [100%]
=================================== FAILURES ===================================
____________________________ test_p6_base_rollover _____________________________
test_solution.py:5: in test_p6_base_rollover
    assert to_base(36, 36) == '10'
E   AssertionError: assert '01' == '10'
E     
E     - 10
E     + 01
=========================== short test summary info ============================
FAILED test_solution.py::test_p6_base_rollover - AssertionError: assert '01' ...
1 failed in 0.01s
```

## test_p5_spec_example

- Plan P5: Verify the exact behavior shown in the specification example. — input `to_base(31, 16)`, expected `'1F'`
- Reviewer: The test directly cites the specification example expecting '1F'. The implementation returns 'F1' because it constructs the string in reverse order, violating the spec.

```
F                                                                        [100%]
=================================== FAILURES ===================================
_____________________________ test_p5_spec_example _____________________________
test_solution.py:5: in test_p5_spec_example
    assert to_base(31, 16) == '1F'
E   AssertionError: assert 'F1' == '1F'
E     
E     - 1F
E     + F1
=========================== short test summary info ============================
FAILED test_solution.py::test_p5_spec_example - AssertionError: assert 'F1' =...
1 failed in 0.01s
```

## test_p7_power_of_two_binary

- Plan P7: Test a power-of-two value in the minimum base to verify zero-padding/multiple zeros. — input `to_base(256, 2)`, expected `'100000000'`
- Reviewer: The test expects standard binary representation '100000000' per the specification. The implementation returns the reversed string '000000001', violating the spec.

```
[100%]
=================================== FAILURES ===================================
_________________________ test_p7_power_of_two_binary __________________________
test_solution.py:5: in test_p7_power_of_two_binary
    assert to_base(256, 2) == '100000000'
E   AssertionError: assert '000000001' == '100000000'
E     
E     - 100000000
E     ? -
E     + 000000001
E     ?         +
=========================== short test summary info ============================
FAILED test_solution.py::test_p7_power_of_two_binary - AssertionError: assert...
1 failed in 0.01s
```
