# Suspected implementation bugs

## test_p3_not_present

- Plan P3: Target not present in array — input `arr=[1, 2, 3], x=4`, expected `-1`
- Reviewer: Test follows specification. Fails due to implementation bug: hi=len(arr) allows mid to equal len(arr), causing IndexError on arr[mid].

```
_________
test_solution.py:6: in test_p3_not_present
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
FAILED test_solution.py::test_p3_not_present - IndexError: list index out of ...
1 failed in 0.03s
```

## test_p4_empty_list

- Plan P4: Empty input array — input `arr=[], x=1`, expected `-1`
- Reviewer: Test follows specification. Fails due to implementation bug: hi=len(arr) causes mid=0 on an empty array, triggering IndexError.

```
________________________
test_solution.py:6: in test_p4_empty_list
    result = find_first_in_sorted([], 1)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
_testgen_contracts.py:375: in guarded
    return function(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
solution.py:22: in find_first_in_sorted
    if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            ^^^^^^^^
E   IndexError: list index out of range
=========================== short test summary info ============================
FAILED test_solution.py::test_p4_empty_list - IndexError: list index out of r...
1 failed in 0.05s
```

## test_p6_single_no_match

- Plan P6: Single element array, does not match target — input `arr=[5], x=3`, expected `-1`
- Reviewer: Test follows specification. Fails due to implementation bug causing out-of-bounds access or incorrect loop termination logic.

```

```

## test_p7_target_smaller

- Plan P7: Target smaller than all elements — input `arr=[2, 3, 4], x=1`, expected `-1`
- Reviewer: Test follows specification. Fails due to implementation bug causing out-of-bounds access.

```

```

## test_p8_target_larger

- Plan P8: Target larger than all elements — input `arr=[2, 3, 4], x=5`, expected `-1`
- Reviewer: Test follows specification. Fails due to implementation bug: hi=len(arr) allows mid to equal len(arr), causing IndexError.

```
_______
test_solution.py:6: in test_p8_target_larger
    result = find_first_in_sorted([2, 3, 4], 5)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_testgen_contracts.py:375: in guarded
    return function(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
solution.py:22: in find_first_in_sorted
    if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            ^^^^^^^^
E   IndexError: list index out of range
=========================== short test summary info ============================
FAILED test_solution.py::test_p8_target_larger - IndexError: list index out o...
1 failed in 0.04s
```
