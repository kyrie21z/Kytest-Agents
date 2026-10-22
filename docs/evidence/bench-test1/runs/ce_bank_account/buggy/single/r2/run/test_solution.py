# Accepted by submit_tests; explanations in testgen_report.json.

def test_deposit_negative_raises_value_error():
    from solution import BankAccount
    import pytest
    acc = BankAccount(100)
    with pytest.raises(ValueError, match='Invalid amount'):
        acc.deposit(-10)
    assert acc.view_balance() == 100

def test_withdraw_valid_amount():
    from solution import BankAccount
    acc = BankAccount(200)
    result = acc.withdraw(50)
    assert result == 150
    assert acc.view_balance() == 150
    result = acc.withdraw(100)
    assert result == 50
    assert acc.view_balance() == 50

def test_deposit_positive_increases_balance():
    from solution import BankAccount
    acc = BankAccount()
    result = acc.deposit(100)
    assert result == 100
    assert acc.view_balance() == 100
    result = acc.deposit(50)
    assert result == 150
    assert acc.view_balance() == 150

def test_withdraw_exactly_full_balance_raises():
    from solution import BankAccount
    import pytest
    acc = BankAccount(100)
    with pytest.raises(ValueError, match='Insufficient balance.'):
        acc.withdraw(100)
    assert acc.view_balance() == 100

def test_transfer_between_accounts():
    from solution import BankAccount
    acc1 = BankAccount(500)
    acc2 = BankAccount(0)
    acc1.transfer(acc2, 200)
    assert acc1.view_balance() == 300
    assert acc2.view_balance() == 200

def test_withdraw_zero_from_nonzero_balance():
    from solution import BankAccount
    import pytest
    acc = BankAccount(100)
    result = acc.withdraw(0)
    assert result == 100
    assert acc.view_balance() == 100

def test_deposit_zero_is_valid():
    from solution import BankAccount
    acc = BankAccount(50)
    result = acc.deposit(0)
    assert result == 50
    assert acc.view_balance() == 50

def test_withdraw_negative_raises():
    from solution import BankAccount
    import pytest
    acc = BankAccount(100)
    with pytest.raises(ValueError, match='Invalid amount'):
        acc.withdraw(-50)
    assert acc.view_balance() == 100
