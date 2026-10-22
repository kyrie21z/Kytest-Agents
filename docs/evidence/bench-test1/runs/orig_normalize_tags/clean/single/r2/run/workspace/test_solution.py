# Accepted by submit_tests; explanations in testgen_report.json.

from solution import normalize_tags as _case0_normalize_tags

def test_docstring_example():
    """Quote: '>>> normalize_tags(" Python, ML ,python,, Data ")
    ['python', 'ml', 'data']'

    Input domain: A comma-separated string with mixed-case tags, surrounding
    whitespace on some tags, and a double-comma producing an empty slot.

    Oracle: After normalizing (strip + lowercase), the expected unique tags in
    order of first appearance are 'python', 'ml', 'data'. The duplicate 'python'
    (second occurrence) must be dropped.

    Fault hypothesis: If the implementation fails to deduplicate or fails to
    strip/lowercase, the result will contain extra elements or wrong casing.
    """
    result = _case0_normalize_tags(' Python, ML ,python,, Data ')
    assert result == ['python', 'ml', 'data']

from solution import normalize_tags as _case1_normalize_tags

def test_empty_string():
    """Quote: 'A string without any non-empty tag gives an empty list.'

    Input domain: An empty string "" — no characters at all.

    Oracle: split(",") on "" yields [""], which strips to "" and is falsy, so
    nothing is appended. Expected result is [].

    Fault hypothesis: If the function does not handle the empty-string edge case,
    it might return [""] or crash.
    """
    result = _case1_normalize_tags('')
    assert result == []

from solution import normalize_tags as _case2_normalize_tags

def test_only_commas():
    """Quote: 'Empty tags (including ones that are only whitespace) are dropped.'

    Input domain: A string consisting solely of commas ",,," — every split token
    is empty or whitespace-only.

    Oracle: All tokens are empty after strip; none pass the truthiness check.
    Expected result is [].

    Fault hypothesis: A bug that does not filter empty tokens could return
    unexpected entries.
    """
    result = _case2_normalize_tags(',,,')
    assert result == []

from solution import normalize_tags as _case3_normalize_tags

def test_all_duplicates_preserves_first():
    """Quote: 'Duplicates, compared after normalization, are removed so that
    only the first occurrence is kept, and the remaining tags keep their
    original order.'

    Input domain: "A, a, A,  a " — four tokens that all normalize to "a".

    Oracle: Only the first normalized form should survive. Expected result is
    ["a"].

    Fault hypothesis: If deduplication uses a set instead of preserving insertion
    order / first occurrence, or if it compares raw (pre-normalized) values,
    results may differ.
    """
    result = _case3_normalize_tags('A, a, A,  a ')
    assert result == ['a']

from solution import normalize_tags as _case4_normalize_tags

def test_multiple_distinct_tags_order_preserved():
    """Quote: 'the remaining tags keep their original order.'

    Input domain: "Zebra, apple, Banana" — three distinct tags with varied
    casing.

    Oracle: After normalization the order of first appearance is preserved:
    ["zebra", "apple", "banana"].

    Fault hypothesis: If sorting is applied, the order would change.
    """
    result = _case4_normalize_tags('Zebra, apple, Banana')
    assert result == ['zebra', 'apple', 'banana']

from solution import normalize_tags as _case5_normalize_tags

def test_return_type_is_list():
    """Quote: Implicit contract — the function returns a list.

    Input domain: Any valid input, here "tag1, tag2".

    Oracle: The return value must be a Python list instance.

    Fault hypothesis: If the function accidentally returns a tuple or other type,
    downstream code expecting list methods would break.
    """
    result = _case5_normalize_tags('tag1, tag2')
    assert isinstance(result, list)
