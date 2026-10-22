# Suspected implementation bugs

## test_p1_simple_left_associative_subtraction

- Plan P1: Converts a simple left-associative subtraction chain to RPN — input `[10, '-', 5, '-', 2]`, expected `[10, 5, '-', 2, '-']`
- Reviewer: Follows spec Example 1. Implementation drops operators because `opstack.append(token)` is missing, violating the RPN conversion requirement.

```
AILURES ===================================
_________________ test_p1_simple_left_associative_subtraction __________________
test_solution.py:4: in test_p1_simple_left_associative_subtraction
    assert result == [10, 5, '-', 2, '-']
E   AssertionError: assert [10, 5, 2] == [10, 5, '-', 2, '-']
E     
E     At index 2 diff: 2 != '-'
E     Right contains 2 more items, first extra item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p1_simple_left_associative_subtraction - Assert...
1 failed in 0.01s
```

## test_p2_mixed_precedence_division_over_subtraction

- Plan P2: Handles mixed operator precedence (division over subtraction) — input `[34, '-', 12, '/', 5]`, expected `[34, 12, 5, '/', '-']`
- Reviewer: Follows spec Example 2. Same implementation bug causes operators to be omitted from output.

```
======================= FAILURES ===================================
______________ test_p2_mixed_precedence_division_over_subtraction ______________
test_solution.py:4: in test_p2_mixed_precedence_division_over_subtraction
    assert result == [34, 12, 5, '/', '-']
E   AssertionError: assert [34, 12, 5] == [34, 12, 5, '/', '-']
E     
E     Right contains 2 more items, first extra item: '/'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p2_mixed_precedence_division_over_subtraction
1 failed in 0.01s
```

## test_p3_complex_interleaved_operators

- Plan P3: Processes a complex expression with interleaved addition, multiplication, and subtraction — input `[4, '+', 9, '*', 9, '-', 10, '+', 13]`, expected `[4, 9, 9, '*', '+', 10, '-', 13, '+']`
- Reviewer: Follows spec Example 3. Implementation fails to handle operator stacking, dropping all operators.

```
===============
____________________ test_p3_complex_interleaved_operators _____________________
test_solution.py:4: in test_p3_complex_interleaved_operators
    assert result == [4, 9, 9, '*', '+', 10, '-', 13, '+']
E   AssertionError: assert [4, 9, 9, 10, 13] == [4, 9, 9, '*', '+', 10, ...]
E     
E     At index 3 diff: 10 != '*'
E     Right contains 4 more items, first extra item: 10
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p3_complex_interleaved_operators - AssertionErr...
1 failed in 0.01s
```

## test_p5_simplest_non_trivial_infix

- Plan P5: Converts the simplest non-trivial infix expression — input `[3, '+', 7]`, expected `[3, 7, '+']`
- Reviewer: Follows spec base case for two operands. Implementation omits the '+' operator due to missing stack push.

```
[100%]
=================================== FAILURES ===================================
______________________ test_p5_simplest_non_trivial_infix ______________________
test_solution.py:4: in test_p5_simplest_non_trivial_infix
    assert result == [3, 7, '+']
E   AssertionError: assert [3, 7] == [3, 7, '+']
E     
E     Right contains one more item: '+'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p5_simplest_non_trivial_infix - AssertionError:...
1 failed in 0.01s
```

## test_p1_left_assoc_subtraction

- Plan P1: Converts a simple left-associative subtraction chain to RPN — input `[10, '-', 5, '-', 2]`, expected `[10, 5, '-', 2, '-']`
- Reviewer: The implementation omits `opstack.append(token)` after the precedence check, causing all operators to be dropped from the output. This directly contradicts the specification's examples and RPN conversion requirement.

