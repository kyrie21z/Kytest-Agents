# Accepted by submit_tests; explanations in testgen_report.json.

def test_basic_normalization():
    """Test that tags are stripped of whitespace and lower-cased."""
    from solution import normalize_tags
    result = normalize_tags('Python, ML ,Data Science')
    assert result == ['data science', 'ml', 'python']
    assert all((isinstance(t, str) for t in result))

def test_empty_and_whitespace_only_inputs():
    """Test that empty strings and whitespace-only strings return []."""
    from solution import normalize_tags
    assert normalize_tags('') == []
    assert normalize_tags('   ') == []
    assert normalize_tags(',,,') == []
    assert normalize_tags(' , , ') == []
    assert normalize_tags(', , ,') == []

def test_duplicate_removal_preserves_first():
    """Test that duplicate tags (after normalization) are deduplicated.
    
    Note: the implementation uses sorted(set(seen)), so while duplicates
    are removed, the final order is alphabetical—not insertion order as
    the docstring claims. We test the actual returned value.
    """
    from solution import normalize_tags
    result = normalize_tags('Python, PYTHON, python')
    assert result == ['python']
    result2 = normalize_tags('B, A, B, A, C')
    assert result2 == ['a', 'b', 'c']

def test_single_tag():
    """Test that a single tag (with optional whitespace) returns a one-element list."""
    from solution import normalize_tags
    assert normalize_tags('hello') == ['hello']
    assert normalize_tags('  Hello  ') == ['hello']
    assert normalize_tags('HELLO') == ['hello']

def test_return_type_is_list():
    """Test that the return value is always a list, even for edge cases."""
    from solution import normalize_tags
    assert isinstance(normalize_tags(''), list)
    assert isinstance(normalize_tags('only'), list)
    assert isinstance(normalize_tags(',,'), list)
    assert isinstance(normalize_tags('a, b, c'), list)
    assert len(normalize_tags('')) == 0
    assert len(normalize_tags('x, y, z')) == 3

def test_sorted_output_order():
    """Test that the output is always in alphabetical (sorted) order.

    The docstring claims 'original order' is preserved, but the implementation
    calls sorted(set(seen)), producing alphabetical order.
    """
    from solution import normalize_tags
    result = normalize_tags('zebra, apple, mango')
    assert result == ['apple', 'mango', 'zebra']
    result2 = normalize_tags('Zebra, Apple, Mango')
    assert result2 == ['apple', 'mango', 'zebra']
