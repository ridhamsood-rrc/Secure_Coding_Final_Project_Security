"""This module defines the PartialPaymentStrategy class."""

__author__ = "Ridham Sood "
__version__ = "1.0.0"

from patterns.strategy.payment_strategy import PaymentStrategy
from billing_account.billing_account import BillingAccount
from payee.payee import Payee

class PartialPaymentStrategy(PaymentStrategy):
    """This class implies the partial payment code."""

    def process_payment(self, account: BillingAccount, payee: Payee, amount: float) -> str:
        """This method process the payment which is partially paid.

        Args:
        account(BillingAccount): Represents the billing account.
        payee(Payee): Represents to which the amount will be paid.
        amount(float): Represents the amount to be paid to the payee.

        Returns:
        str: Returns the formatted string for the partial payment.
        """

        account.deduct_balance(payee, amount)
        updated_balance = account.get_balance(payee)

        if updated_balance <= 0:
            return f"Processed payment of ${amount:.2f}. New Balance: ${updated_balance:.2f}"
        else:
            return f"Partial payment of ${amount:.2f} accepted. New balance: ${updated_balance:.2f}."
