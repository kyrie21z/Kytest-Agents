"""Hidden checks added by Kytest-Agents for docstring promises the upstream tests skip.

"The dictionary values represent the frequency of these two-letter combinations in the given word."
"""
from solution import bigram_counts


def test_overlapping_occurrences_are_all_counted():
    assert bigram_counts("aaa")["aa"] == 2
    assert bigram_counts("abab")["ab"] == 2
    assert bigram_counts("abab")["ba"] == 1


def test_every_two_letter_combination_is_a_key():
    assert len(bigram_counts("")) == 26 * 26
