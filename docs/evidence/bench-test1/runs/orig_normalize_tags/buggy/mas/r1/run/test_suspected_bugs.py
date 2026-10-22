# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

from solution import normalize_tags

def test_p1_mixed_case_whitespace():
    result = normalize_tags(" Python, ML ,python,, Data ")
    assert result == ["python", "ml", "data"]

from solution import normalize_tags

def test_p6_order_preservation():
    result = normalize_tags("cherry, banana, cherry, date, banana")
    assert result == ["cherry", "banana", "date"]

from solution import normalize_tags

def test_p8_internal_spaces_and_punctuation():
    """Tests preservation of internal spaces and punctuation within tags.

    Contract quote:
      Each tag is stripped of surrounding whitespace and lower-cased.

    Input domain:
      Tags containing internal spaces and punctuation: 'hello world, foo-bar!'

    Oracle / expected result:
      Split on ',' → ['hello world', ' foo-bar!']; strip+lower → ['hello world', 'foo-bar!'];
      both non-empty and unique → ['hello world', 'foo-bar!'].

    Fault hypothesis:
      If the implementation removes internal characters (e.g. via regex), the output
      would differ from the expected preserved content.
    """
    result = normalize_tags("hello world, foo-bar!")
    assert result == ["hello world", "foo-bar!"]

from solution import normalize_tags

def test_extra_duplicate_removal_first_kept():
    """Verifies that when duplicates exist, only the first occurrence's position is kept.

    Contract quote:
      Duplicates, compared after normalization, are removed so that only the first
      occurrence is kept.

    Input domain:
      'Zebra, apple, ZEBRA' — 'Zebra' appears twice with different casing.

    Oracle / expected result:
      Normalized: ['zebra', 'apple', 'zebra']; deduplicate keeping first → ['zebra', 'apple'].
      Note: this also tests that order is preserved (first occurrence at index 0).

    Fault hypothesis:
      If sorted() is used, result becomes ['apple', 'zebra'], losing original order.
      If last occurrence is kept instead of first, result would be ['apple', 'zebra'].
    """
    result = normalize_tags("Zebra, apple, ZEBRA")
    assert result == ["zebra", "apple"]
