# Suspected implementation bugs

## test_p1_standard_bigrams

- Plan P1: Standard word with distinct adjacent bigrams — input `'abcdef'`, expected `Dictionary contains all 676 lowercase bigram permutations. 'ab': 1, 'bc': 1, 'cd': 1, 'de': 1, 'ef': 1, and all other keys map to 0.`
- Reviewer: The test correctly expects standard forward bigrams (e.g., 'ab': 1) as specified and shown in the docstring example. The implementation violates this by using zip(word[1:], word), which reverses the character order.

```
F                                                                        [100%]
=================================== FAILURES ===================================
___________________________ test_p1_standard_bigrams ___________________________
test_solution.py:8: in test_p1_standard_bigrams
    assert result[bg] == 1, f"{bg!r} should have count 1"
E   AssertionError: 'ab' should have count 1
E   assert 0 == 1
=========================== short test summary info ============================
FAILED test_solution.py::test_p1_standard_bigrams - AssertionError: 'ab' shou...
1 failed in 0.01s
```

## test_p4_overlapping_repeated

- Plan P4: Overlapping and repeated bigrams — input `'banana'`, expected `'ba': 1, 'an': 2, 'na': 1, all other keys 0.`
- Reviewer: The test correctly expects overlapping bigram counts for 'banana' per standard definition. The implementation's reversed zip order causes the counts to be incorrect.

```
F                                                                        [100%]
=================================== FAILURES ===================================
_________________________ test_p4_overlapping_repeated _________________________
test_solution.py:6: in test_p4_overlapping_repeated
    assert result["ba"] == 1
E   assert 0 == 1
=========================== short test summary info ============================
FAILED test_solution.py::test_p4_overlapping_repeated - assert 0 == 1
1 failed in 0.01s
```

## test_extra_non_symmetric_bigram

- Reviewer: The test correctly verifies forward bigram ordering for 'ab'. The implementation swaps zip arguments, producing 'ba' instead of 'ab', contradicting the specification.

```
[100%]
=================================== FAILURES ===================================
_______________________ test_extra_non_symmetric_bigram ________________________
test_solution.py:8: in test_extra_non_symmetric_bigram
    assert result["ab"] == 1, "Correct implementation should have 'ab': 1"
E   AssertionError: Correct implementation should have 'ab': 1
E   assert 0 == 1
=========================== short test summary info ============================
FAILED test_solution.py::test_extra_non_symmetric_bigram - AssertionError: Co...
1 failed in 0.01s
```
