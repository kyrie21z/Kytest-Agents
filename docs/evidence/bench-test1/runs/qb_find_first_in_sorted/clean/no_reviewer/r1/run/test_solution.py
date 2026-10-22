# Accepted by submit_tests; explanations in testgen_report.json.

def test_p1_middle_duplicates():
    from solution import find_first_in_sorted
    assert find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5) == 2

def test_p2_start_duplicates():
    from solution import find_first_in_sorted
    assert find_first_in_sorted([5, 5, 6, 7], 5) == 0

def test_p3_tail_duplicates():
    from solution import find_first_in_sorted
    assert find_first_in_sorted([3, 4, 5, 5, 5], 5) == 2

def test_p4_empty_list():
    from solution import find_first_in_sorted
    assert find_first_in_sorted([], 5) == -1

def test_p5_single_match():
    from solution import find_first_in_sorted
    assert find_first_in_sorted([10], 10) == 0

def test_p6_single_no_match():
    from solution import find_first_in_sorted
    assert find_first_in_sorted([10], 5) == -1

def test_p7_underflow():
    from solution import find_first_in_sorted
    assert find_first_in_sorted([5, 6, 7], 2) == -1

def test_p8_overflow():
    from solution import find_first_in_sorted
    assert find_first_in_sorted([2, 3, 4], 8) == -1

def test_p9_all_equal():
    from solution import find_first_in_sorted
    assert find_first_in_sorted([5, 5, 5], 5) == 0

def test_p10_between_values():
    from solution import find_first_in_sorted
    assert find_first_in_sorted([1, 3, 5], 4) == -1
