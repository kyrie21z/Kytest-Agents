# Accepted by submit_tests; explanations in testgen_report.json.

def test_basic_duplicate_middle():
    from solution import find_first_in_sorted
    result = find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5)
    assert result == 2

def test_empty_array():
    from solution import find_first_in_sorted
    result = find_first_in_sorted([], 5)
    assert result == -1

def test_single_element_match():
    from solution import find_first_in_sorted
    result = find_first_in_sorted([5], 5)
    assert result == 0

def test_all_same_elements():
    from solution import find_first_in_sorted
    result = find_first_in_sorted([5, 5, 5, 5], 5)
    assert result == 0

def test_not_present_smaller():
    from solution import find_first_in_sorted
    result = find_first_in_sorted([3, 4, 5], 2)
    assert result == -1

def test_last_element():
    from solution import find_first_in_sorted
    result = find_first_in_sorted([1, 2, 3], 3)
    assert result == 2
