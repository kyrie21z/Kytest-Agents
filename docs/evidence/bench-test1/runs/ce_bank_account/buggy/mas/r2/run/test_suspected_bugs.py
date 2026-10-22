# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

from solution import BankAccount
import pytest

def test_p8_withdraw_exact_balance():
    """P8 – Withdraw exact balance amount.
    Docstring quote: 'If the withdrawal amount is greater than the account balance, raise a ValueError("Insufficient balance.").'
    Note: 'greater than' means strict inequality. Equal should be allowed.
    Input domain: positive int; amount == balance
    Expected: returns 0; balance becomes 0.
    Faulty behaviour detected: implementation uses >= instead of >, raising ValueError incorrectly when amount equals balance.
    NOTE: This test follows the specification strictly. If it fails on solution.py, the implementation has a bug (uses >= instead of >)."""
    acct = BankAccount(75)
    result = acct.withdraw(75)
    assert result == 0
    assert acct.balance == 0
