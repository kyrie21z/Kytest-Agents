# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

"""Fix test_basic_example_sorted: assert original input order, not alphabetical sort.
The docstring example shows normalize_tags(' Python, ML ,python,, Data ') should yield
['python', 'ml', 'data'] — preserving the order of first occurrences."""
from solution import normalize_tags

def test_basic_example_preserves_order():
    result = normalize_tags(' Python, ML ,python,, Data ')
    assert isinstance(result, list)
    # First unique tag encountered: 'Python' -> 'python'
    # Second: 'ML' -> 'ml'
    # Third: 'python' is duplicate (already seen), skipped
    # Fourth: empty string after ',,', skipped
    # Fifth: 'Data' -> 'data'
    assert result == ['python', 'ml', 'data'], f"Expected order preserved, got {result}"

"""Add a specification-valid test using non-alphabetical input.
Input: 'zebra, apple, banana'. Expected output must preserve original order:
['zebra', 'apple', 'banana']. This catches the implementation's incorrect
sorted() behavior which would produce ['apple', 'banana', 'zebra']."""
from solution import normalize_tags

def test_non_alphabetical_input_preserves_order():
    result = normalize_tags('zebra, apple, banana')
    assert isinstance(result, list)
    assert result == ['zebra', 'apple', 'banana'], \
        f"Expected original order ['zebra', 'apple', 'banana'], got {result}"

"""Test deduplication preserves the FIRST occurrence's position.
When duplicates appear later, they are dropped but the first one stays where it was."""
from solution import normalize_tags

def test_dedup_keeps_first_occurrence_position():
    result = normalize_tags('B, A, B, A, C')
    assert isinstance(result, list)
    # First 'B' at index 0, first 'A' at index 1, then 'B' dup skipped, 'A' dup skipped, 'C' at end
    assert result == ['b', 'a', 'c'], f"Expected ['b', 'a', 'c'], got {result}"

"""Test mixed case with non-alphabetical order: first occurrence wins for dedup."""
from solution import normalize_tags

def test_mixed_case_order_preservation():
    result = normalize_tags('Zebra, APPLE, zebra, Banana, apple')
    assert isinstance(result, list)
    # 'Zebra' -> 'zebra' (first), 'APPLE' -> 'apple' (second), 'zebra' dup skipped,
    # 'Banana' -> 'banana' (third), 'apple' dup skipped
    assert result == ['zebra', 'apple', 'banana'], \
        f"Expected ['zebra', 'apple', 'banana'], got {result}"
