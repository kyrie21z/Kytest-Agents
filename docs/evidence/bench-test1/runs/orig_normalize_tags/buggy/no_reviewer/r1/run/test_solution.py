# Accepted by submit_tests; explanations in testgen_report.json.

from solution import normalize_tags as _case0_normalize_tags

def test_p2_empty_string():
    """P2: Returns an empty list when given an empty string."""
    result = _case0_normalize_tags('')
    assert result == []

from solution import normalize_tags as _case1_normalize_tags

def test_p3_whitespace_only():
    """P3: Returns an empty list when all tokens are whitespace-only."""
    result = _case1_normalize_tags(', ,  , ')
    assert result == []

from solution import normalize_tags as _case2_normalize_tags

def test_p4_single_tag_no_delimiter():
    """P4: Handles a single tag with no delimiters, stripping only surrounding whitespace."""
    result = _case2_normalize_tags('  Hello World  ')
    assert result == ['hello world']

from solution import normalize_tags as _case3_normalize_tags

def test_p5_case_insensitive_duplicates():
    """P5: Removes case-insensitive duplicates, keeping only the first occurrence."""
    result = _case3_normalize_tags('Data,data,DATA')
    assert result == ['data']

from solution import normalize_tags as _case4_normalize_tags

def test_p6_leading_trailing_commas():
    """P6: Correctly handles leading, trailing, and consecutive commas."""
    result = _case4_normalize_tags(',tag1,,tag2,')
    assert result == ['tag1', 'tag2']

from solution import normalize_tags as _case5_normalize_tags

def test_p7_order_preservation():
    """P7: Preserves original order while filtering out subsequent duplicates."""
    result = _case5_normalize_tags('a,b,a,c,b,d')
    assert result == ['a', 'b', 'c', 'd']

from solution import normalize_tags as _case6_normalize_tags

def test_p10_single_exact_tag():
    """P10: Returns a single-element list for a tag with no surrounding whitespace."""
    result = _case6_normalize_tags('exact')
    assert result == ['exact']

from solution import normalize_tags as _case7_normalize_tags

def test_extra_return_type():
    """Extra: Verifies the return type is always a list."""
    result_empty = _case7_normalize_tags('')
    result_single = _case7_normalize_tags('hello')
    result_multi = _case7_normalize_tags('a,b,c')
    assert isinstance(result_empty, list)
    assert isinstance(result_single, list)
    assert isinstance(result_multi, list)

from solution import normalize_tags as _case8_normalize_tags

def test_extra_boundary_single_comma():
    """Extra: A single comma between two tags produces exactly two normalized tags."""
    result = _case8_normalize_tags('a,b')
    assert result == ['a', 'b']
    assert len(result) == 2

from solution import normalize_tags as _case9_normalize_tags

def test_extra_all_same_duplicate():
    """Extra: All identical tokens reduce to a single-element list."""
    result = _case9_normalize_tags('foo, foo ,FOO,Foo')
    assert result == ['foo']
