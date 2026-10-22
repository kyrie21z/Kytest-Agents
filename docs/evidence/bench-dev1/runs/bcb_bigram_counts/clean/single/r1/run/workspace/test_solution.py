# Accepted by submit_tests; explanations in testgen_report.json.

"""Test duplicate bigram counting."""
from solution import bigram_counts as _case0_bigram_counts

def test_repeated_bigrams():
    result = _case0_bigram_counts('banana')
    assert isinstance(result, dict)
    assert result['ba'] == 1
    assert result['an'] == 2
    assert result['na'] == 2
    assert result['bb'] == 0
    assert result['zz'] == 0

"""Test that empty input yields all-zero dict."""
from solution import bigram_counts as _case1_bigram_counts

def test_empty_string():
    result = _case1_bigram_counts('')
    assert isinstance(result, dict)
    assert len(result) == 26 * 26
    assert result['ab'] == 0
    assert result['zz'] == 0
    assert result['aa'] == 0

"""Test single-character input yields all zeros."""
from solution import bigram_counts as _case2_bigram_counts

def test_single_character():
    result = _case2_bigram_counts('a')
    assert isinstance(result, dict)
    assert len(result) == 26 * 26
    assert result['aa'] == 0
    assert result['ab'] == 0
    assert result['zz'] == 0

"""Test basic counting on a short word."""
from solution import bigram_counts as _case3_bigram_counts

def test_simple_three_letter_word():
    result = _case3_bigram_counts('abc')
    assert isinstance(result, dict)
    assert len(result) == 26 * 26
    assert result['ab'] == 1
    assert result['bc'] == 1
    assert result['ac'] == 0
    assert result['ba'] == 0

"""Test double-letter bigrams like 'oo', 'kk'."""
from solution import bigram_counts as _case4_bigram_counts

def test_double_letter_bigram():
    result = _case4_bigram_counts('bookkeeper')
    assert isinstance(result, dict)
    assert len(result) == 26 * 26
    assert result['oo'] == 1
    assert result['kk'] == 1
    assert result['ee'] == 1
    assert result['bo'] == 1
    assert result['er'] == 1
    assert result['aa'] == 0

"""Test non-alpha characters produce no matching alpha bigrams."""
from solution import bigram_counts as _case5_bigram_counts

def test_non_alpha_characters():
    result = _case5_bigram_counts('a1b2c')
    assert isinstance(result, dict)
    assert len(result) == 26 * 26
    assert result['ab'] == 0
    assert result['bc'] == 0
    assert result['aa'] == 0
    assert result['zz'] == 0
