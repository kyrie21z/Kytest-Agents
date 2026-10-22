# Suspected implementation bugs

## test_p3_total_price_multiple_items

- Plan P3: Calculate total price across multiple items — input `After add_item('a', 1.0, 5) and add_item('b', 2.0, 3), call total_price()`, expected `11.0`
- Reviewer: The test accurately reflects the specification's requirement that total price is the sum of (quantity * price) for all items. The implementation incorrectly sums only the prices, ignoring quantities, which violates the spec.

```
[100%]
=================================== FAILURES ===================================
______________________ test_p3_total_price_multiple_items ______________________
test_solution.py:14: in test_p3_total_price_multiple_items
    assert cart.total_price() == 11.0
E   assert 3.0 == 11.0
E    +  where 3.0 = total_price()
E    +    where total_price = <solution.ShoppingCart object at 0x797d25a76a50>.total_price
=========================== short test summary info ============================
FAILED test_solution.py::test_p3_total_price_multiple_items - assert 3.0 == 11.0
1 failed in 0.01s
```

## test_p8_total_with_zero_qty

- Plan P8: Total price arithmetic consistency with zero-quantity items — input `After add_item('a', 5.0, 0) and add_item('b', 2.0, 3), call total_price()`, expected `6.0`
- Reviewer: The test correctly applies the specification's pricing formula. The implementation fails to multiply item prices by their quantities, leading to an incorrect result. This is an implementation fault.

```
[100%]
=================================== FAILURES ===================================
_________________________ test_p8_total_with_zero_qty __________________________
test_solution.py:14: in test_p8_total_with_zero_qty
    assert cart.total_price() == 6.0
E   assert 7.0 == 6.0
E    +  where 7.0 = total_price()
E    +    where total_price = <solution.ShoppingCart object at 0x79166f8c6a50>.total_price
=========================== short test summary info ============================
FAILED test_solution.py::test_p8_total_with_zero_qty - assert 7.0 == 6.0
1 failed in 0.01s
```
