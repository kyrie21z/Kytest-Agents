# Accepted by submit_tests; explanations in testgen_report.json.

from solution import normalize_tags as _case0_normalize_tags

def test_empty_string():
    """An empty input string should produce an empty list."""
    result = _case0_normalize_tags('')
    assert result == []
    assert isinstance(result, list)

from solution import normalize_tags as _case1_normalize_tags

def test_only_commas_and_whitespace():
    """A string containing only commas and whitespace should yield an empty list."""
    result = _case1_normalize_tags(', ,  ,')
    assert result == []
    assert isinstance(result, list)
    result2 = _case1_normalize_tags(',,, ')
    assert result2 == []

from solution import normalize_tags as _case2_normalize_tags

def test_duplicate_removal_preserves_order():
    """Duplicates after normalization are removed; first occurrence order is kept."""
    result = _case2_normalize_tags('Apple, banana, APPLE, Banana, cherry, apple')
    assert result == ['apple', 'banana', 'cherry']
    assert len(result) == 3
    assert result.index('apple') < result.index('banana')
    assert result.index('banana') < result.index('cherry')

from solution import normalize_tags as _case3_normalize_tags

def test_single_tag_with_whitespace():
    """A single tag surrounded by whitespace should be normalized correctly."""
    result = _case3_normalize_tags('   Hello World   ')
    assert result == ['hello world']
    assert isinstance(result, list)
    assert len(result) == 1
    result2 = _case3_normalize_tags('simple')
    assert result2 == ['simple']

from solution import normalize_tags as _case4_normalize_tags

def test_consecutive_commas_and_edge_cases():
    """Multiple consecutive commas produce empty tags that should be dropped."""
    result = _case4_normalize_tags('a,,,b')
    assert result == ['a', 'b']
    result2 = _case4_normalize_tags('tag1,tag2,')
    assert result2 == ['tag1', 'tag2']
    result3 = _case4_normalize_tags(',tag1,tag2')
    assert result3 == ['tag1', 'tag2']
    result4 = _case4_normalize_tags('a,b,c')
    assert result4 == ['a', 'b', 'c']
    result5 = _case4_normalize_tags(' hello  world , foo bar ')
    assert result5 == ['hello  world', 'foo bar']

from solution import normalize_tags as _case5_normalize_tags

def test_basic_normalization():
    """Test the documented example: mixed case, whitespace, duplicates."""
    result = _case5_normalize_tags(' Python, ML ,python,, Data ')
    assert result == ['python', 'ml', 'data']
