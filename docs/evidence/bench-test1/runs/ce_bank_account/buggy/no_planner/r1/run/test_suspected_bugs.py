# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

from solution import BankAccount
import pytest

def test_withdraw_equal_to_balance_succeeds():
    """Test withdrawing exactly the balance succeeds per spec ('greater than' triggers error)."""
    account = BankAccount(100)
    initial = account.balance
    amount = 100
    result = account.withdraw(amount)
    assert account.balance == initial - amount
    assert result == initial - amount
    assert account.balance == 0
