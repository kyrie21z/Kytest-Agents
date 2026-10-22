# Accepted by submit_tests; explanations in testgen_report.json.

from solution import bigram_counts as _case0_bigram_counts

def test_basic_bigram_counting():
    result = _case0_bigram_counts('abcdef')
    assert isinstance(result, dict)
    assert result['ab'] == 1
    assert result['bc'] == 1
    assert result['cd'] == 1
    assert result['de'] == 1
    assert result['ef'] == 1
    assert result['zz'] == 0
    assert result['xy'] == 0
    assert result['aa'] == 0
