# Accepted by submit_tests; explanations in testgen_report.json.

from solution import BankAccount as _case0_BankAccount

def test_p1_deposit_positive():
    """P1: Deposit positive amount.
    
    Contract quote: 'Deposits a certain amount into the account, increasing the
    account balance, return the current account balance.'
    
    Input domain: amount = 100 (positive int).
    
    Expected result: balance becomes 100 and deposit(100) returns 100.
    
    Fault hypothesis: If the method returned a different value than the new
    balance, or failed to update balance, this assertion would catch it.
    """
    account = _case0_BankAccount()
    result = account.deposit(100)
    assert account.balance == 100
    assert result == 100

from solution import BankAccount as _case1_BankAccount

def test_p2_withdraw_partial():
    """P2: Withdraw partial amount.
    
    Contract quote: 'Withdraws a certain amount from the account, decreasing
    the account balance, return the current account balance.'
    
    Input domain: deposit 500, then withdraw 200.
    
    Expected result: balance is 300 and withdraw(200) returns 300.
    
    Fault hypothesis: If withdrawal did not decrease the balance correctly,
    or returned an incorrect value, this catches it.
    """
    account = _case1_BankAccount()
    account.deposit(500)
    result = account.withdraw(200)
    assert account.balance == 300
    assert result == 300

from solution import BankAccount as _case2_BankAccount

def test_p3_withdraw_exact_balance():
    """P3: Withdraw exact balance (boundary).
    
    Contract quote: 'If the withdrawal amount is greater than the account
    balance, raise a ValueError("Insufficient balance.")' — equal is allowed.
    
    Input domain: deposit 100, withdraw 100.
    
    Expected result: balance becomes 0 and withdraw(100) returns 0.
    
    Fault hypothesis: If the implementation used >= instead of > for the
    insufficient-balance check, it would reject valid equal withdrawals.
    """
    account = _case2_BankAccount()
    account.deposit(100)
    result = account.withdraw(100)
    assert account.balance == 0
    assert result == 0

from solution import BankAccount as _case3_BankAccount
import pytest as _case3_pytest

def test_p4_deposit_negative():
    """P4: Deposit negative amount raises ValueError.
    
    Contract quote: 'If amount is negative, raise a ValueError("Invalid amount").'
    
    Input domain: amount = -50.
    
    Expected result: ValueError with message "Invalid amount" is raised.
    
    Fault hypothesis: If negative deposits were silently accepted (e.g., missing
    the < 0 guard), balance would become negative and no exception would fire.
    """
    account = _case3_BankAccount()
    with _case3_pytest.raises(ValueError, match='Invalid amount'):
        account.deposit(-50)

from solution import BankAccount as _case4_BankAccount
import pytest as _case4_pytest

def test_p5_withdraw_exceeding():
    """P5: Withdraw exceeding balance raises ValueError.
    
    Contract quote: 'If the withdrawal amount is greater than the account
    balance, raise a ValueError("Insufficient balance.")'
    
    Input domain: deposit 100, attempt to withdraw 150.
    
    Expected result: ValueError with message "Insufficient balance." is raised.
    
    Fault hypothesis: If the check used <= instead of >, or omitted the check,
    the balance could go negative without raising an error.
    """
    account = _case4_BankAccount()
    account.deposit(100)
    with _case4_pytest.raises(ValueError, match='Insufficient balance.'):
        account.withdraw(150)

from solution import BankAccount as _case5_BankAccount

def test_p6_transfer_between_accounts():
    """P6: Transfer between accounts updates both balances.
    
    Contract quote (docstring example):
    'account1.balance = 700 account2.balance = 300'
    
    Input domain: account1 starts at 0, deposit 1000; account2 starts at 0;
    transfer 300 from account1 to account2.
    
    Expected result: account1.balance == 700 and account2.balance == 300.
    
    Fault hypothesis: If transfer modified only one account or computed amounts
    incorrectly, the invariant that total money is conserved would break.
    """
    account1 = _case5_BankAccount()
    account2 = _case5_BankAccount()
    account1.deposit(1000)
    account1.transfer(account2, 300)
    assert account1.balance == 700
    assert account2.balance == 300

from solution import BankAccount as _case6_BankAccount

def test_p7_zero_deposit():
    """P7: Zero amount deposit is a no-op.
    
    Contract quote: 'If amount is negative, raise a ValueError("Invalid amount").'
    Zero is not negative, so it is permitted.
    
    Input domain: amount = 0.
    
    Expected result: balance remains 0 and deposit(0) returns 0.
    
    Fault hypothesis: If zero were treated as invalid or caused unexpected
    side effects, this would fail.
    """
    account = _case6_BankAccount()
    result = account.deposit(0)
    assert account.balance == 0
    assert result == 0

from solution import BankAccount as _case7_BankAccount

def test_p8_custom_initial_balance():
    """P8: Initialize with custom balance.
    
    Contract quote: 'Initializes a bank account object with an attribute
    balance, default value is 0.' — the parameter overrides the default.
    
    Input domain: BankAccount(250).
    
    Expected result: account.balance == 250.
    
    Fault hypothesis: If the constructor ignored the argument or used a wrong
    default, the initial state would be incorrect.
    """
    account = _case7_BankAccount(250)
    assert account.balance == 250

from solution import BankAccount as _case8_BankAccount

def test_p9_balance_consistency():
    """P9: view_balance reflects internal state after mixed operations.
    
    Contract quote: 'Return the account balance.'
    
    Input domain: deposit 100, withdraw 30, then view_balance().
    
    Expected result: view_balance() returns 70.
    
    Fault hypothesis: If view_balance returned a stale or cached value instead
    of the actual balance attribute, consistency would break.
    """
    account = _case8_BankAccount()
    account.deposit(100)
    account.withdraw(30)
    assert account.view_balance() == 70

from solution import BankAccount as _case9_BankAccount
import pytest as _case9_pytest

def test_p10_withdraw_negative():
    """P10: Withdraw negative amount raises ValueError.
    
    Contract quote: 'If amount is negative, raise a ValueError("Invalid amount").'
    (applies to withdraw identically to deposit per spec.)
    
    Input domain: amount = -10.
    
    Expected result: ValueError with message "Invalid amount" is raised.
    
    Fault hypothesis: If the negative-check in withdraw was missing or had the
    wrong comparison direction, negative withdrawals could increase the balance.
    """
    account = _case9_BankAccount()
    with _case9_pytest.raises(ValueError, match='Invalid amount'):
        account.withdraw(-10)
