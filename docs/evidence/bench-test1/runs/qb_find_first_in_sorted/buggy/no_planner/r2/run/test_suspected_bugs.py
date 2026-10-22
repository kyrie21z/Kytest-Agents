# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

def test_not_found_smaller_than_min():
    """
    Quote: 'or -1 if x not in arr'
    Input domain: arr=[5, 10, 15], x=3
    Expected: -1 — value smaller than all elements.
    Fault hypothesis: Returns 0 or some wrong index instead of -1.
    """
    from solution import find_first_in_sorted
    result = find_first_in_sorted([5, 10, 15], 3)
    assert result == -1

def test_not_found_larger_than_max():
    """
    Quote: 'or -1 if x not in arr'
    Input domain: arr=[5, 10, 15], x=20
    Expected: -1 — value larger than all elements.
    Fault hypothesis: Returns len(arr) or some wrong index instead of -1.
    """
    from solution import find_first_in_sorted
    result = find_first_in_sorted([5, 10, 15], 20)
    assert result == -1

def test_not_found_between_elements():
    """
    Quote: 'or -1 if x not in arr'
    Input domain: arr=[1, 3, 5, 7], x=4
    Expected: -1 — value falls between existing elements.
    Fault hypothesis: Binary search lands on wrong position and returns it.
    """
    from solution import find_first_in_sorted
    result = find_first_in_sorted([1, 3, 5, 7], 4)
    assert result == -1

def test_single_element_not_found():
    """
    Quote: 'or -1 if x not in arr'
    Input domain: arr=[42], x=99
    Expected: -1 — value not present in single-element array.
    Fault hypothesis: Crashes with IndexError instead of returning -1.
    """
    from solution import find_first_in_sorted
    result = find_first_in_sorted([42], 99)
    assert result == -1
