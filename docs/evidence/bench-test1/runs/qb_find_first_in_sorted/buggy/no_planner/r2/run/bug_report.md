# Suspected implementation bugs

## test_not_found_smaller_than_min

- Reviewer: Test correctly enforces the specification requirement to return -1 when x is not in arr. The implementation contains an off-by-one error (hi = len(arr)) that permits mid to equal len(arr), causing incorrect traversal or an IndexError, thereby violating the spec.

```

```

## test_not_found_larger_than_max

- Reviewer: Test correctly enforces the specification requirement to return -1 when x is not in arr. The implementation crashes with IndexError because hi is initialized to len(arr), allowing mid to reference arr[len(arr)], which is out of bounds.

```
lution.py:9: in test_not_found_larger_than_max
    result = find_first_in_sorted([5, 10, 15], 20)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_testgen_contracts.py:375: in guarded
    return function(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
solution.py:22: in find_first_in_sorted
    if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            ^^^^^^^^
E   IndexError: list index out of range
=========================== short test summary info ============================
FAILED test_solution.py::test_not_found_larger_than_max - IndexError: list in...
1 failed in 0.03s
```

## test_not_found_between_elements

- Reviewer: Test correctly enforces the specification requirement to return -1 for non-existent values between existing elements. The implementation fails due to the same boundary condition bug (hi = len(arr)), preventing correct convergence and returning invalid results or crashing.

```

```

## test_single_element_not_found

- Reviewer: Test correctly enforces the specification requirement to return -1 when x is not in arr. The implementation crashes with IndexError when mid equals len(arr), directly violating the documented contract.

```
_______
test_solution.py:9: in test_single_element_not_found
    result = find_first_in_sorted([42], 99)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_testgen_contracts.py:375: in guarded
    return function(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
solution.py:22: in find_first_in_sorted
    if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            ^^^^^^^^
E   IndexError: list index out of range
=========================== short test summary info ============================
FAILED test_solution.py::test_single_element_not_found - IndexError: list ind...
1 failed in 0.04s
```
