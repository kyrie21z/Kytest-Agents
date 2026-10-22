# Suspected implementation bugs

## test_total_price_with_single_item

- Reviewer: The test correctly expects price * quantity (2.5 * 4 = 10.0) per the specification. The implementation incorrectly sums only prices, ignoring quantities.

```
[100%]
=================================== FAILURES ===================================
______________________ test_total_price_with_single_item _______________________
test_solution.py:9: in test_total_price_with_single_item
    assert result == 10.0, f"Expected 10.0 (2.5*4), got {result}"
E   AssertionError: Expected 10.0 (2.5*4), got 2.5
E   assert 2.5 == 10.0
=========================== short test summary info ============================
FAILED test_solution.py::test_total_price_with_single_item - AssertionError: ...
1 failed in 0.01s
```

## test_total_price_empty_cart

- Reviewer: The test correctly expects a float (0.0) for an empty cart as per the method signature and spec. The implementation returns an integer (0) from sum([]).

```
============== FAILURES ===================================
_________________________ test_total_price_empty_cart __________________________
test_solution.py:6: in test_total_price_empty_cart
    assert isinstance(result, float), "total_price should return a float even for empty cart"
E   AssertionError: total_price should return a float even for empty cart
E   assert False
E    +  where False = isinstance(0, float)
=========================== short test summary info ============================
FAILED test_solution.py::test_total_price_empty_cart - AssertionError: total_...
1 failed in 0.01s
```
