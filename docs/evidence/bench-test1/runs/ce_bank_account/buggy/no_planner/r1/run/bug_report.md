# Suspected implementation bugs

## test_withdraw_equal_to_balance_succeeds

- Reviewer: The specification explicitly states that a ValueError is raised only if the withdrawal amount is 'greater than' the account balance. Equality should be permitted and succeed. The implementation incorrectly uses `>=`, causing it to reject valid withdrawals of the exact balance. The test correctly follows the specification.

```
test_withdraw_equal_to_balance_succeeds ____________________
test_solution.py:9: in test_withdraw_equal_to_balance_succeeds
    result = account.withdraw(amount)
             ^^^^^^^^^^^^^^^^^^^^^^^^
_testgen_contracts.py:353: in counted
    return method(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^
solution.py:33: in withdraw
    raise ValueError('Insufficient balance.')
E   ValueError: Insufficient balance.
=========================== short test summary info ============================
FAILED test_solution.py::test_withdraw_equal_to_balance_succeeds - ValueError...
1 failed in 0.02s
```
