# Suspected implementation bugs

## test_p5_empty_list

- Plan P5: Search in an empty list — input `arr=[], x=5`, expected `-1`
- Reviewer: The test correctly follows the specification. The implementation contains a bug: it initializes hi to len(arr) and lacks an empty-list guard, causing an IndexError when accessing arr[mid].

```
________________________
test_solution.py:9: in test_p5_empty_list
    result = find_first_in_sorted([], 5)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
_testgen_contracts.py:375: in guarded
    return function(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
solution.py:22: in find_first_in_sorted
    if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            ^^^^^^^^
E   IndexError: list index out of range
=========================== short test summary info ============================
FAILED test_solution.py::test_p5_empty_list - IndexError: list index out of r...
1 failed in 0.04s
```

## test_p6_target_absent

- Plan P6: Target absent between existing elements — input `arr=[1, 3, 5, 7], x=4`, expected `-1`
- Reviewer: The test correctly follows the specification. The implementation contains a bug: it sets hi = mid instead of hi = mid - 1, which prevents the search interval from shrinking and causes an infinite loop or out-of-bounds access when the target is absent.

```

```

## test_p8_single_element_no_match

- Plan P8: Single-element list without match — input `arr=[42], x=99`, expected `-1`
- Reviewer: The test correctly follows the specification. The implementation contains a bug: when the single element does not match, lo increments past hi, leading to mid pointing outside the array bounds and raising an IndexError.

```
_____
test_solution.py:9: in test_p8_single_element_no_match
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
FAILED test_solution.py::test_p8_single_element_no_match - IndexError: list i...
1 failed in 0.05s
```
