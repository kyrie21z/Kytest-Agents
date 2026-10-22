# Accepted by submit_tests; explanations in testgen_report.json.

from solution import bigram_counts as _case0_bigram_counts

def test_sum_equals_length_minus_one():
    """For any non-empty word, the sum of all bigram counts must equal len(word)-1,
    since each position pair contributes exactly one bigram."""
    for word in ['hello', 'python', 'aabba', 'xyzzy']:
        result = _case0_bigram_counts(word)
        total = sum(result.values())
        assert total == len(word) - 1, f"For word '{word}' (len={len(word)}), expected sum={len(word) - 1}, got {total}"

from solution import bigram_counts as _case1_bigram_counts

def test_empty_string_specific_key():
    """An empty string has no bigrams; every key maps to 0.
    Check a few specific keys to confirm."""
    result = _case1_bigram_counts('')
    assert isinstance(result, dict)
    assert len(result) == 676
    assert result['ab'] == 0
    assert result['zz'] == 0
    assert result['aa'] == 0

from solution import bigram_counts as _case2_bigram_counts

def test_single_char_specific_key():
    """A single-character word has no bigrams; specific keys must be 0."""
    result = _case2_bigram_counts('x')
    assert isinstance(result, dict)
    assert len(result) == 676
    assert result['xx'] == 0
    assert result['xa'] == 0
    assert result['ax'] == 0

from solution import bigram_counts as _case3_bigram_counts

def test_two_char_word_bigram_count_fixed():
    """For word 'ab', the only bigram from zip(word[1:], word) is ('b','a') -> 'ba'.
    So 'ba' should have count 1, all others 0."""
    result = _case3_bigram_counts('ab')
    assert isinstance(result, dict)
    assert len(result) == 676
    assert result['ba'] == 1
    assert result['ab'] == 0
    assert sum(result.values()) == 1

from solution import bigram_counts as _case4_bigram_counts

def test_repeated_bigrams_count_correctly_fixed():
    """Word 'aaaa' produces bigrams: zip('aaa','aaaa') = [('a','a'),('a','a'),('a','a')] -> 'aa' x3.
    So 'aa' should have count 3."""
    result = _case4_bigram_counts('aaaa')
    assert result['aa'] == 3
    assert result['ab'] == 0
    assert result['ba'] == 0
    assert sum(result.values()) == 3
