# Accepted by submit_tests; explanations in testgen_report.json.

from solution import normalize_tags as _case0_normalize_tags

def test_p1_standard_mixed_case():
    """P1: Standard comma-separated tags with mixed case and surrounding whitespace
    are normalized, empty tags are dropped, and duplicates are removed while preserving order."""
    result = _case0_normalize_tags(' Python, ML ,python,, Data ')
    assert result == ['python', 'ml', 'data']
    assert isinstance(result, list)
    assert len(result) == 3

from solution import normalize_tags as _case1_normalize_tags

def test_p2_single_tag_no_commas():
    """P2: A single tag with no commas is stripped and lower-cased."""
    result = _case1_normalize_tags('  HelloWorld  ')
    assert result == ['helloworld']
    assert isinstance(result, list)
    assert len(result) == 1

from solution import normalize_tags as _case2_normalize_tags

def test_p4_empty_string():
    """P4: An empty input string yields an empty list."""
    result = _case2_normalize_tags('')
    assert result == []
    assert isinstance(result, list)

from solution import normalize_tags as _case3_normalize_tags

def test_p5_only_commas_and_whitespace():
    """P5: A string containing only commas and whitespace yields an empty list because
    all parsed tags are empty/whitespace-only."""
    result = _case3_normalize_tags(' , , , ')
    assert result == []
    assert isinstance(result, list)

from solution import normalize_tags as _case4_normalize_tags

def test_p3_duplicate_different_casing():
    """P3: Tags with identical content but different casing and spacing are treated
    as duplicates after normalization; only the first is kept."""
    result = _case4_normalize_tags('Apple, apple, APPLE , app le')
    assert result == ['apple', 'app le']
    assert isinstance(result, list)
    assert len(result) == 2

from solution import normalize_tags as _case5_normalize_tags

def test_p7_order_preservation():
    """P7: Original order of distinct tags is preserved regardless of case variations
    in later duplicates."""
    result = _case5_normalize_tags('Zebra, Apple, zebra, Banana')
    assert result == ['zebra', 'apple', 'banana']
    assert isinstance(result, list)
    assert len(result) == 3

from solution import normalize_tags as _case6_normalize_tags

def test_p6_consecutive_trailing_commas():
    """P6: Consecutive commas and trailing commas produce empty segments that are correctly ignored."""
    result = _case6_normalize_tags('tag1,,,tag2,')
    assert result == ['tag1', 'tag2']
    assert isinstance(result, list)
    assert len(result) == 2

from solution import normalize_tags as _case7_normalize_tags

def test_p8_internal_whitespace_preserved():
    """P8: Internal whitespace within a tag is preserved; only leading/trailing whitespace is removed."""
    result = _case7_normalize_tags('  hello   world  , foo ')
    assert result == ['hello   world', 'foo']
    assert isinstance(result, list)
    assert len(result) == 2

from solution import normalize_tags as _case8_normalize_tags

def test_extra_single_tag_no_spaces():
    """Extra: A single lowercase tag with no surrounding whitespace returns itself."""
    result = _case8_normalize_tags('hello')
    assert result == ['hello']
    assert isinstance(result, list)
    assert len(result) == 1

from solution import normalize_tags as _case9_normalize_tags

def test_extra_all_duplicates():
    """Extra: When every tag is a duplicate of the first after normalization, only one remains."""
    result = _case9_normalize_tags('Foo, FOO, foo,  Foo  ')
    assert result == ['foo']
    assert isinstance(result, list)
    assert len(result) == 1
