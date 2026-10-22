# Accepted by submit_tests; explanations in testgen_report.json.

"""Test P1: Deposit a positive amount into a new account."""
from solution import BankAccount as _case0_BankAccount

def test_p1_deposit_positive():
    account = _case0_BankAccount()
    result = account.deposit(100)
    assert result == 100
    assert account.balance == 100

"""Test P2: Withdraw a partial amount from an account."""
from solution import BankAccount as _case1_BankAccount

def test_p2_withdraw_partial():
    account = _case1_BankAccount(500)
    result = account.withdraw(200)
    assert result == 300
    assert account.balance == 300

"""Test P3: Deposit zero amount — should be accepted without changing balance."""
from solution import BankAccount as _case2_BankAccount

def test_p3_deposit_zero():
    account = _case2_BankAccount(100)
    result = account.deposit(0)
    assert result == 100
    assert account.balance == 100

"""Test P4: Attempt to deposit a negative amount — must raise ValueError."""
from solution import BankAccount as _case3_BankAccount
import pytest as _case3_pytest

def test_p4_deposit_negative():
    account = _case3_BankAccount()
    with _case3_pytest.raises(ValueError, match='Invalid amount'):
        account.deposit(-50)

"""Test P5: Attempt to withdraw more than available balance — must raise ValueError."""
from solution import BankAccount as _case4_BankAccount
import pytest as _case4_pytest

def test_p5_withdraw_exceeds_balance():
    account = _case4_BankAccount(50)
    with _case4_pytest.raises(ValueError, match='Insufficient balance'):
        account.withdraw(100)

"""Test P6: Transfer money between two accounts."""
from solution import BankAccount as _case5_BankAccount

def test_p6_transfer_between_accounts():
    a1 = _case5_BankAccount()
    a1.deposit(1000)
    a2 = _case5_BankAccount()
    a1.transfer(a2, 300)
    assert a1.balance == 700
    assert a2.balance == 300

"""Test P7: View balance without modifying state."""
from solution import BankAccount as _case6_BankAccount

def test_p7_view_balance():
    account = _case6_BankAccount(250)
    result = account.view_balance()
    assert result == 250
    assert account.balance == 250

"""Test P8: Withdraw exact balance amount — should succeed and leave zero."""
from solution import BankAccount as _case7_BankAccount

def test_p8_withdraw_exact_balance():
    account = _case7_BankAccount(100)
    result = account.withdraw(100)
    assert result == 0
    assert account.balance == 0

"""Test P9: Attempt to withdraw a negative amount — must raise ValueError."""
from solution import BankAccount as _case8_BankAccount
import pytest as _case8_pytest

def test_p9_withdraw_negative():
    account = _case8_BankAccount(100)
    with _case8_pytest.raises(ValueError, match='Invalid amount'):
        account.withdraw(-10)

"""Test P10: Initialize account with default parameters — balance should be 0."""
from solution import BankAccount as _case9_BankAccount

def test_p10_default_init():
    account = _case9_BankAccount()
    assert account.balance == 0

"""Extra test: Transfer with insufficient balance — must raise ValueError via withdraw."""
from solution import BankAccount as _case10_BankAccount
import pytest as _case10_pytest

def test_extra_transfer_insufficient():
    a1 = _case10_BankAccount(50)
    a2 = _case10_BankAccount()
    with _case10_pytest.raises(ValueError, match='Insufficient balance'):
        a1.transfer(a2, 100)

"""Extra test: Transfer with negative amount — must raise ValueError via withdraw."""
from solution import BankAccount as _case11_BankAccount
import pytest as _case11_pytest

def test_extra_transfer_negative_amount():
    a1 = _case11_BankAccount(100)
    a2 = _case11_BankAccount()
    with _case11_pytest.raises(ValueError, match='Invalid amount'):
        a1.transfer(a2, -50)

"""Extra test: Multiple sequential operations on one account."""
from solution import BankAccount as _case12_BankAccount

def test_extra_multiple_operations():
    account = _case12_BankAccount()
    assert account.deposit(100) == 100
    assert account.withdraw(30) == 70
    assert account.deposit(50) == 120
    assert account.view_balance() == 120
    assert account.balance == 120
