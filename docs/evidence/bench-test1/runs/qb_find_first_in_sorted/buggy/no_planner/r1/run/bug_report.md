# Suspected implementation bugs

## test_not_found_returns_minus_one

- Reviewer: The test correctly implements the specification requirement to return -1 when x is not in arr. The implementation contains an off-by-one error (hi = len(arr) combined with while lo <= hi) that allows mid to reach len(arr), causing an IndexError instead of returning -1.

```
t_solution.py:6: in test_not_found_returns_minus_one
    result = find_first_in_sorted([1, 2, 3], 4)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_testgen_contracts.py:375: in guarded
    return function(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
solution.py:22: in find_first_in_sorted
    if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            ^^^^^^^^
E   IndexError: list index out of range
=========================== short test summary info ============================
FAILED test_solution.py::test_not_found_returns_minus_one - IndexError: list ...
1 failed in 0.04s
```

## test_not_found_small_value

- Reviewer: The test correctly follows the specification. The implementation crashes with an IndexError when searching for a value smaller than all elements due to the same out-of-bounds access bug.

```

```

## test_single_element_not_found

- Reviewer: The test correctly follows the specification. The implementation crashes with an IndexError when searching a single-element array due to the same out-of-bounds access bug.

```

```
