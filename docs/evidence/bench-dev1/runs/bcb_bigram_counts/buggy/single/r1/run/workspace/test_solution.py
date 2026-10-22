# Accepted by submit_tests; explanations in testgen_report.json.

def test_repeated_bigrams():
    from solution import bigram_counts
    result = bigram_counts('aaaa')
    assert result['aa'] == 3
    assert result['ab'] == 0
    assert result['ba'] == 0
    assert result['zz'] == 0
    assert len(result) == 676

def test_basics_abcdef():
    from solution import bigram_counts
    result = bigram_counts('abcdef')
    assert len(result) == 676
    assert result['ba'] == 1
    assert result['cb'] == 1
    assert result['dc'] == 1
    assert result['ed'] == 1
    assert result['fe'] == 1
    assert result['ab'] == 0
    assert result['bc'] == 0
    assert result['cd'] == 0
    assert result['de'] == 0
    assert result['ef'] == 0
    assert result['ac'] == 0
    assert result['za'] == 0

def test_double_letter_bigrams_included():
    from solution import bigram_counts
    result = bigram_counts('aab')
    assert result['aa'] == 1
    assert result['ba'] == 1
    assert 'bb' in result
    assert 'cc' in result
    assert 'zz' in result
    assert result['bb'] == 0
    assert result['cc'] == 0

def test_empty_string():
    from solution import bigram_counts
    result = bigram_counts('')
    assert len(result) == 676
    assert result['ab'] == 0
    assert result['ba'] == 0
    assert result['aa'] == 0
    assert result['zz'] == 0
    assert result['bc'] == 0
    assert result['zy'] == 0

def test_single_char():
    from solution import bigram_counts
    result = bigram_counts('a')
    assert len(result) == 676
    assert result['aa'] == 0
    assert result['ab'] == 0
    assert result['ba'] == 0
    assert result['zz'] == 0
    assert result['xy'] == 0
