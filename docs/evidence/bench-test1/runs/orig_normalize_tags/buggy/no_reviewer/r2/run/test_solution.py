# Accepted by submit_tests; explanations in testgen_report.json.

def test_p2_empty_input():
    from solution import normalize_tags
    result = normalize_tags('')
    assert result == []

def test_p3_whitespace_only_tags():
    from solution import normalize_tags
    result = normalize_tags('   , , ,  ')
    assert result == []

def test_p6_leading_trailing_consecutive_commas():
    from solution import normalize_tags
    result = normalize_tags(',tag1,,tag2,')
    assert result == ['tag1', 'tag2']

def test_p4_case_insensitive_duplicates():
    from solution import normalize_tags
    result = normalize_tags('Apple, BANANA, apple, Cherry, banana')
    assert result == ['apple', 'banana', 'cherry']

def test_p7_single_tag():
    from solution import normalize_tags
    result = normalize_tags('SingleTag')
    assert result == ['singletag']
