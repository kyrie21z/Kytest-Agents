# Suspected implementation bugs

## test_docstring_example_1

- Reviewer: Test input and expected output match the specification examples exactly. The implementation violates the spec by failing to push operators onto the stack, resulting in missing operators in the output.

```
================= FAILURES ===================================
___________________________ test_docstring_example_1 ___________________________
test_solution.py:5: in test_docstring_example_1
    assert result == [10, 5, '-', 2, '-']
E   AssertionError: assert [10, 5, 2] == [10, 5, '-', 2, '-']
E     
E     At index 2 diff: 2 != '-'
E     Right contains 2 more items, first extra item: 2
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_docstring_example_1 - AssertionError: assert [1...
1 failed in 0.01s
```

## test_docstring_example_2

- Reviewer: Test input and expected output match the specification examples exactly. The implementation violates the spec by failing to push operators onto the stack.

```
[100%]
=================================== FAILURES ===================================
___________________________ test_docstring_example_2 ___________________________
test_solution.py:5: in test_docstring_example_2
    assert result == [34, 12, 5, '/', '-']
E   AssertionError: assert [34, 12, 5] == [34, 12, 5, '/', '-']
E     
E     Right contains 2 more items, first extra item: '/'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_docstring_example_2 - AssertionError: assert [3...
1 failed in 0.01s
```

## test_single_operator

- Reviewer: Test correctly validates basic operator handling per the shunting-yard algorithm described in the spec. Implementation omits operators.

```
[100%]
=================================== FAILURES ===================================
_____________________________ test_single_operator _____________________________
test_solution.py:5: in test_single_operator
    assert result == [1, 2, '+']
E   AssertionError: assert [1, 2] == [1, 2, '+']
E     
E     Right contains one more item: '+'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_single_operator - AssertionError: assert [1, 2]...
1 failed in 0.01s
```

## test_multiplication_precedence

- Reviewer: Test correctly validates precedence handling per the algorithm spec. Implementation omits operators.

```
============== FAILURES ===================================
________________________ test_multiplication_precedence ________________________
test_solution.py:5: in test_multiplication_precedence
    assert result == [2, 3, '*', 4, '+']
E   AssertionError: assert [2, 3, 4] == [2, 3, '*', 4, '+']
E     
E     At index 2 diff: 4 != '*'
E     Right contains 2 more items, first extra item: 4
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_multiplication_precedence - AssertionError: ass...
1 failed in 0.01s
```
