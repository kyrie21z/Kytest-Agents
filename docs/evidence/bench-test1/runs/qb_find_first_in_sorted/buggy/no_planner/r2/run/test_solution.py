# Accepted by submit_tests; explanations in testgen_report.json.

def test_docstring_example():
    """
    Quote: 'The lowest index i such that arr[i] == x, or -1 if x not in arr'
    Input domain: arr=[3,4,5,5,5,5,6], x=5
    Expected: 2 — the first occurrence of 5 is at index 2.
    Fault hypothesis: Function might return last occurrence or any duplicate index.
    """
    from solution import find_first_in_sorted
    result = find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5)
    assert result == 2

def test_single_element_found():
    """
    Quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr=[42], x=42
    Expected: 0 — only one element, it matches.
    Fault hypothesis: Returns -1 for single-element match.
    """
    from solution import find_first_in_sorted
    result = find_first_in_sorted([42], 42)
    assert result == 0

def test_first_of_duplicates():
    """
    Quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr=[1, 2, 2, 2, 3], x=2
    Expected: 1 — first of three consecutive 2s starts at index 1.
    Fault hypothesis: Returns last duplicate index (3) instead of first (1).
    """
    from solution import find_first_in_sorted
    result = find_first_in_sorted([1, 2, 2, 2, 3], 2)
    assert result == 1

def test_two_element_duplicate():
    """
    Quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr=[5, 5], x=5
    Expected: 0 — first of two identical elements.
    Fault hypothesis: Returns 1 (second occurrence) instead of 0.
    """
    from solution import find_first_in_sorted
    result = find_first_in_sorted([5, 5], 5)
    assert result == 0

def test_return_type_is_int():
    """
    Quote: 'Output:
        The lowest index i such that arr[i] == x, or -1 if x not in arr'
    Input domain: arr=[1, 2, 3], x=2
    Expected: int type returned.
    Fault hypothesis: Returns float, None, or other unexpected type.
    """
    from solution import find_first_in_sorted
    result = find_first_in_sorted([1, 2, 3], 2)
    assert isinstance(result, int)

def test_element_at_end():
    """
    Quote: 'The lowest index i such that arr[i] == x, or -1 if x not in arr'
    Input domain: arr=[1, 3, 5, 7], x=7
    Expected: 3 — last element matches.
    Fault hypothesis: Fails to reach the last element in binary search.
    """
    from solution import find_first_in_sorted
    result = find_first_in_sorted([1, 3, 5, 7], 7)
    assert result == 3

def test_all_same_elements():
    """
    Quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr=[7, 7, 7, 7], x=7
    Expected: 0 — all elements are 7, lowest index is 0.
    Fault hypothesis: Returns wrong index among identical values.
    """
    from solution import find_first_in_sorted
    result = find_first_in_sorted([7, 7, 7, 7], 7)
    assert result == 0

def test_negative_numbers():
    """
    Quote: 'A sorted list of ints' / 'The lowest index i such that arr[i] == x'
    Input domain: arr=[-10, -5, 0, 5, 10], x=-5
    Expected: 1 — negative numbers are handled correctly.
    Fault hypothesis: Sign handling bug misroutes binary search.
    """
    from solution import find_first_in_sorted
    result = find_first_in_sorted([-10, -5, 0, 5, 10], -5)
    assert result == 1

def test_many_duplicates_first_index():
    """
    Quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr=[7]*50 + [8], x=7
    Expected: 0 — first of 50 identical values.
    Fault hypothesis: Linear scan behavior or wrong midpoint logic misses index 0.
    """
    from solution import find_first_in_sorted
    result = find_first_in_sorted([7] * 50 + [8], 7)
    assert result == 0

def test_element_at_start():
    """
    Quote: 'The lowest index i such that arr[i] == x'
    Input domain: arr=[1, 3, 5, 7], x=1
    Expected: 0 — first element matches.
    Fault hypothesis: Skips past index 0 due to off-by-one in binary search.
    """
    from solution import find_first_in_sorted
    result = find_first_in_sorted([1, 3, 5, 7], 1)
    assert result == 0

def test_two_elements_both():
    """
    Quote: 'The lowest index i such that arr[i] == x, or -1 if x not in arr'
    Input domain: arr=[10, 20], x=10 and x=20
    Expected: 0 for x=10, 1 for x=20.
    Fault hypothesis: Off-by-one errors cause incorrect results on small arrays.
    """
    from solution import find_first_in_sorted
    assert find_first_in_sorted([10, 20], 10) == 0
    assert find_first_in_sorted([10, 20], 20) == 1
