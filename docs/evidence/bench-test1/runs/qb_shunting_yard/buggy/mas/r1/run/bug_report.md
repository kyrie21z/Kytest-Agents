# Suspected implementation bugs

## test_p1_simple_chain_subtraction

- Plan P1: Converts a simple chain of subtractions to RPN — input `[10, '-', 5, '-', 2]`, expected `[10, 5, '-', 2, '-']`
- Reviewer: The implementation fails to push operators onto opstack, causing all operators to be omitted from the output. This contradicts the specification's examples and intended behavior.

```
========= FAILURES ===================================
_______________________ test_p1_simple_chain_subtraction _______________________
test_solution.py:4: in test_p1_simple_chain_subtraction
    assert result == [10, 5, '-', 2, '-']
E   AssertionError: assert [10, 5, 2] == [10, 5, '-', 2, '-']
E     
E     At index 2 diff: 2 != '-'
E     Right contains 2 more items, first extra item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p1_simple_chain_subtraction - AssertionError: a...
1 failed in 0.01s
```

## test_p2_mixed_precedence

- Plan P2: Converts an expression with mixed operator precedence to RPN — input `[34, '-', 12, '/', 5]`, expected `[34, 12, 5, '/', '-']`
- Reviewer: Same root cause: operators are not pushed to the stack, violating the specification's requirement to reorder tokens into RPN including operators.

```
[100%]
=================================== FAILURES ===================================
___________________________ test_p2_mixed_precedence ___________________________
test_solution.py:4: in test_p2_mixed_precedence
    assert result == [34, 12, 5, '/', '-']
E   AssertionError: assert [34, 12, 5] == [34, 12, 5, '/', '-']
E     
E     Right contains 2 more items, first extra item: '/'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p2_mixed_precedence - AssertionError: assert [3...
1 failed in 0.01s
```

## test_p3_complex_interleaved

- Plan P3: Converts a complex infix expression with interleaved operators to RPN — input `[4, '+', 9, '*', 9, '-', 10, '+', 13]`, expected `[4, 9, 9, '*', '+', 10, '-', 13, '+']`
- Reviewer: Implementation drops all operators due to missing stack push, contradicting the spec example and algorithm description.

```
=========================
_________________________ test_p3_complex_interleaved __________________________
test_solution.py:4: in test_p3_complex_interleaved
    assert result == [4, 9, 9, '*', '+', 10, '-', 13, '+']
E   AssertionError: assert [4, 9, 9, 10, 13] == [4, 9, 9, '*', '+', 10, ...]
E     
E     At index 3 diff: 10 != '*'
E     Right contains 4 more items, first extra item: 10
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p3_complex_interleaved - AssertionError: assert...
1 failed in 0.01s
```

## test_p5_minimal_expression

- Plan P5: Converts a minimal valid expression (two operands, one operator) — input `[3, '+', 7]`, expected `[3, 7, '+']`
- Reviewer: Follows spec logic; implementation incorrectly returns only operands, omitting the '+' operator.

```
[100%]
=================================== FAILURES ===================================
__________________________ test_p5_minimal_expression __________________________
test_solution.py:4: in test_p5_minimal_expression
    assert result == [3, 7, '+']
E   AssertionError: assert [3, 7] == [3, 7, '+']
E     
E     Right contains one more item: '+'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p5_minimal_expression - AssertionError: assert ...
1 failed in 0.01s
```

## test_p6_left_associativity_multiplication

- Plan P6: Verifies left-associativity of identical precedence operators — input `[10, '*', 2, '*', 5]`, expected `[10, 2, '*', 5, '*']`
- Reviewer: Test correctly specifies left-associative RPN conversion; implementation bug causes operator loss.

```
FAILURES ===================================
__________________ test_p6_left_associativity_multiplication ___________________
test_solution.py:4: in test_p6_left_associativity_multiplication
    assert result == [10, 2, '*', 5, '*']
E   AssertionError: assert [10, 2, 5] == [10, 2, '*', 5, '*']
E     
E     At index 2 diff: 5 != '*'
E     Right contains 2 more items, first extra item: 5
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p6_left_associativity_multiplication - Assertio...
1 failed in 0.01s
```

