# Accepted by submit_tests; explanations in testgen_report.json.

from solution import normalize_tags as _case0_normalize_tags

def test_p2_single_tag():
    result = _case0_normalize_tags('hello')
    assert result == ['hello']

from solution import normalize_tags as _case1_normalize_tags

def test_p3_empty_string():
    result = _case1_normalize_tags('')
    assert result == []

from solution import normalize_tags as _case2_normalize_tags

def test_p4_commas_only():
    result = _case2_normalize_tags(', , , ')
    assert result == []

from solution import normalize_tags as _case3_normalize_tags

def test_p5_case_insensitive_duplicates():
    result = _case3_normalize_tags('Apple, apple, APPLE')
    assert result == ['apple']

from solution import normalize_tags as _case4_normalize_tags

def test_p7_leading_trailing_commas():
    """Tests leading and trailing commas with a single valid tag in the middle.

    Contract quote:
      Empty tags (including ones that are only whitespace) are dropped.

    Input domain:
      A string like '  ,tag1,  ' where leading/trailing commas produce empty segments.

    Oracle / expected result:
      Split on ',' → ['', 'tag1', '  ']; strip+lower → ['', 'tag1', '']; drop empties
      → ['tag1']. Result is ['tag1'].

    Fault hypothesis:
      If empty/whitespace-only segments are not properly filtered, the output would
      contain '' entries or miss the valid tag.
    """
    result = _case4_normalize_tags('  ,tag1,  ')
    assert result == ['tag1']

from solution import normalize_tags as _case5_normalize_tags

def test_p9_whitespace_only_string():
    """Tests a string containing only whitespace characters.

    Contract quote:
      Empty tags (including ones that are only whitespace) are dropped.

    Input domain:
      A string of only whitespace: '   	
   '

    Oracle / expected result:
      Split on ',' → ['   	
   ']; strip+lower → ''; empty → filtered → [].

    Fault hypothesis:
      If whitespace-only strings are not treated as empty after stripping, the result
      might contain unexpected elements.
    """
    result = _case5_normalize_tags('   \t\n   ')
    assert result == []

from solution import normalize_tags as _case6_normalize_tags

def test_p10_standard_compact():
    """Tests standard compact comma-separated input without extra spacing.

    Contract quote:
      Each tag is stripped of surrounding whitespace and lower-cased.

    Input domain:
      Compact input: 'Tag1,Tag2,Tag3'

    Oracle / expected result:
      Split on ',' → ['Tag1', 'Tag2', 'Tag3']; strip+lower → ['tag1', 'tag2', 'tag3'];
      all unique → ['tag1', 'tag2', 'tag3'].

    Fault hypothesis:
      If lowercasing is missing, the result would retain original casing ['Tag1','Tag2','Tag3'].
    """
    result = _case6_normalize_tags('Tag1,Tag2,Tag3')
    assert result == ['tag1', 'tag2', 'tag3']

from solution import normalize_tags as _case7_normalize_tags

def test_extra_return_type_list():
    """Verifies the return type is always a list for various inputs.

    Contract quote:
      Turn a comma-separated tag string into a list of normalized tags.

    Input domain:
      Various inputs including empty string, single tag, and multi-tag strings.

    Oracle / expected result:
      All calls must return instances of list.

    Fault hypothesis:
      Returning None, a tuple, or any non-list type would violate the documented return type.
    """
    assert isinstance(_case7_normalize_tags(''), list)
    assert isinstance(_case7_normalize_tags('hello'), list)
    assert isinstance(_case7_normalize_tags('a,b,c'), list)
