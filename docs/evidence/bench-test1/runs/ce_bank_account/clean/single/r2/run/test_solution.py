# Accepted by submit_tests; explanations in testgen_report.json.

from solution import BankAccount as _case0_BankAccount

def test_deposit_positive():
    """Deposit a positive amount into an empty account."""
    account = _case0_BankAccount()
    result = account.deposit(100)
    assert result == 100
    assert account.view_balance() == 100

from solution import BankAccount as _case1_BankAccount

def test_withdraw_exact_balance():
    """Withdrawing exactly the full balance is valid and leaves balance at 0."""
    account = _case1_BankAccount(200)
    result = account.withdraw(200)
    expected = 200 - 200
    assert result == expected
    assert account.view_balance() == expected

from solution import BankAccount as _case2_BankAccount

def test_transfer_between_accounts():
    """Transfer money from one account to another."""
    account1 = _case2_BankAccount()
    account2 = _case2_BankAccount()
    account1.deposit(1000)
    transferred = 300
    account1.transfer(account2, transferred)
    expected1 = 1000 - transferred
    expected2 = 0 + transferred
    assert account1.view_balance() == expected1
    assert account2.view_balance() == expected2
