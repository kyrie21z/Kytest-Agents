# Accepted by submit_tests; explanations in testgen_report.json.

"""Test P2: Single character word."""
from solution import bigram_counts as _case0_bigram_counts

def test_p2_single_char():
    result = _case0_bigram_counts('z')
    assert len(result) == 676
    assert result['aa'] == 0
    assert result['zz'] == 0
    assert result['ab'] == 0
    assert result['za'] == 0
    assert result['az'] == 0

"""Test P3: Empty string input."""
from solution import bigram_counts as _case1_bigram_counts

def test_p3_empty_string():
    result = _case1_bigram_counts('')
    assert len(result) == 676
    assert result['aa'] == 0
    assert result['zz'] == 0
    assert result['ab'] == 0

"""Test P5 variant: total count for 'ab'."""
from solution import bigram_counts as _case2_bigram_counts

def test_p5_total_count_ab():
    result = _case2_bigram_counts('ab')
    assert sum(result.values()) == 1

"""Test P6: Key space completeness."""
from solution import bigram_counts as _case3_bigram_counts

def test_p6_key_space_completeness():
    result = _case3_bigram_counts('a')
    assert len(result) == 676
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    expected_keys = set()
    for i in range(len(alpha)):
        for j in range(len(alpha)):
            expected_keys.add(alpha[i] + alpha[j])
    assert set(result.keys()) == expected_keys

"""Test P7: Return type and value types."""
from solution import bigram_counts as _case4_bigram_counts

def test_p7_return_types():
    result = _case4_bigram_counts('test')
    assert isinstance(result, dict)
    for key in list(result.keys())[:5]:
        val = result[key]
        assert isinstance(val, int), f'value for {key!r} is not int'
    assert isinstance(result.get('te', 0), int)

"""Test P8: Identical character repetition."""
from solution import bigram_counts as _case5_bigram_counts

def test_p8_identical_chars():
    result = _case5_bigram_counts('mmmm')
    assert result['mm'] == 3
    assert result['zz'] == 0
    assert result['xx'] == 0

"""Extra test: Single char does not crash."""
from solution import bigram_counts as _case6_bigram_counts

def test_extra_len_one_no_crash():
    result = _case6_bigram_counts('x')
    assert isinstance(result, dict)
    assert len(result) == 676
    assert result['xx'] == 0
