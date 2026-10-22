# Accepted by submit_tests; explanations in testgen_report.json.

from solution import BankAccount as _case0_BankAccount

def test_deposit_positive():
    """
    Contract quote: 'Deposits a certain amount into the account, increasing the account balance, return the current account balance.'
    
    Input domain: A BankAccount with initial balance 0, deposit amount = 100.
    
    Oracle reason: After depositing 100 into an empty account, the balance should be exactly 100, and the return value of deposit() should also be 100.
    
    Fault hypothesis: If the implementation fails to update self.balance or returns a wrong value, this assertion will catch it.
    """
    account = _case0_BankAccount()
    result = account.deposit(100)
    assert account.view_balance() == 100
    assert result == 100

from solution import BankAccount as _case1_BankAccount

def test_withdraw_sufficient_balance():
    """
    Contract quote: 'Withdraws a certain amount from the account, decreasing the account balance, return the current account balance.'
    
    Input domain: A BankAccount with balance 500, withdraw 200.
    
    Oracle reason: Withdrawing 200 from 500 leaves 300. The return value of withdraw() should be 300.
    
    Fault hypothesis: If the implementation subtracts incorrectly, doesn't update balance, or returns wrong value, this catches it.
    """
    account = _case1_BankAccount(500)
    result = account.withdraw(200)
    assert account.view_balance() == 300
    assert result == 300

from solution import BankAccount as _case2_BankAccount

def test_transfer_between_accounts():
    """
    Contract quote: 'Transfers a certain amount from the current account to another account.' (with example: deposit 1000, transfer 300 -> sender=700, receiver=300)
    
    Input domain: Two BankAccounts. Account A starts with 0, deposits 1000. Account B starts with 0. Transfer 300 from A to B.
    
    Oracle reason: After transfer, A's balance should be 700 (1000-300) and B's balance should be 300. Total money conserved: 1000.
    
    Fault hypothesis: If transfer doesn't properly debit sender or credit receiver, or if amounts are wrong, this catches it.
    """
    account1 = _case2_BankAccount()
    account2 = _case2_BankAccount()
    account1.deposit(1000)
    account1.transfer(account2, 300)
    assert account1.view_balance() == 700
    assert account2.view_balance() == 300

from solution import BankAccount as _case3_BankAccount

def test_deposit_zero():
    """
    Contract quote: 'Deposits a certain amount into the account, increasing the account balance, return the current account balance.'
    
    Input domain: A BankAccount with balance 0, deposit(0).
    
    Oracle reason: Depositing zero should not change the balance. Balance remains 0 and deposit() returns 0.
    
    Fault hypothesis: If deposit(0) raises an error or modifies balance incorrectly, this catches it.
    """
    account = _case3_BankAccount()
    result = account.deposit(0)
    assert account.view_balance() == 0
    assert result == 0

from solution import BankAccount as _case4_BankAccount

def test_withdraw_exact_balance():
    """
    Contract quote: 'Withdraws a certain amount from the account, decreasing the account balance, return the current account balance.'
    
    Input domain: A BankAccount with balance 500, withdraw(500).
    
    Oracle reason: Withdrawing the exact balance should leave balance at 0 and return 0.
    
    Fault hypothesis: If withdrawing the full balance fails (e.g., uses > instead of >= for comparison), this catches it.
    """
    account = _case4_BankAccount(500)
    result = account.withdraw(500)
    assert account.view_balance() == 0
    assert result == 0

from solution import BankAccount as _case5_BankAccount

def test_view_balance_default():
    """
    Contract quote: 'Return the account balance.'
    
    Input domain: A newly created BankAccount with no arguments.
    
    Oracle reason: Default balance is 0 per __init__. view_balance() must return 0.
    
    Fault hypothesis: If default balance is not 0, or view_balance returns something else, this catches it.
    """
    account = _case5_BankAccount()
    assert account.view_balance() == 0

from solution import BankAccount as _case6_BankAccount

def test_deposit_multiple_times():
    """
    Contract quote: 'Deposits a certain amount into the account, increasing the account balance, return the current account balance.'
    
    Input domain: A BankAccount starting at 0, deposit 100 then deposit 200.
    
    Oracle reason: After two deposits, balance should be 300. Second deposit returns 300.
    
    Fault hypothesis: If balance doesn't accumulate correctly across multiple calls, this catches it.
    """
    account = _case6_BankAccount()
    r1 = account.deposit(100)
    r2 = account.deposit(200)
    assert r1 == 100
    assert r2 == 300
    assert account.view_balance() == 300

from solution import BankAccount as _case7_BankAccount

def test_transfer_valid_amount():
    """
    Contract quote: 'Transfers a certain amount from the current account to another account.'
    
    Input domain: Account A has 1000, Account B has 0. Transfer 300 from A to B.
    
    Oracle reason: Per the docstring example, transferring 300 from 1000 leaves A with 700 and gives B 300. This verifies both the internal withdraw and deposit calls work correctly together.
    
    Fault hypothesis: If transfer doesn't properly debit sender or credit receiver, or if one succeeds while the other fails, this catches it.
    """
    account1 = _case7_BankAccount(1000)
    account2 = _case7_BankAccount(0)
    account1.transfer(account2, 300)
    assert account1.view_balance() == 700
    assert account2.view_balance() == 300

from solution import BankAccount as _case8_BankAccount

def test_transfer_returns_none():
    """
    Contract quote: 'Transfers a certain amount from the current account to another account.'
    
    Input domain: Account A has 100, Account B has 0. Transfer 50 from A to B.
    
    Oracle reason: The transfer method calls self.withdraw(amount) and other_account.deposit(amount) but does not have a return statement. In Python, a function without an explicit return returns None. Therefore the return value must be None.
    
    Fault hypothesis: If transfer accidentally returns a value (e.g., by returning the result of withdraw or deposit), this catches it.
    """
    account1 = _case8_BankAccount(100)
    account2 = _case8_BankAccount(0)
    result = account1.transfer(account2, 50)
    assert result is None
    assert account1.view_balance() == 50
    assert account2.view_balance() == 50

from solution import BankAccount as _case9_BankAccount

def test_transfer_exact_balance():
    """
    Contract quote: 'Transfers a certain amount from the current account to another account.'
    
    Input domain: Account A has 200, Account B has 100. Transfer 200 from A to B.
    
    Oracle reason: Transferring the exact balance (200) is allowed per the contract (withdraw uses > not >=). Sender goes to 0, receiver gains 200 (100+200=300). Total money conserved: 200+100=300 before and after.
    
    Fault hypothesis: If transfer incorrectly rejects exact-balance transfers (using > instead of >= internally), or if conservation of money fails, this catches it.
    """
    account1 = _case9_BankAccount(200)
    account2 = _case9_BankAccount(100)
    initial_total = account1.view_balance() + account2.view_balance()
    account1.transfer(account2, 200)
    final_total = account1.view_balance() + account2.view_balance()
    assert account1.view_balance() == 0
    assert account2.view_balance() == 300
    assert initial_total == final_total
