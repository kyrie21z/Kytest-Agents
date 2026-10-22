# Suspected implementation bugs

## test_p4_withdraw_exact_balance

- Plan P4: Withdrawing exactly the current balance succeeds and zeroes it — input `BankAccount(balance=100).withdraw(100)`, expected `returns 0, balance becomes 0`
- Reviewer: The specification explicitly states that a ValueError is raised only if the withdrawal amount is 'greater than' the balance, implying that withdrawing exactly the balance is permitted. The test correctly expects success for an exact-balance withdrawal, but the implementation incorrectly rejects it using `amount >= self.balance`.

```
________________________ test_p4_withdraw_exact_balance ________________________
test_solution.py:13: in test_p4_withdraw_exact_balance
    result = acct.withdraw(100)
             ^^^^^^^^^^^^^^^^^^
_testgen_contracts.py:353: in counted
    return method(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^
solution.py:33: in withdraw
    raise ValueError('Insufficient balance.')
E   ValueError: Insufficient balance.
=========================== short test summary info ============================
FAILED test_solution.py::test_p4_withdraw_exact_balance - ValueError: Insuffi...
1 failed in 0.02s
```
