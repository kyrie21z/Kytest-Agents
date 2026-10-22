# Accepted by submit_tests; explanations in testgen_report.json.

"""Test P1: Standard multi-tag input with mixed case and extra whitespace."""
from solution import normalize_tags as _case0_normalize_tags

def test_p1_mixed_case_whitespace():
    result = _case0_normalize_tags(' Python, ML ,python,, Data ')
    assert result == ['python', 'ml', 'data']

"""Test P2: Input contains only whitespace and commas."""
from solution import normalize_tags as _case1_normalize_tags

def test_p2_only_whitespace_and_commas():
    result = _case1_normalize_tags('   ,  ,   ')
    assert result == []

"""Test P3: Input is an empty string."""
from solution import normalize_tags as _case2_normalize_tags

def test_p3_empty_string():
    result = _case2_normalize_tags('')
    assert result == []

"""Test P5: Order preservation across different cases and duplicates."""
from solution import normalize_tags as _case3_normalize_tags

def test_p5_order_preservation():
    result = _case3_normalize_tags('Zebra, apple, ZEBRA, Apple')
    assert result == ['zebra', 'apple']

"""Test P6: Leading and trailing commas produce empty segments."""
from solution import normalize_tags as _case4_normalize_tags

def test_p6_leading_trailing_commas():
    result = _case4_normalize_tags(',tag1,tag2,')
    assert result == ['tag1', 'tag2']

"""Test P4: Duplicate tags appear after normalization."""
from solution import normalize_tags as _case5_normalize_tags

def test_p4_duplicate_tags_after_normalization():
    result = _case5_normalize_tags('Apple, BANANA, apple')
    assert result == ['apple', 'banana']

"""Test P7: Single tag with surrounding whitespace."""
from solution import normalize_tags as _case6_normalize_tags

def test_p7_single_tag_with_whitespace():
    result = _case6_normalize_tags('  Machine Learning  ')
    assert result == ['machine learning']

"""Test P8: Tags with special characters and numbers retain them after normalization."""
from solution import normalize_tags as _case7_normalize_tags

def test_p8_special_characters_and_numbers():
    result = _case7_normalize_tags('Tag-1, TAG_2, tag-1')
    assert result == ['tag-1', 'tag_2']
