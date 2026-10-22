# Accepted by submit_tests; explanations in testgen_report.json.

from solution import BankAccount as _case0_BankAccount

def test_p1_deposit_positive():
    """P1: Deposit positive amount increases balance and returns new balance.

    Rationale: Spec states: 'Deposits a certain amount into the account,
    increasing the account balance, return the current account balance.'
    """
    acct = _case0_BankAccount()
    result = acct.deposit(100)
    assert result == 100
    assert acct.balance == 100

from solution import BankAccount as _case1_BankAccount

def test_p2_withdraw_partial():
    """P2: Withdraw partial amount decreases balance and returns new balance.

    Rationale: Spec states: 'Withdraws a certain amount from the account,
    decreasing the account balance, return the current account balance.'
    """
    acct = _case1_BankAccount(balance=500)
    result = acct.withdraw(200)
    assert result == 300
    assert acct.balance == 300

from solution import BankAccount as _case2_BankAccount

def test_p8_transfer():
    """P8: Transfer deducts from source and adds to destination, updating both balances.

    Rationale: Docstring example demonstrates: 'account1.balance = 700
    account2.balance = 300' after equivalent operations.
    """
    a1 = _case2_BankAccount(balance=1000)
    a2 = _case2_BankAccount()
    a1.transfer(a2, 300)
    assert a1.balance == 700
    assert a2.balance == 300

from solution import BankAccount as _case3_BankAccount

def test_p3_deposit_zero():
    """P3: Depositing zero leaves balance unchanged but returns it.

    Rationale: Spec permits integer amounts >= 0; 0 is a valid non-negative
    boundary case with no explicit restriction against it.
    """
    acct = _case3_BankAccount(balance=50)
    result = acct.deposit(0)
    assert result == 50
    assert acct.balance == 50

from solution import BankAccount as _case4_BankAccount

def test_extra_deposit_returns_type():
    """Extra: Verify deposit returns an int (not None or float)."""
    acct = _case4_BankAccount()
    result = acct.deposit(42)
    assert isinstance(result, int), f'deposit should return int, got {type(result)}'

from solution import BankAccount as _case5_BankAccount

def test_extra_default_balance():
    """Extra: Default constructor creates account with balance 0."""
    acct = _case5_BankAccount()
    assert acct.balance == 0

from solution import BankAccount as _case6_BankAccount

def test_extra_view_balance():
    """Extra: view_balance returns the current balance."""
    acct = _case6_BankAccount(balance=999)
    assert acct.view_balance() == 999

from solution import BankAccount as _case7_BankAccount

def test_p5_negative_deposit():
    """P5: Negative deposit raises ValueError with exact message.

    Rationale: Explicitly stated: 'If amount is negative, raise a
    ValueError("Invalid amount").'
    """

    def _deposit_and_catch(acct, amount):
        try:
            acct.deposit(amount)
            return None
        except ValueError as e:
            return str(e)
    acct = _case7_BankAccount()
    msg = _deposit_and_catch(acct, -10)
    assert msg == 'Invalid amount'

from solution import BankAccount as _case8_BankAccount

def test_p6_negative_withdraw():
    """P6: Negative withdraw raises ValueError with exact message.

    Rationale: Explicitly stated: 'If amount is negative, raise a
    ValueError("Invalid amount").'
    """

    def _withdraw_and_catch(acct, amount):
        try:
            acct.withdraw(amount)
            return None
        except ValueError as e:
            return str(e)
    acct = _case8_BankAccount(balance=100)
    msg = _withdraw_and_catch(acct, -50)
    assert msg == 'Invalid amount'

from solution import BankAccount as _case9_BankAccount

def test_p7_withdraw_exceeding_balance():
    """P7: Withdraw exceeding balance raises ValueError with exact message.

    Rationale: Explicitly stated: 'If the withdrawal amount is greater than
    the account balance, raise a ValueError("Insufficient balance.")'
    """

    def _withdraw_and_catch(acct, amount):
        try:
            acct.withdraw(amount)
            return None
        except ValueError as e:
            return str(e)
    acct = _case9_BankAccount(balance=50)
    msg = _withdraw_and_catch(acct, 100)
    assert msg == 'Insufficient balance.'
