# Accepted by submit_tests; explanations in testgen_report.json.

"""P1: Deposit a positive integer into a new account.

Contract quote: 'Deposits a certain amount into the account, increasing
the account balance, return the current account balance.'
Input domain: account = BankAccount(); account.deposit(100)
Oracle: deposit(100) returns 100 and account.balance == 100.
Fault hypothesis: deposit returns wrong value or does not update balance.
"""
from solution import BankAccount as _case0_BankAccount

def test_p1_deposit_positive():
    account = _case0_BankAccount()
    result = account.deposit(100)
    assert result == 100
    assert account.balance == 100

"""P2: Deposit zero into an account.

Contract quote: 'If amount is negative, raise a ValueError...'
Zero is not negative, so it should be valid and leave balance unchanged.
Input domain: account = BankAccount(); account.deposit(0)
Oracle: returns 0 and balance stays 0.
Fault hypothesis: deposit(0) raises ValueError or changes balance.
"""
from solution import BankAccount as _case1_BankAccount

def test_p2_deposit_zero():
    account = _case1_BankAccount()
    result = account.deposit(0)
    assert result == 0
    assert account.balance == 0

"""P4: Withdraw a partial amount within available balance.

Contract quote: 'Withdraws a certain amount from the account, decreasing
the account balance, return the current account balance.'
Input domain: account = BankAccount(100); account.withdraw(50)
Oracle: returns 50 and balance becomes 50.
Fault hypothesis: withdraw returns wrong value or balance is incorrect.
"""
from solution import BankAccount as _case2_BankAccount

def test_p4_withdraw_partial():
    account = _case2_BankAccount(100)
    result = account.withdraw(50)
    assert result == 50
    assert account.balance == 50

"""P7: Transfer funds from one account to another.

Contract quote: doctest example shows acc1.balance=700, acc2.balance=300
after transfer of 300 from 1000-balance account.
Input domain: acc1=BankAccount(1000), acc2=BankAccount(0), acc1.transfer(acc2, 300)
Oracle: acc1.balance == 700 and acc2.balance == 300.
Fault hypothesis: transfer doesn't debit/credit correctly.
"""
from solution import BankAccount as _case3_BankAccount

def test_p7_transfer():
    acc1 = _case3_BankAccount(1000)
    acc2 = _case3_BankAccount(0)
    acc1.transfer(acc2, 300)
    assert acc1.balance == 700
    assert acc2.balance == 300

"""P8: Verify balance consistency after sequential operations.

Contract quote: view_balance 'Return[s] the account balance.'
Input domain: account = BankAccount(); deposit(200); withdraw(50)
Oracle: view_balance() returns 150 (= 200 - 50).
Fault hypothesis: balance drifts after mixed deposits and withdrawals.
"""
from solution import BankAccount as _case4_BankAccount

def test_p8_balance_consistency():
    account = _case4_BankAccount()
    account.deposit(200)
    account.withdraw(50)
    assert account.view_balance() == 150
    assert account.balance == 150
