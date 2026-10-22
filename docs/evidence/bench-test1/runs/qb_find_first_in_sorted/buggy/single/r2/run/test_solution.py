# Accepted by submit_tests; explanations in testgen_report.json.

"""Test the exact example given in the docstring.

Contract quote: 'The lowest index i such that arr[i] == x, or -1 if x not in arr'
Input domain: arr=[3, 4, 5, 5, 5, 5, 6], x=5
Expected: 2, because arr[2]==5 and arr[1]==4!=5, so index 2 is the first occurrence.
Fault hypothesis: Detects off-by-one errors or failure to find the *first* duplicate.
"""
from solution import find_first_in_sorted as _case0_find_first_in_sorted

def test_docstring_example():
    assert _case0_find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5) == 2

"""Test finding the only element in a single-element array.

Contract quote: 'The lowest index i such that arr[i] == x'
Input domain: arr=[42], x=42
Expected: 0, since the sole element at index 0 matches x.
Fault hypothesis: Detects returning wrong index or failing on trivial input.
"""
from solution import find_first_in_sorted as _case1_find_first_in_sorted

def test_single_element_found():
    assert _case1_find_first_in_sorted([42], 42) == 0

"""Test finding the first element when it is the target.

Contract quote: 'The lowest index i such that arr[i] == x'
Input domain: arr=[1, 2, 3, 4, 5], x=1
Expected: 0, because arr[0]==1 and it is the first (and only) occurrence.
Fault hypothesis: Detects returning -1 or skipping index 0.
"""
from solution import find_first_in_sorted as _case2_find_first_in_sorted

def test_first_element_of_array():
    assert _case2_find_first_in_sorted([1, 2, 3, 4, 5], 1) == 0

"""Test finding the last element when it is the target.

Contract quote: 'The lowest index i such that arr[i] == x'
Input domain: arr=[1, 2, 3, 4, 5], x=5
Expected: 4, because arr[4]==5 and it is the first (and only) occurrence.
Fault hypothesis: Detects binary search boundary errors near the end.
"""
from solution import find_first_in_sorted as _case3_find_first_in_sorted

def test_last_element_of_array():
    assert _case3_find_first_in_sorted([1, 2, 3, 4, 5], 5) == 4

"""Test finding the first element in an array where all elements are equal.

Contract quote: 'The lowest index i such that arr[i] == x'
Input domain: arr=[7, 7, 7, 7, 7], x=7
Expected: 0, because every element equals 7, so the lowest index is 0.
Fault hypothesis: Detects failure to converge to the leftmost duplicate.
"""
from solution import find_first_in_sorted as _case4_find_first_in_sorted

def test_all_identical_elements():
    assert _case4_find_first_in_sorted([7, 7, 7, 7, 7], 7) == 0

"""Test with negative integers in the sorted array.

Contract quote: 'A sorted list of ints'
Input domain: arr=[-10, -5, -3, 0, 2, 8], x=-5
Expected: 1, because arr[1]==-5 and arr[0]==-10!=-5.
Fault hypothesis: Detects sign-related comparison bugs in binary search.
"""
from solution import find_first_in_sorted as _case5_find_first_in_sorted

def test_negative_values():
    assert _case5_find_first_in_sorted([-10, -5, -3, 0, 2, 8], -5) == 1
