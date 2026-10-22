# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

"""Test P1: Standard word with distinct adjacent bigrams."""
from solution import bigram_counts

def test_p1_standard_bigrams():
    result = bigram_counts("abcdef")
    assert isinstance(result, dict)
    for bg in ("ab", "bc", "cd", "de", "ef"):
        assert result[bg] == 1, f"{bg!r} should have count 1"
    assert result["zz"] == 0
    assert result["xy"] == 0
    assert result["ba"] == 0, "Reversal bug detected: 'ba' should be 0"

"""Test P4: Overlapping and repeated bigrams."""
from solution import bigram_counts

def test_p4_overlapping_repeated():
    result = bigram_counts("banana")
    assert result["ba"] == 1
    assert result["an"] == 2
    assert result["na"] == 1
    assert result["zz"] == 0
    assert result["xx"] == 0

"""Extra test: Verify reversal bug with non-symmetric bigram."""
from solution import bigram_counts

def test_extra_non_symmetric_bigram():
    result = bigram_counts("ab")
    # With correct implementation: 'ab' -> 1
    # With reversal bug: 'ba' -> 1, 'ab' -> 0
    assert result["ab"] == 1, "Correct implementation should have 'ab': 1"
    assert result["ba"] == 0, "Reversal bug: 'ba' should be 0"
