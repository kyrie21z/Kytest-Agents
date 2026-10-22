# Suspected implementation bugs

## test_order_preserved_non_alpha

- Reviewer: The specification explicitly guarantees that tags retain their original input order after normalization and deduplication. This test correctly expects ['zebra', 'apple'], but the implementation uses sorted(), producing ['apple', 'zebra'], violating the contract.

```
======================
________________________ test_order_preserved_non_alpha ________________________
test_solution.py:13: in test_order_preserved_non_alpha
    assert result == ['zebra', 'apple'], \
E   AssertionError: Expected original-order ['zebra', 'apple'], got ['apple', 'zebra']
E   assert ['apple', 'zebra'] == ['zebra', 'apple']
E     
E     At index 0 diff: 'apple' != 'zebra'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_order_preserved_non_alpha - AssertionError: Exp...
1 failed in 0.01s
```

## test_duplicates_first_wins_order

- Reviewer: The specification requires preserving original order after deduplication. This test correctly expects first-wins order ['cherry', 'apple', 'banana'], but the implementation returns an alphabetically sorted list, violating the spec.

```
es_first_wins_order _______________________
test_solution.py:13: in test_duplicates_first_wins_order
    assert result == ['cherry', 'apple', 'banana'], \
E   AssertionError: Expected first-wins order ['cherry', 'apple', 'banana'], got ['apple', 'banana', 'cherry']
E   assert ['apple', 'banana', 'cherry'] == ['cherry', 'apple', 'banana']
E     
E     At index 0 diff: 'apple' != 'cherry'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_duplicates_first_wins_order - AssertionError: E...
1 failed in 0.01s
```

## test_three_tags_reverse_alpha

- Reviewer: The specification mandates original order preservation. This test correctly expects ['zebra', 'mango', 'apple'], but the implementation sorts the results, contradicting the docstring contract.

```
___ test_three_tags_reverse_alpha _________________________
test_solution.py:12: in test_three_tags_reverse_alpha
    assert result == ['zebra', 'mango', 'apple'], \
E   AssertionError: Expected original-order ['zebra', 'mango', 'apple'], got ['apple', 'mango', 'zebra']
E   assert ['apple', 'mango', 'zebra'] == ['zebra', 'mango', 'apple']
E     
E     At index 0 diff: 'apple' != 'zebra'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED test_solution.py::test_three_tags_reverse_alpha - AssertionError: Expe...
1 failed in 0.01s
```
