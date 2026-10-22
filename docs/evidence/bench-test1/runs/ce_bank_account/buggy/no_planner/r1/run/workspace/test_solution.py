# Accepted by submit_tests; explanations in testgen_report.json.

# Accepted by submit_tests; explanations in testgen_report.json.

from solution import BankAccount as _case0_BankAccount

def test_deposit_positive_amount():
    """Test that depositing a positive amount increases balance and returns new balance."""
    account = _case0_BankAccount()
    result = account.deposit(100)
    assert result == 100
    assert account.view_balance() == 100

from solution import BankAccount as _case1_BankAccount

def test_withdraw_within_balance():
    """Test withdrawing less than balance correctly reduces balance and returns new balance."""
    account = _case1_BankAccount(500)
    result = account.withdraw(200)
    assert result == 300
    assert account.view_balance() == 300

from solution import BankAccount as _case2_BankAccount

def test_transfer_between_accounts():
    """Test transferring money between two accounts changes both balances correctly."""
    account1 = _case2_BankAccount()
    account2 = _case2_BankAccount()
    account1.deposit(1000)
    account1.transfer(account2, 300)
    assert account1.view_balance() == 700
    assert account2.view_balance() == 300

from solution import BankAccount as _case3_BankAccount
import pytest as _case3_pytest

def test_deposit_negative_raises():
    """Test that depositing a negative amount raises ValueError and balance stays unchanged."""
    account = _case3_BankAccount(50)
    with _case3_pytest.raises(ValueError):
        account.deposit(-30)
    assert account.view_balance() == 50

from solution import BankAccount as _case4_BankAccount
import pytest as _case4_pytest

def test_withdraw_equal_to_balance_boundary():
    """Test withdrawing exactly the balance raises ValueError and balance stays unchanged."""
    account = _case4_BankAccount(100)
    with _case4_pytest.raises(ValueError):
        account.withdraw(100)
    assert account.view_balance() == 100

from solution import BankAccount as _case5_BankAccount
import pytest as _case5_pytest

def test_withdraw_exceeds_balance():
    """Test withdrawing more than balance raises ValueError and balance stays unchanged."""
    account = _case5_BankAccount(100)
    with _case5_pytest.raises(ValueError):
        account.withdraw(200)
    assert account.view_balance() == 100


from solution import BankAccount as _new5f7136e80_BankAccount

def test_deposit_strong_assertion():
    """Test depositing a positive amount with strong balance assertion."""
    account = _new5f7136e80_BankAccount(0)
    initial = account.balance
    amount = 100
    result = account.deposit(amount)
    assert account.balance == initial + amount
    assert result == initial + amount
    assert isinstance(result, int)

from solution import BankAccount as _new5f7136e81_BankAccount

def test_withdraw_return_value_assertion():
    """Test withdraw returns the correct remaining balance."""
    account = _new5f7136e81_BankAccount(500)
    initial = account.balance
    amount = 200
    result = account.withdraw(amount)
    assert account.balance == initial - amount
    assert result == initial - amount
    assert isinstance(result, int)

from solution import BankAccount as _new5f7136e82_BankAccount

def test_view_balance_returns_correct_value():
    """Test that view_balance returns the current balance without side effects."""
    account = _new5f7136e82_BankAccount(750)
    balance_before = account.balance
    result = account.view_balance()
    assert result == balance_before
    assert account.balance == balance_before
    assert isinstance(result, int)

from solution import BankAccount as _new5f7136e83_BankAccount

def test_init_nonzero_initial_balance():
    """Test __init__ correctly sets balance when a non-zero initial value is provided."""
    account = _new5f7136e83_BankAccount(250)
    assert account.balance == 250
    assert isinstance(account.balance, int)
