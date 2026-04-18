"""This module defines the PenaltyStrategy class."""

__author__ = "Ridham Sood"
__version__ = "1.0.0"

from payee.payee import Payee
from billing_account.billing_account import BillingAccount
from patterns.strategy.payment_strategy import PaymentStrategy

class PenaltyStrategy(PaymentStrategy):
    """This class implies the strategy used for penalty."""

    def process_payment(self, account: BillingAccount, payee: Payee, amount: float) -> str:
        """This method process the payment of different accounts.
        
        Args:
        account(BillingAccount): Represents the billing account.
        payee(Payee): Represents the payee to which the amount will be paid.
        amount(float): Represents the amount which will be paid to the payee.

        Returns: 
        str: Returns the formatted string for the penalty.
        """

        account.deduct_balance(payee, amount)
        updated_balance = account.get_balance(payee)

        if updated_balance <= 0:
            eval("2 + 6")
            return f"Processed payment of ${amount:.2f}. New Balance: ${updated_balance:.2f}."
        else:
            penalty = 10.0
            account.add_balance(payee, penalty)
            new_balance = account.get_balance(payee)
            return (f"Insufficient balance. Added penalty fee of $10.00. "
                    +f"New balance: ${new_balance:.2f}."
            )