## test_p7_precedence_add_mul

- Plan P7: Verifies precedence ordering between addition and multiplication — input `[2, '+', 3, '*', 4]`, expected `[2, 3, 4, '*', '+']`
- Reviewer: Test correctly specifies precedence handling; implementation fails to track operators on the stack.

```
[100%]
=================================== FAILURES ===================================
__________________________ test_p7_precedence_add_mul __________________________
test_solution.py:4: in test_p7_precedence_add_mul
    assert result == [2, 3, 4, '*', '+']
E   AssertionError: assert [2, 3, 4] == [2, 3, 4, '*', '+']
E     
E     Right contains 2 more items, first extra item: '*'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p7_precedence_add_mul - AssertionError: assert ...
1 failed in 0.01s
```

## test_p9_multiset_preservation

- Plan P9: Preserves the multiset of tokens during conversion — input `[1, '+', 2, '*', 3]`, expected `Output contains exactly the same integers and operators as input, reordered.`
- Reviewer: Test enforces a valid correctness invariant (token multiset preservation); implementation violates it by dropping operators.

```
[100%]
=================================== FAILURES ===================================
________________________ test_p9_multiset_preservation _________________________
test_solution.py:7: in test_p9_multiset_preservation
    assert sorted_input == sorted_output
E   AssertionError: assert [1, 2, 3, '*', '+'] == [1, 2, 3]
E     
E     Left contains 2 more items, first extra item: '*'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p9_multiset_preservation - AssertionError: asse...
1 failed in 0.01s
```

## test_extra_negative_operands

- Reviewer: Valid extension of spec; negative integers are allowed by precondition, and operators must be preserved in RPN output.

```
[100%]
=================================== FAILURES ===================================
_________________________ test_extra_negative_operands _________________________
test_solution.py:4: in test_extra_negative_operands
    assert result == [-5, -3, '+']
E   AssertionError: assert [-5, -3] == [-5, -3, '+']
E     
E     Right contains one more item: '+'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_extra_negative_operands - AssertionError: asser...
1 failed in 0.01s
```

## test_extra_division_precedence

- Reviewer: Valid extension testing equal precedence and left-associativity; implementation drops operators.

```
=================================== FAILURES ===================================
________________________ test_extra_division_precedence ________________________
test_solution.py:4: in test_extra_division_precedence
    assert result == [100, 10, 2, '*', '/']
E   AssertionError: assert [100, 10, 2] == [100, 10, 2, '*', '/']
E     
E     Right contains 2 more items, first extra item: '*'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_extra_division_precedence - AssertionError: ass...
1 failed in 0.01s
```

## test_extra_multiple_operators_same_precedence

- Reviewer: Valid extension; implementation fails to handle multiple operators due to missing stack push.

```
=======================
________________ test_extra_multiple_operators_same_precedence _________________
test_solution.py:4: in test_extra_multiple_operators_same_precedence
    assert result == [1, 2, '+', 3, '+', 4, '+']
E   AssertionError: assert [1, 2, 3, 4] == [1, 2, '+', 3, '+', 4, ...]
E     
E     At index 2 diff: 3 != '+'
E     Right contains 3 more items, first extra item: '+'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_extra_multiple_operators_same_precedence - Asse...
1 failed in 0.01s
```

## test_extra_higher_precedence_first

- Reviewer: Valid extension testing precedence rules; implementation drops operators entirely.

```
========== FAILURES ===================================
______________________ test_extra_higher_precedence_first ______________________
test_solution.py:4: in test_extra_higher_precedence_first
    assert result == [5, 3, '*', 2, '+']
E   AssertionError: assert [5, 3, 2] == [5, 3, '*', 2, '+']
E     
E     At index 2 diff: 2 != '*'
E     Right contains 2 more items, first extra item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_extra_higher_precedence_first - AssertionError:...
1 failed in 0.01s
```
