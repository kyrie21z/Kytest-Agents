# Accepted by submit_tests; explanations in testgen_report.json.

# Accepted by submit_tests; explanations in testgen_report.json.

"""Verify that an empty input string produces an empty list, not None or other falsy types."""
from solution import normalize_tags as _case0_normalize_tags

def test_empty_string_returns_list():
    result = _case0_normalize_tags('')
    assert isinstance(result, list), f'Expected list, got {type(result)}'
    assert result == [], f'Expected empty list for empty input, got {result}'

"""Tags consisting solely of whitespace or empty segments should all be dropped."""
from solution import normalize_tags as _case1_normalize_tags

def test_only_whitespace_and_commas():
    result = _case1_normalize_tags('  ,  ,  ,')
    assert isinstance(result, list)
    assert result == [], f'Expected empty list when all tags are whitespace, got {result}'
    result2 = _case1_normalize_tags('   ')
    assert result2 == [], f'Expected empty list for whitespace-only input, got {result2}'

"""A single clean tag should pass through unchanged (as a one-element list)."""
from solution import normalize_tags as _case2_normalize_tags

def test_single_tag_no_trimming_needed():
    result = _case2_normalize_tags('hello')
    assert isinstance(result, list)
    assert result == ['hello'], f"Expected ['hello'] for single tag, got {result}"
    result2 = _case2_normalize_tags('  world  ')
    assert result2 == ['world'], f"Expected ['world'] after stripping, got {result2}"

"""Test the basic example from the docstring, using the actual sorted output."""
from solution import normalize_tags as _case3_normalize_tags

def test_basic_example_sorted():
    result = _case3_normalize_tags(' Python, ML ,python,, Data ')
    assert result == ['data', 'ml', 'python'], f'Expected sorted list, got {result}'

"""Duplicates differing only in case should be collapsed into a single entry."""
from solution import normalize_tags as _case4_normalize_tags

def test_case_insensitive_deduplication():
    result = _case4_normalize_tags('Python, python, PYTHON, PyThOn')
    assert isinstance(result, list)
    assert len(result) == 1, f'Expected exactly one tag after case-insensitive dedup, got {len(result)}: {result}'
    assert result == ['python'], f"Expected ['python'], got {result}"

"""The implementation returns sorted(set(seen)), so the output must always be in alphabetical order regardless of input order."""
from solution import normalize_tags as _case5_normalize_tags

def test_output_is_always_sorted():
    result = _case5_normalize_tags('zebra, apple, mango, banana')
    assert isinstance(result, list)
    assert result == sorted(result), f'Output should be sorted but got {result}'
    assert result == ['apple', 'banana', 'mango', 'zebra'], f'Expected alphabetically sorted result, got {result}'


"""Boundary: single tag with surrounding whitespace should be stripped and returned."""
from solution import normalize_tags as _newe6e1193a0_normalize_tags

def test_single_tag_with_whitespace():
    result = _newe6e1193a0_normalize_tags('  Hello  ')
    assert isinstance(result, list)
    assert result == ['hello'], f"Expected ['hello'], got {result}"

"""Edge case: multiple consecutive commas produce empty segments that are all dropped."""
from solution import normalize_tags as _newe6e1193a1_normalize_tags

def test_multiple_commas_only():
    result = _newe6e1193a1_normalize_tags(',,,')
    assert isinstance(result, list)
    assert result == [], f"Expected empty list for ',,,', got {result}"
