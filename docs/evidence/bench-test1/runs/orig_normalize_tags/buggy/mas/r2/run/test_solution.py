# Accepted by submit_tests; explanations in testgen_report.json.

def test_p2_empty_string():
    from solution import normalize_tags
    result = normalize_tags('')
    assert result == []

def test_p7_single_tag():
    from solution import normalize_tags
    result = normalize_tags('  hello  ')
    assert result == ['hello']

def test_p8_only_commas():
    from solution import normalize_tags
    result = normalize_tags(',,,,')
    assert result == []

def test_p3_whitespace_only():
    from solution import normalize_tags
    result = normalize_tags('   , ,  ')
    assert result == []

def test_p4_duplicate_casing():
    from solution import normalize_tags
    result = normalize_tags('Apple, apple, APPLE')
    assert result == ['apple']

def test_p6_internal_spaces():
    from solution import normalize_tags
    result = normalize_tags('Data Science, Machine Learning')
    assert result == ['data science', 'machine learning']

def test_p9_mixed_valid_invalid():
    from solution import normalize_tags
    result = normalize_tags('  Tag1 , TAG2 , tag1 ,  ')
    assert result == ['tag1', 'tag2']

def test_extra_single_char_tags():
    from solution import normalize_tags
    result = normalize_tags('a,b,c,a,b')
    assert result == ['a', 'b', 'c']
