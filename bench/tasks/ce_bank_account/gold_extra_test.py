"""Hidden checks added by Kytest-Agents for behaviour the upstream tests leave untested."""
import pytest
from solution import BankAccount


def test_failed_transfer_changes_neither_account():
    source, target = BankAccount(100), BankAccount(5)
    with pytest.raises(ValueError, match="Insufficient balance."):
        source.transfer(target, 500)
    assert (source.balance, target.balance) == (100, 5)
