# Accepted by submit_tests; explanations in testgen_report.json.

from solution import normalize_tags as _case0_normalize_tags

def test_p1_standard_mixed_case():
    """Standard mixed case and whitespace handling matching the docstring example."""
    result = _case0_normalize_tags(' Python, ML ,python,, Data ')
    assert result == ['python', 'ml', 'data']

from solution import normalize_tags as _case1_normalize_tags

def test_p2_all_lowercase_no_whitespace():
    """All lowercase tags with no extra whitespace pass through unchanged."""
    result = _case1_normalize_tags('tag1,tag2,tag3')
    assert result == ['tag1', 'tag2', 'tag3']

from solution import normalize_tags as _case2_normalize_tags

def test_p3_duplicate_different_casing():
    """Duplicate tags with different casing are deduplicated, keeping first occurrence."""
    result = _case2_normalize_tags('Apple, apple, APPLE, banana')
    assert result == ['apple', 'banana']

from solution import normalize_tags as _case3_normalize_tags

def test_p4_only_commas_and_whitespace():
    """String containing only commas and whitespace yields an empty list."""
    result = _case3_normalize_tags(', , , ')
    assert result == []

from solution import normalize_tags as _case4_normalize_tags

def test_p5_single_tag_surrounding_whitespace():
    """Single tag with surrounding whitespace is stripped and returned."""
    result = _case4_normalize_tags('  hello  ')
    assert result == ['hello']

from solution import normalize_tags as _case5_normalize_tags

def test_p7_internal_spaces_preserved():
    """Internal spaces within tags are preserved; only surrounding whitespace is stripped."""
    result = _case5_normalize_tags('machine learning, deep learning')
    assert result == ['machine learning', 'deep learning']

from solution import normalize_tags as _case6_normalize_tags

def test_p6_leading_trailing_commas():
    """Leading and trailing commas produce empty tokens that are dropped."""
    result = _case6_normalize_tags(',  foo  , bar  ,')
    assert result == ['foo', 'bar']

from solution import normalize_tags as _case7_normalize_tags

def test_p8_multiple_consecutive_commas():
    """Multiple consecutive commas without spaces generate empty intermediate tokens."""
    result = _case7_normalize_tags('a,,,b')
    assert result == ['a', 'b']

from solution import normalize_tags as _case8_normalize_tags

def test_p9_uppercase_only_tags():
    """Tags with uppercase letters only are lower-cased."""
    result = _case8_normalize_tags('FOO, BAR')
    assert result == ['foo', 'bar']

from solution import normalize_tags as _case9_normalize_tags

def test_p10_order_preservation_interleaved_duplicates():
    """Order preservation with interleaved duplicates keeps first occurrence."""
    result = _case9_normalize_tags('cat, dog, cat, bird, dog')
    assert result == ['cat', 'dog', 'bird']

from solution import normalize_tags as _case10_normalize_tags

def test_extra_empty_string():
    """An empty string input returns an empty list."""
    result = _case10_normalize_tags('')
    assert result == []

from solution import normalize_tags as _case11_normalize_tags

def test_extra_single_tag_no_comma():
    """A single tag without any comma is returned as a one-element list."""
    result = _case11_normalize_tags('hello')
    assert result == ['hello']
