# Accepted by submit_tests; explanations in testgen_report.json.

# Accepted by submit_tests; explanations in testgen_report.json.

from solution import BankAccount as _case0_BankAccount

def test_deposit_basic():
    """Test that depositing a positive amount increases balance correctly."""
    account = _case0_BankAccount(100)
    result = account.deposit(50)
    assert result == 150
    assert account.view_balance() == 150

from solution import BankAccount as _case1_BankAccount
import pytest as _case1_pytest

def test_deposit_negative_raises():
    """Test that depositing a negative amount raises ValueError."""
    account = _case1_BankAccount(100)
    with _case1_pytest.raises(ValueError, match='Invalid amount'):
        account.deposit(-10)
    assert account.view_balance() == 100

from solution import BankAccount as _case2_BankAccount

def test_withdraw_basic():
    """Test that withdrawing an amount less than or equal to balance works correctly."""
    account = _case2_BankAccount(200)
    result = account.withdraw(80)
    assert result == 120
    assert account.view_balance() == 120

from solution import BankAccount as _case3_BankAccount
import pytest as _case3_pytest

def test_withdraw_insufficient_raises():
    """Test that withdrawing more than the balance raises ValueError."""
    account = _case3_BankAccount(50)
    with _case3_pytest.raises(ValueError, match='Insufficient balance.'):
        account.withdraw(100)
    assert account.view_balance() == 50

from solution import BankAccount as _case4_BankAccount
import pytest as _case4_pytest

def test_withdraw_negative_raises():
    """Test that withdrawing a negative amount raises ValueError."""
    account = _case4_BankAccount(100)
    with _case4_pytest.raises(ValueError, match='Invalid amount'):
        account.withdraw(-50)
    assert account.view_balance() == 100

from solution import BankAccount as _case5_BankAccount

def test_transfer_between_accounts():
    """Test transferring money from one account to another."""
    account1 = _case5_BankAccount(500)
    account2 = _case5_BankAccount(200)
    result = account1.transfer(account2, 150)
    assert account1.view_balance() == 350
    assert account2.view_balance() == 350
    assert result is None


from solution import BankAccount as _new08b319630__t_BankAccount

def test_init_default_balance():
    """Test that __init__ defaults balance to 0 when called without arguments."""
    account = _new08b319630__t_BankAccount()
    assert account.balance == 0
    assert isinstance(account.balance, int)

from solution import BankAccount as _new08b319631__t_BankAccount

def test_view_balance_returns_current():
    """Test that view_balance returns the current account balance accurately."""
    account = _new08b319631__t_BankAccount(500)
    assert account.view_balance() == 500
    account.deposit(100)
    assert account.view_balance() == 600
    account.withdraw(200)
    assert account.view_balance() == 400

from solution import BankAccount as _new08b319632__t_BankAccount

def test_deposit_return_value():
    """Test that deposit returns the updated balance as stated in the docstring."""
    account = _new08b319632__t_BankAccount(0)
    result = account.deposit(100)
    assert result == 100
    assert result is account.balance
    result2 = account.deposit(50)
    assert result2 == 150
    assert result2 is account.balance

from solution import BankAccount as _new08b319633__t_BankAccount

def test_withdraw_return_value():
    """Test that withdraw returns the updated balance as stated in the docstring."""
    account = _new08b319633__t_BankAccount(300)
    result = account.withdraw(100)
    assert result == 200
    assert result is account.balance
    result2 = account.withdraw(50)
    assert result2 == 150
    assert result2 is account.balance

from solution import BankAccount as _new08b319634__t_BankAccount

def test_deposit_zero_amount():
    """Test that depositing zero is allowed and returns unchanged balance."""
    account = _new08b319634__t_BankAccount(100)
    result = account.deposit(0)
    assert result == 100
    assert account.balance == 100

from solution import BankAccount as _new08b319635__t_BankAccount

def test_withdraw_exact_balance():
    """Test that withdrawing exactly the full balance is allowed and results in zero."""
    account = _new08b319635__t_BankAccount(200)
    result = account.withdraw(200)
    assert result == 0
    assert account.balance == 0
