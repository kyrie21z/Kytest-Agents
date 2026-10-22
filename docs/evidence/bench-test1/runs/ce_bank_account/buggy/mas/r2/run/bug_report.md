# Suspected implementation bugs

## test_p8_withdraw_exact_balance

- Plan P8: Withdraw exact balance amount — input `BankAccount(75).withdraw(75)`, expected `Returns 0; balance becomes 0`
- Reviewer: The specification explicitly states that a ValueError should be raised only when the withdrawal amount is 'greater than' the account balance. The test correctly expects the operation to succeed when amount equals balance, returning 0. The implementation incorrectly uses '>=' in its guard clause, raising ValueError on equality, which directly contradicts the specification.

```
=
________________________ test_p8_withdraw_exact_balance ________________________
test_solution.py:13: in test_p8_withdraw_exact_balance
    result = acct.withdraw(75)
             ^^^^^^^^^^^^^^^^^
_testgen_contracts.py:353: in counted
    return method(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^
solution.py:33: in withdraw
    raise ValueError('Insufficient balance.')
E   ValueError: Insufficient balance.
=========================== short test summary info ============================
FAILED test_solution.py::test_p8_withdraw_exact_balance - ValueError: Insuffi...
1 failed in 0.02s
```
