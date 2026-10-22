# Accepted by submit_tests; explanations in testgen_report.json.

from solution import normalize_tags as _case0_normalize_tags

def test_p1_standard_mixed_case_whitespace_duplicates():
    result = _case0_normalize_tags(' Python, ML ,python,, Data ')
    assert result == ['python', 'ml', 'data']
    assert isinstance(result, list)

from solution import normalize_tags as _case1_normalize_tags

def test_p2_empty_string():
    result = _case1_normalize_tags('')
    assert result == []
    assert isinstance(result, list)

from solution import normalize_tags as _case2_normalize_tags

def test_p3_only_commas_and_whitespace():
    result = _case2_normalize_tags(', , , ')
    assert result == []
    assert isinstance(result, list)

from solution import normalize_tags as _case3_normalize_tags

def test_p4_duplicate_tags_different_casing_preserve_first():
    result = _case3_normalize_tags('A, b, A, B')
    assert result == ['a', 'b']
    assert isinstance(result, list)

from solution import normalize_tags as _case4_normalize_tags

def test_p5_single_tag_with_surrounding_whitespace():
    result = _case4_normalize_tags('  Hello  ')
    assert result == ['hello']
    assert isinstance(result, list)

from solution import normalize_tags as _case5_normalize_tags

def test_p6_leading_and_trailing_commas():
    result = _case5_normalize_tags(',tag1,tag2,')
    assert result == ['tag1', 'tag2']
    assert isinstance(result, list)

from solution import normalize_tags as _case6_normalize_tags

def test_p7_multiple_consecutive_commas():
    result = _case6_normalize_tags('a,,,b')
    assert result == ['a', 'b']
    assert isinstance(result, list)

from solution import normalize_tags as _case7_normalize_tags

def test_p8_internal_whitespace_preserved():
    result = _case7_normalize_tags('foo bar, baz qux')
    assert result == ['foo bar', 'baz qux']
    assert isinstance(result, list)
