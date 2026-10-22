# Accepted by submit_tests; explanations in testgen_report.json.

"""Test that BankAccount() initializes with balance 0."""
from solution import BankAccount as _case0_BankAccount

def test_default_balance_is_zero():
    """Contract: default value of balance is 0.

    Expected: creating an account without arguments yields balance==0.
    Fault hypothesis: if __init__ silently used some non-zero default,
    view_balance would reveal it.
    """
    acct = _case0_BankAccount()
    assert acct.view_balance() == 0

"""Test that deposit increases balance correctly and returns new balance."""
from solution import BankAccount as _case1_BankAccount

def test_deposit_positive_amount():
    """Contract: deposit(amount > 0) increases balance by amount and returns new balance.

    Input domain: amount = 100, starting balance = 0.
    Expected: returns 100, balance becomes 100.
    Fault hypothesis: if deposit did not update self.balance, view_balance
    would still show 0.
    """
    acct = _case1_BankAccount()
    result = acct.deposit(100)
    assert result == 100
    assert acct.view_balance() == 100

"""Test that deposit(negative) raises ValueError with correct message."""
from solution import BankAccount as _case2_BankAccount
import pytest as _case2_pytest

def test_deposit_negative_raises():
    """Contract: deposit(negative) raises ValueError('Invalid amount').

    Input domain: amount = -10.
    Expected: ValueError raised with message 'Invalid amount'.
    Fault hypothesis: if the sign check was reversed or missing,
    negative deposits would silently succeed.
    """
    acct = _case2_BankAccount(100)
    with _case2_pytest.raises(ValueError, match='Invalid amount'):
        acct.deposit(-10)
    assert acct.view_balance() == 100

"""Test that withdraw(amount == balance) raises Insufficient balance error."""
from solution import BankAccount as _case3_BankAccount
import pytest as _case3_pytest

def test_withdraw_exactly_equal_fails():
    """Contract: withdraw(amount >= balance) raises ValueError('Insufficient balance.')

    The contract says 'amount >= self.balance' triggers the error, so
    withdrawing the entire balance is NOT allowed.

    Input domain: balance=100, amount=100.
    Expected: ValueError raised.
    Fault hypothesis: if the check used '>' instead of '>=', this would
    incorrectly allow withdrawing the full balance.
    """
    acct = _case3_BankAccount(100)
    with _case3_pytest.raises(ValueError, match='Insufficient balance.'):
        acct.withdraw(100)
    assert acct.view_balance() == 100

"""Test that transfer moves money from sender to receiver correctly."""
from solution import BankAccount as _case4_BankAccount

def test_transfer_between_accounts():
    """Contract: transfer(amount) withdraws from self and deposits to other.

    From docstring example: deposit 1000, transfer 300.
    Expected: sender balance = 700, receiver balance = 300.
    Fault hypothesis: if transfer didn't actually move money (e.g., forgot
    to call withdraw or deposit), balances would be wrong.
    """
    acct1 = _case4_BankAccount()
    acct2 = _case4_BankAccount()
    acct1.deposit(1000)
    acct1.transfer(acct2, 300)
    assert acct1.view_balance() == 700
    assert acct2.view_balance() == 300

"""Test that transfer conserves total money across both accounts."""
from solution import BankAccount as _case5_BankAccount

def test_transfer_preserves_total():
    """Contract: transfer conserves total money across accounts.

    Input domain: two accounts with balances 500 and 200, transfer 150.
    Expected: sum of balances before = 700, sum after = 700.
    Fault hypothesis: if money was created or destroyed during transfer.
    """
    acct1 = _case5_BankAccount(500)
    acct2 = _case5_BankAccount(200)
    total_before = acct1.view_balance() + acct2.view_balance()
    acct1.transfer(acct2, 150)
    total_after = acct1.view_balance() + acct2.view_balance()
    assert total_before == total_after == 700
