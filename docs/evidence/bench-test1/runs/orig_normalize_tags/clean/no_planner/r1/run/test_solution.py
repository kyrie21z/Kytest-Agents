# Accepted by submit_tests; explanations in testgen_report.json.

def test_basic_doctest():
    from solution import normalize_tags
    result = normalize_tags(' Python, ML ,python,, Data ')
    assert result == ['python', 'ml', 'data']

def test_empty_string():
    from solution import normalize_tags
    result = normalize_tags('')
    assert result == []
    assert isinstance(result, list)

def test_whitespace_only():
    from solution import normalize_tags
    result = normalize_tags('   ,  ,   ')
    assert result == []
    assert isinstance(result, list)

def test_duplicate_dedup_order():
    from solution import normalize_tags
    result = normalize_tags('B, a, B, A, c, b')
    assert result == ['b', 'a', 'c']
    assert isinstance(result, list)
    assert len(result) == 3

def test_internal_spaces_preserved():
    from solution import normalize_tags
    result = normalize_tags('hello world, foo bar')
    assert result == ['hello world', 'foo bar']
    assert isinstance(result, list)
    assert len(result) == 2

def test_leading_trailing_commas():
    from solution import normalize_tags
    result = normalize_tags(',tag1,,tag2,')
    assert result == ['tag1', 'tag2']
    assert isinstance(result, list)
    assert len(result) == 2