```
=========== FAILURES ===================================
________________________ test_p1_left_assoc_subtraction ________________________
test_solution.py:6: in test_p1_left_assoc_subtraction
    assert result == [10, 5, '-', 2, '-']
E   AssertionError: assert [10, 5, 2] == [10, 5, '-', 2, '-']
E     
E     At index 2 diff: 2 != '-'
E     Right contains 2 more items, first extra item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p1_left_assoc_subtraction - AssertionError: ass...
1 failed in 0.01s
```

## test_p2_division_over_subtraction

- Plan P2: Handles mixed operator precedence (division over subtraction) — input `[34, '-', 12, '/', 5]`, expected `[34, 12, 5, '/', '-']`
- Reviewer: Same implementation bug: operators are never pushed to the stack, so they are omitted from the result, violating the spec's expected output.

```
=================================== FAILURES ===================================
______________________ test_p2_division_over_subtraction _______________________
test_solution.py:6: in test_p2_division_over_subtraction
    assert result == [34, 12, 5, '/', '-']
E   AssertionError: assert [34, 12, 5] == [34, 12, 5, '/', '-']
E     
E     Right contains 2 more items, first extra item: '/'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p2_division_over_subtraction - AssertionError: ...
1 failed in 0.01s
```

## test_p3_complex_interleaved

- Plan P3: Processes a complex expression with interleaved addition, multiplication, and subtraction — input `[4, '+', 9, '*', 9, '-', 10, '+', 13]`, expected `[4, 9, 9, '*', '+', 10, '-', 13, '+']`
- Reviewer: Same implementation bug: missing stack push causes all operators to be lost, contradicting the specification.

```
=========================
_________________________ test_p3_complex_interleaved __________________________
test_solution.py:6: in test_p3_complex_interleaved
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

## test_p5_simplest_infix

- Plan P5: Converts the simplest non-trivial infix expression — input `[3, '+', 7]`, expected `[3, 7, '+']`
- Reviewer: Same implementation bug: the '+' operator is dropped, failing to meet the spec's basic conversion requirement.

```
[100%]
=================================== FAILURES ===================================
____________________________ test_p5_simplest_infix ____________________________
test_solution.py:6: in test_p5_simplest_infix
    assert result == [3, 7, '+']
E   AssertionError: assert [3, 7] == [3, 7, '+']
E     
E     Right contains one more item: '+'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p5_simplest_infix - AssertionError: assert [3, ...
1 failed in 0.01s
```

## test_p7_token_preservation

- Plan P7: Preserves all original tokens (multiset equality) — input `[1, '+', 2, '*', 3, '-', 4]`, expected `Output list contains exactly the same elements as input (one '1', one '2', one '3', one '4', one '+', one '*', one '-') in some order.`
- Reviewer: The implementation drops all operators, violating the spec's guarantee that the output is a reordering of the input tokens.

```
_________________________ test_p7_token_preservation __________________________
test_solution.py:8: in test_p7_token_preservation
    assert sorted((str(t) for t in result)) == sorted((str(t) for t in tokens))
E   AssertionError: assert ['1', '2', '3', '4'] == ['*', '+', '-...'2', '3', ...]
E     
E     At index 0 diff: '1' != '*'
E     Right contains 3 more items, first extra item: '2'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p7_token_preservation - AssertionError: assert ...
1 failed in 0.01s
```

## test_p8_precedence_multiplication_before_addition

- Plan P8: Enforces standard mathematical precedence (multiplication before addition) — input `[5, '+', 6, '*', 2]`, expected `[5, 6, 2, '*', '+']`
- Reviewer: Same implementation bug: operators are not retained in the output, failing to enforce precedence as specified.

```
========================= FAILURES ===================================
______________ test_p8_precedence_multiplication_before_addition _______________
test_solution.py:6: in test_p8_precedence_multiplication_before_addition
    assert result == [5, 6, 2, '*', '+']
E   AssertionError: assert [5, 6, 2] == [5, 6, 2, '*', '+']
E     
E     Right contains 2 more items, first extra item: '*'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_p8_precedence_multiplication_before_addition - ...
1 failed in 0.01s
```
