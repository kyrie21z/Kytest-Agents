# Accepted by submit_tests; explanations in testgen_report.json.

# Accepted by submit_tests; explanations in testgen_report.json.

from solution import BankAccount as _case0_BankAccount

def test_deposit_basic():
    """
    Contract quote: 'Deposits a certain amount into the account, increasing the account balance, return the current account balance.'
    Input domain: A freshly created account (default balance 0), deposit 100.
    Expected result: balance becomes 100, and deposit() returns 100.
    Fault hypothesis: deposit does not update self.balance or returns wrong value.
    """
    acc = _case0_BankAccount()
    result = acc.deposit(100)
    assert acc.view_balance() == 100
    assert result == 100

from solution import BankAccount as _case1_BankAccount

def test_deposit_multiple():
    """
    Contract quote: 'Deposits a certain amount into the account, increasing the account balance, return the current account balance.'
    Input domain: Account starting at 0, deposit 50 then deposit 75.
    Expected result: balance is 125 after two deposits; each call returns the running total.
    Fault hypothesis: deposit resets balance instead of accumulating.
    """
    acc = _case1_BankAccount()
    r1 = acc.deposit(50)
    assert r1 == 50
    r2 = acc.deposit(75)
    assert r2 == 125
    assert acc.view_balance() == 125

from solution import BankAccount as _case2_BankAccount
import pytest as _case2_pytest

def test_deposit_negative_raises():
    """
    Contract quote: 'If amount is negative, raise a ValueError("Invalid amount").'
    Input domain: Any account, deposit(-10).
    Expected result: ValueError is raised with message containing 'Invalid amount'.
    Fault hypothesis: negative deposit silently accepted or raises wrong exception type.
    """
    acc = _case2_BankAccount()
    with _case2_pytest.raises(ValueError, match='Invalid amount'):
        acc.deposit(-10)

from solution import BankAccount as _case3_BankAccount

def test_withdraw_basic():
    """
    Contract quote: 'Withdraws a certain amount from the account, decreasing the account balance, return the current account balance.'
    Input domain: Account with balance 200, withdraw 80.
    Expected result: balance becomes 120, withdraw returns 120.
    Fault hypothesis: withdraw does not decrease balance or returns stale value.
    """
    acc = _case3_BankAccount(200)
    result = acc.withdraw(80)
    assert acc.view_balance() == 120
    assert result == 120

from solution import BankAccount as _case4_BankAccount
import pytest as _case4_pytest

def test_withdraw_insufficient_raises():
    """
    Contract quote: 'If the withdrawal amount is greater than the account balance, raise a ValueError("Insufficient balance.").'
    Input domain: Account with balance 50, attempt to withdraw 100.
    Expected result: ValueError is raised with message containing 'Insufficient balance.'.
    Fault hypothesis: insufficient withdrawal is silently allowed or raises wrong error.
    """
    acc = _case4_BankAccount(50)
    with _case4_pytest.raises(ValueError, match='Insufficient balance.'):
        acc.withdraw(100)

from solution import BankAccount as _case5_BankAccount

def test_transfer_balances():
    """
    Contract quote: 'Transfers a certain amount from the current account to another account.'
    Docstring example: 'account1.deposit(1000); account1.transfer(account2, 300) => account1.balance=700, account2.balance=300'
    Input domain: Two accounts; first has 1000, transfer 300 to second (initially 0).
    Expected result: sender balance drops by 300, receiver balance increases by 300.
    Fault hypothesis: transfer only debits sender but does not credit receiver.
    """
    acc1 = _case5_BankAccount(1000)
    acc2 = _case5_BankAccount(0)
    acc1.transfer(acc2, 300)
    assert acc1.view_balance() == 700
    assert acc2.view_balance() == 300


from solution import BankAccount as _new9a2c7e7e0_BankAccount

def test_view_balance_returns_current():
    """
    Contract quote: 'Return the account balance.'
    Input domain: An account initialized with balance 500.
    Expected result: view_balance() returns 500 without modifying the balance.
    Fault hypothesis: view_balance modifies the balance or returns an incorrect value.
    """
    acc = _new9a2c7e7e0_BankAccount(500)
    result = acc.view_balance()
    assert result == 500
    assert acc.view_balance() == 500

import pytest as _new9a2c7e7e1_pytest
from solution import BankAccount as _new9a2c7e7e1_BankAccount

def test_withdraw_negative_raises():
    """
    Contract quote: 'If amount is negative, raise a ValueError("Invalid amount").'
    Input domain: Any account, withdraw(-50).
    Expected result: ValueError is raised with message containing 'Invalid amount'.
    Fault hypothesis: negative withdrawal is silently accepted or raises wrong exception.
    """
    acc = _new9a2c7e7e1_BankAccount(100)
    with _new9a2c7e7e1_pytest.raises(ValueError, match='Invalid amount'):
        acc.withdraw(-50)
