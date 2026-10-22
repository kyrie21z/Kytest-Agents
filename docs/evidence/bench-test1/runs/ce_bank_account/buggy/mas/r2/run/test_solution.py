# Accepted by submit_tests; explanations in testgen_report.json.

from solution import BankAccount as _case0_BankAccount

def test_p1_deposit_positive():
    """P1 – Deposit positive amount.
    Docstring quote: 'increasing the account balance, return the current account balance.'
    Input domain: non-negative int; amount > 0
    Expected: returns the new balance (= previous + amount); balance attribute updated.
    Faulty behaviour detected: wrong return value or balance not updated."""
    acct = _case0_BankAccount()
    result = acct.deposit(50)
    assert result == 50
    assert acct.balance == 50

from solution import BankAccount as _case1_BankAccount

def test_p2_withdraw_within_balance():
    """P2 – Withdraw positive amount within balance.
    Docstring quote: 'decreasing the account balance, return the current account balance.'
    Input domain: positive int; amount <= balance
    Expected: returns new balance (= previous - amount); balance attribute updated.
    Faulty behaviour detected: wrong return value or balance not decremented."""
    acct = _case1_BankAccount(100)
    result = acct.withdraw(40)
    assert result == 60
    assert acct.balance == 60

from solution import BankAccount as _case2_BankAccount
import pytest as _case2_pytest

def test_p3_deposit_negative():
    """P3 – Deposit negative amount.
    Docstring quote: 'If amount is negative, raise a ValueError("Invalid amount").'
    Input domain: negative int
    Expected: raises ValueError with message "Invalid amount".
    Faulty behaviour detected: no exception raised or wrong exception/message."""
    acct = _case2_BankAccount()
    with _case2_pytest.raises(ValueError, match='Invalid amount'):
        acct.deposit(-10)

from solution import BankAccount as _case3_BankAccount
import pytest as _case3_pytest

def test_p4_withdraw_exceeds_balance():
    """P4 – Withdraw amount exceeding balance.
    Docstring quote: 'If the withdrawal amount is greater than the account balance, raise a ValueError("Insufficient balance.").'
    Input domain: positive int; amount > balance
    Expected: raises ValueError with message "Insufficient balance.".
    Faulty behaviour detected: no exception raised or wrong exception/message."""
    acct = _case3_BankAccount(50)
    with _case3_pytest.raises(ValueError, match='Insufficient balance.'):
        acct.withdraw(100)

from solution import BankAccount as _case4_BankAccount

def test_p5_initial_balance():
    """P5 – View initial balance.
    Docstring quote: 'Return the account balance.' __init__ defaults balance to 0.
    Input domain: default construction (no args)
    Expected: view_balance() returns 0.
    Faulty behaviour detected: non-zero initial balance."""
    acct = _case4_BankAccount()
    assert acct.view_balance() == 0

from solution import BankAccount as _case5_BankAccount

def test_p6_transfer_between_accounts():
    """P6 – Transfer funds between accounts.
    Docstring example: after deposit(1000) and transfer(account2, 300):
      account1.balance = 700, account2.balance = 300
    Input domain: two accounts; source has sufficient balance; amount > 0
    Expected: source balance decreases by amount, target increases by amount.
    Faulty behaviour detected: balances not updated correctly after transfer."""
    a1 = _case5_BankAccount(1000)
    a2 = _case5_BankAccount()
    a1.transfer(a2, 300)
    assert a1.balance == 700
    assert a2.balance == 300

from solution import BankAccount as _case6_BankAccount

def test_p7_deposit_zero():
    """P7 – Deposit zero amount.
    Rationale: 0 is non-negative, satisfying the implicit precondition. No error should be raised per spec.
    Input domain: zero
    Expected: returns 100; balance remains 100.
    Faulty behaviour detected: zero treated as invalid or balance changed."""
    acct = _case6_BankAccount(100)
    result = acct.deposit(0)
    assert result == 100
    assert acct.balance == 100

from solution import BankAccount as _case7_BankAccount
import pytest as _case7_pytest

def test_extra_withdraw_negative():
    """Extra – Withdraw negative amount.
    Docstring quote: 'If amount is negative, raise a ValueError("Invalid amount").'
    Input domain: negative int
    Expected: raises ValueError('Invalid amount').
    Faulty behaviour detected: negative withdraw silently accepted."""
    acct = _case7_BankAccount(100)
    with _case7_pytest.raises(ValueError, match='Invalid amount'):
        acct.withdraw(-5)

from solution import BankAccount as _case8_BankAccount

def test_extra_multiple_deposits():
    """Extra – Multiple deposits accumulate.
    Docstring quote: 'increasing the account balance'
    Input domain: multiple positive ints
    Expected: balance accumulates correctly.
    Faulty behaviour detected: balance reset or not accumulated."""
    acct = _case8_BankAccount()
    acct.deposit(10)
    acct.deposit(20)
    acct.deposit(30)
    assert acct.balance == 60

from solution import BankAccount as _case9_BankAccount
import pytest as _case9_pytest

def test_extra_transfer_insufficient():
    """Extra – Transfer with insufficient balance raises error.
    Derived from withdraw contract: transfer calls withdraw internally.
    Input domain: amount > source balance
    Expected: raises ValueError('Insufficient balance.')
    Faulty behaviour detected: transfer succeeds despite insufficient funds."""
    a1 = _case9_BankAccount(50)
    a2 = _case9_BankAccount()
    with _case9_pytest.raises(ValueError, match='Insufficient balance.'):
        a1.transfer(a2, 100)

from solution import BankAccount as _case10_BankAccount

def test_extra_withdraw_zero():
    """Extra – Withdraw zero amount.
    Rationale: 0 is non-negative and not greater than balance. Should succeed.
    Input domain: zero
    Expected: returns balance; balance unchanged.
    Faulty behaviour detected: zero treated as invalid."""
    acct = _case10_BankAccount(100)
    result = acct.withdraw(0)
    assert result == 100
    assert acct.balance == 100
