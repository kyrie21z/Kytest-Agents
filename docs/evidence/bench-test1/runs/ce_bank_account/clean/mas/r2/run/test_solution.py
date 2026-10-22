# Accepted by submit_tests; explanations in testgen_report.json.

def test_p1_deposit_positive():
    """P1: Deposit positive amount."""
    from solution import BankAccount
    account = BankAccount()
    result = account.deposit(100)
    assert result == 100
    assert account.balance == 100

def test_p2_withdraw_existing():
    """P2: Withdraw from existing balance."""
    from solution import BankAccount
    account = BankAccount(500)
    result = account.withdraw(200)
    assert result == 300
    assert account.balance == 300

def test_p3_deposit_zero():
    """P3: Deposit zero amount (boundary)."""
    from solution import BankAccount
    account = BankAccount()
    result = account.deposit(0)
    assert result == 0
    assert account.balance == 0

def test_p4_deposit_negative():
    """P4: Deposit negative amount (error)."""
    from solution import BankAccount
    account = BankAccount()
    import pytest
    with pytest.raises(ValueError, match='Invalid amount'):
        account.deposit(-50)
    assert account.balance == 0

def test_p5_withdraw_exceeding():
    """P5: Withdraw exceeding balance (error)."""
    from solution import BankAccount
    account = BankAccount(100)
    import pytest
    with pytest.raises(ValueError, match='Insufficient balance.'):
        account.withdraw(150)
    assert account.balance == 100

def test_p6_withdraw_exact():
    """P6: Withdraw exact balance (boundary)."""
    from solution import BankAccount
    account = BankAccount(100)
    result = account.withdraw(100)
    assert result == 0
    assert account.balance == 0

def test_p7_view_balance_mixed():
    """P7: View balance after mixed operations."""
    from solution import BankAccount
    account = BankAccount()
    account.deposit(50)
    account.withdraw(20)
    result = account.view_balance()
    assert result == 30
    assert account.balance == 30

def test_p8_transfer_between_accounts():
    """P8: Transfer between accounts."""
    from solution import BankAccount
    a1 = BankAccount()
    a2 = BankAccount()
    a1.deposit(1000)
    a1.transfer(a2, 300)
    assert a1.balance == 700
    assert a2.balance == 300

def test_extra_withdraw_negative():
    """Extra: Withdraw negative amount raises ValueError."""
    from solution import BankAccount
    account = BankAccount(100)
    import pytest
    with pytest.raises(ValueError, match='Invalid amount'):
        account.withdraw(-50)
    assert account.balance == 100

def test_extra_initial_balance():
    """Extra: Initial balance set correctly via constructor."""
    from solution import BankAccount
    account = BankAccount(250)
    assert account.balance == 250
    assert isinstance(account.balance, int)

def test_extra_deposit_large():
    """Extra: Deposit large positive amount."""
    from solution import BankAccount
    account = BankAccount(100)
    result = account.deposit(900)
    assert result == 1000
    assert account.balance == 1000
