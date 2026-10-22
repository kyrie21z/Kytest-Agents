# Accepted by submit_tests; explanations in testgen_report.json.

"""Test P1: Deposit a positive amount into a new account."""
from solution import BankAccount as _case0_BankAccount

def test_p1_deposit_positive():
    """P1: Deposit a positive amount into a new account.

    Contract quote:
        'Deposits a certain amount into the account, increasing the
         account balance, return the current account balance.'

    Input domain:
        account = BankAccount(); account.deposit(100)

    Oracle:
        deposit(100) returns 100 and account.balance == 100.

    Fault hypothesis:
        If the method fails to update balance or return the correct value,
        this assertion will catch it.
    """
    account = _case0_BankAccount()
    result = account.deposit(100)
    assert result == 100
    assert account.balance == 100

"""Test P2: Deposit zero amount."""
from solution import BankAccount as _case1_BankAccount

def test_p2_deposit_zero():
    """P2: Deposit zero amount.

    Contract quote:
        'If amount is negative, raise a ValueError("Invalid amount").'
        Zero is not negative; it should be accepted.

    Input domain:
        account = BankAccount(); account.deposit(0)

    Oracle:
        deposit(0) returns 0 and account.balance remains 0.

    Fault hypothesis:
        A buggy implementation might reject zero as if it were negative.
    """
    account = _case1_BankAccount()
    result = account.deposit(0)
    assert result == 0
    assert account.balance == 0

"""Test P3: Withdraw a partial amount from a funded account."""
from solution import BankAccount as _case2_BankAccount

def test_p3_withdraw_partial():
    """P3: Withdraw a partial amount from a funded account.

    Contract quote:
        'Withdraws a certain amount from the account, decreasing the
         account balance, return the current account balance.'

    Input domain:
        account = BankAccount(200); account.withdraw(50)

    Oracle:
        withdraw(50) returns 150 and account.balance == 150.

    Fault hypothesis:
        If the subtraction is wrong or the return value is incorrect,
        this catches it.
    """
    account = _case2_BankAccount(200)
    result = account.withdraw(50)
    assert result == 150
    assert account.balance == 150

"""Test P5: Attempt to deposit a negative amount."""
from solution import BankAccount as _case3_BankAccount
import pytest as _case3_pytest

def test_p5_deposit_negative():
    """P5: Attempt to deposit a negative amount.

    Contract quote:
        'If amount is negative, raise a ValueError("Invalid amount").'

    Input domain:
        account = BankAccount(); account.deposit(-10)

    Oracle:
        Raises ValueError with message "Invalid amount".

    Fault hypothesis:
        If the check for negative amounts is missing or broken,
        the exception will not be raised.
    """
    account = _case3_BankAccount()
    with _case3_pytest.raises(ValueError, match='Invalid amount'):
        account.deposit(-10)

"""Test P6: Attempt to withdraw more than available balance."""
from solution import BankAccount as _case4_BankAccount
import pytest as _case4_pytest

def test_p6_withdraw_excess():
    """P6: Attempt to withdraw more than available balance.

    Contract quote:
        'If the withdrawal amount is greater than the account balance,
         raise a ValueError("Insufficient balance.")'

    Input domain:
        account = BankAccount(50); account.withdraw(100)

    Oracle:
        Raises ValueError with message "Insufficient balance."

    Fault hypothesis:
        If the comparison uses <= instead of >, or omits the check,
        the exception will not be raised.
    """
    account = _case4_BankAccount(50)
    with _case4_pytest.raises(ValueError, match='Insufficient balance.'):
        account.withdraw(100)

"""Test P7: Transfer funds between two accounts."""
from solution import BankAccount as _case5_BankAccount

def test_p7_transfer_funds():
    """P7: Transfer funds between two accounts.

    Contract quote:
        Docstring example: after depositing 1000 and transferring 300,
        account1.balance = 700, account2.balance = 300.

    Input domain:
        a1 = BankAccount(); a1.deposit(1000); a2 = BankAccount();
        a1.transfer(a2, 300)

    Oracle:
        a1.balance == 700 and a2.balance == 300.

    Fault hypothesis:
        If transfer does not properly debit the source or credit the
        destination, balances will be wrong.
    """
    a1 = _case5_BankAccount()
    a1.deposit(1000)
    a2 = _case5_BankAccount()
    a1.transfer(a2, 300)
    assert a1.balance == 700
    assert a2.balance == 300

"""Test P8: Query account balance."""
from solution import BankAccount as _case6_BankAccount

def test_p8_view_balance():
    """P8: Query account balance.

    Contract quote:
        'Return the account balance.'

    Input domain:
        account = BankAccount(500); account.view_balance()

    Oracle:
        view_balance() returns 500.

    Fault hypothesis:
        If view_balance returns a stale or incorrect value, this catches it.
    """
    account = _case6_BankAccount(500)
    assert account.view_balance() == 500

"""Extra: Attempt to withdraw a negative amount."""
from solution import BankAccount as _case7_BankAccount
import pytest as _case7_pytest

def test_extra_withdraw_negative():
    """Extra: Attempt to withdraw a negative amount.

    Contract quote:
        'If amount is negative, raise a ValueError("Invalid amount").'

    Input domain:
        account = BankAccount(100); account.withdraw(-50)

    Oracle:
        Raises ValueError with message "Invalid amount".

    Fault hypothesis:
        If the negative-amount check in withdraw is missing,
        the exception will not be raised.
    """
    account = _case7_BankAccount(100)
    with _case7_pytest.raises(ValueError, match='Invalid amount'):
        account.withdraw(-50)

"""Extra: Default account balance is 0."""
from solution import BankAccount as _case8_BankAccount

def test_extra_default_balance():
    """Extra: Default account balance is 0.

    Contract quote:
        'Initializes a bank account object with an attribute balance,
         default value is 0.'

    Input domain:
        account = BankAccount()

    Oracle:
        account.balance == 0.

    Fault hypothesis:
        If __init__ does not set balance to 0 by default, this fails.
    """
    account = _case8_BankAccount()
    assert account.balance == 0

"""Extra: Multiple deposits accumulate correctly."""
from solution import BankAccount as _case9_BankAccount

def test_extra_multiple_deposits():
    """Extra: Multiple deposits accumulate correctly.

    Contract quote:
        'Deposits a certain amount into the account, increasing the
         account balance, return the current account balance.'

    Input domain:
        account = BankAccount(); account.deposit(50); account.deposit(75)

    Oracle:
        After two deposits, balance == 125.

    Fault hypothesis:
        If deposit overwrites instead of accumulating, balance would be 75.
    """
    account = _case9_BankAccount()
    account.deposit(50)
    account.deposit(75)
    assert account.balance == 125

"""Extra: Withdrawing zero should succeed."""
from solution import BankAccount as _case10_BankAccount

def test_extra_withdraw_zero():
    """Extra: Withdrawing zero should succeed (not negative, not excess).

    Contract quote:
        Only negative amounts and amounts > balance are prohibited.
        Zero is neither negative nor greater than any non-negative balance.

    Input domain:
        account = BankAccount(100); account.withdraw(0)

    Oracle:
        withdraw(0) returns 100 and balance remains 100.

    Fault hypothesis:
        If the implementation treats zero as insufficient or rejects it,
        this catches the bug.
    """
    account = _case10_BankAccount(100)
    result = account.withdraw(0)
    assert result == 100
    assert account.balance == 100
