# Accepted by submit_tests; explanations in testgen_report.json.

def test_basic_normalization():
    """Test basic tag normalization: strip, lowercase, deduplicate, preserve order."""
    from solution import normalize_tags
    result = normalize_tags('Python, ML ,python,, Data ')
    assert result == ['python', 'ml', 'data']

def test_empty_string():
    """An empty input string should return an empty list."""
    from solution import normalize_tags
    result = normalize_tags('')
    assert result == []

def test_single_tag():
    """A single tag with surrounding whitespace should be stripped and lowercased."""
    from solution import normalize_tags
    result = normalize_tags('  Hello World  ')
    assert result == ['hello world']

def test_duplicate_preserves_first_order():
    """When the same tag appears multiple times in different cases, only the first occurrence (normalized) is kept, preserving original order."""
    from solution import normalize_tags
    result = normalize_tags('Data, data, DATA, ml, ML, python')
    assert result == ['data', 'ml', 'python']

def test_return_type_is_list():
    """The function must always return a list type."""
    from solution import normalize_tags
    for inp in ['a,b,c', '', '  ', 'single']:
        result = normalize_tags(inp)
        assert isinstance(result, list), f'Expected list, got {type(result).__name__} for input {inp!r}'

def test_only_whitespace_and_empty_tags():
    """Input containing only whitespace-only segments and empty segments should yield []."""
    from solution import normalize_tags
    result = normalize_tags('  ,  ,,   ,')
    assert result == []
