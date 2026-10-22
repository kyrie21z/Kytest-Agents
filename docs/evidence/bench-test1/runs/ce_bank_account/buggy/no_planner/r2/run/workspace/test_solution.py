# Accepted by submit_tests; explanations in testgen_report.json.

from solution import BankAccount as _case0_BankAccount

def test_deposit_positive():
    """Test that depositing a positive amount increases balance correctly."""
    acct = _case0_BankAccount(100)
    result = acct.deposit(50)
    assert result == 150
    assert acct.view_balance() == 150

from solution import BankAccount as _case1_BankAccount
import pytest as _case1_pytest

def test_deposit_negative_raises():
    """Test that depositing a negative amount raises ValueError."""
    acct = _case1_BankAccount(100)
    with _case1_pytest.raises(ValueError, match='Invalid amount'):
        acct.deposit(-10)
    assert acct.view_balance() == 100

from solution import BankAccount as _case2_BankAccount

def test_deposit_zero():
    """Test that depositing zero is valid and returns unchanged balance."""
    acct = _case2_BankAccount(100)
    result = acct.deposit(0)
    assert result == 100
    assert isinstance(result, int)

from solution import BankAccount as _case3_BankAccount
import pytest as _case3_pytest

def test_withdraw_exact_fails():
    """Test that withdrawing exactly the balance raises 'Insufficient balance.' per the >= check."""
    acct = _case3_BankAccount(100)
    with _case3_pytest.raises(ValueError, match='Insufficient balance.'):
        acct.withdraw(100)
    assert acct.view_balance() == 100

from solution import BankAccount as _case4_BankAccount

def test_transfer_basic():
    """Test basic transfer between two accounts."""
    acct1 = _case4_BankAccount()
    acct2 = _case4_BankAccount()
    acct1.deposit(1000)
    acct1.transfer(acct2, 300)
    assert acct1.view_balance() == 700
    assert acct2.view_balance() == 300

from solution import BankAccount as _case5_BankAccount
import pytest as _case5_pytest

def test_withdraw_insufficient_raises():
    """Test that withdrawing more than balance raises ValueError."""
    acct = _case5_BankAccount(50)
    with _case5_pytest.raises(ValueError, match='Insufficient balance.'):
        acct.withdraw(100)
    assert acct.view_balance() == 50
