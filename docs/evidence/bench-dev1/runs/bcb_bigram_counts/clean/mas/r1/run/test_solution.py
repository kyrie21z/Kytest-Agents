# Accepted by submit_tests; explanations in testgen_report.json.

# Accepted by submit_tests; explanations in testgen_report.json.

def test_p8_return_type():
    """Return type verification.

    Spec quote: 'Returns: - dict: A dictionary with keys as two-letter
    alphabet combinations and values as their counts in the word.'
    Input domain: word='test'.
    Expected: the return value is an instance of dict.
    Faulty behavior detected: if the function returns a different type
    (e.g., list, Counter subclass without dict interface).
    """
    from solution import bigram_counts
    result = bigram_counts('test')
    assert isinstance(result, dict)


def test_p1_adjacent_bigrams():
    """Counts adjacent bigrams in a short word.

    Spec quote: 'Create a dictionary containing all possible two-letter combinations of the lowercase English alphabets. The dictionary values represent the frequency of these two-letter combinations in the given word.'
    Input domain: word='abc'.
    Expected: result['ab'] == 1, result['bc'] == 1, all other keys == 0.
    Faulty behavior detected: if adjacent sliding window counting is wrong or bigram extraction misses positions.
    """
    from solution import bigram_counts
    result = bigram_counts('abc')
    assert result['ab'] == 1
    assert result['bc'] == 1
    assert result['ac'] == 0
    assert result['zz'] == 0

def test_p2_overlapping_identical():
    """Handles overlapping identical bigrams.

    Spec quote: 'The dictionary values represent the frequency of these two-letter combinations in the given word.'
    Input domain: word='aaa'.
    Expected: result['aa'] == 2, all other keys == 0.
    Faulty behavior detected: if overlapping bigrams are not counted correctly (e.g., only counting unique positions).
    """
    from solution import bigram_counts
    result = bigram_counts('aaa')
    assert result['aa'] == 2
    assert result['ab'] == 0
    assert result['zz'] == 0

def test_p6_repeated_pattern():
    """Repeated pattern word counts correctly.

    Spec quote: 'The dictionary values represent the frequency of these two-letter combinations in the given word.'
    Input domain: word='abab'.
    Expected: result['ab'] == 2, result['ba'] == 1, others == 0.
    Faulty behavior detected: if repeated patterns are undercounted.
    """
    from solution import bigram_counts
    result = bigram_counts('abab')
    assert result['ab'] == 2
    assert result['ba'] == 1
    assert result['aa'] == 0
    assert result['bb'] == 0
