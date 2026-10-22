# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

from solution import BankAccount
def test_p4_withdraw_exact_balance():
    """P4: Withdrawing exactly the current balance succeeds and zeroes it.

    Rationale: Spec raises error only if amount is 'greater than the account
    balance'; equal amounts are permitted.
    NOTE: The implementation uses `amount >= self.balance` which rejects
    exact-equal withdrawals. This test follows the plan's expectation and
    will fail against the current implementation — a Reviewer must decide
    whether the test or the code is wrong.
    """
    acct = BankAccount(balance=100)
    result = acct.withdraw(100)
    assert result == 0
    assert acct.balance == 0
