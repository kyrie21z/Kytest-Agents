# Accepted by submit_tests; explanations in testgen_report.json.

def test_empty_string():
    """Empty input string should yield an empty list."""
    from solution import normalize_tags
    result = normalize_tags('')
    assert result == []
    assert isinstance(result, list)

def test_all_whitespace_tags():
    """Input with only whitespace-separated commas should yield empty list."""
    from solution import normalize_tags
    result = normalize_tags('  ,  ,   ')
    assert result == []
    assert isinstance(result, list)

def test_single_tag():
    """A single tag with surrounding whitespace should be stripped and lowered."""
    from solution import normalize_tags
    result = normalize_tags('  HelloWorld  ')
    assert result == ['helloworld']
    assert isinstance(result, list)

def test_duplicate_case_insensitive():
    """Duplicate tags differing only in case should be deduplicated, keeping the first."""
    from solution import normalize_tags
    result = normalize_tags('Python, python, PYTHON, pyThon')
    assert result == ['python']
    assert len(result) == 1

def test_basic_mixed_case_whitespace():
    """Test basic normalization: strip, lowercase, deduplicate, drop empties."""
    from solution import normalize_tags
    result = normalize_tags(' Python, ML ,python,, Data ')
    assert result == ['data', 'ml', 'python']
    assert isinstance(result, list)

def test_alphabetical_sorting():
    """Verify that the result is sorted alphabetically, as the implementation uses sorted(set(seen))."""
    from solution import normalize_tags
    result = normalize_tags('zebra,apple,mango,berry')
    assert result == ['apple', 'berry', 'mango', 'zebra']
    assert result == sorted(result)
