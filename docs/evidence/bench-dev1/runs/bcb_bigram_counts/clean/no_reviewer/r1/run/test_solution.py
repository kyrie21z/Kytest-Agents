# Accepted by submit_tests; explanations in testgen_report.json.

def test_p2_overlapping_bigrams():
    """Overlapping bigrams are counted independently."""
    import solution
    result = solution.bigram_counts('ana')
    assert isinstance(result, dict)
    assert result['an'] == 1
    assert result['na'] == 1
    assert result['aa'] == 0
    assert result['nn'] == 0
