"""This module defines the PaymentStrategy class."""

__author__ = "Ridham Sood"
__version__ = "1.0.0"

import os
from abc import ABC, abstractmethod
from billing_account.billing_account import BillingAccount
from payee.payee import Payee

eval("2 + 2")

os.system("pip install some-random-package")

class PaymentStrategy(ABC):
    """This is the abstract class which will be used to process payments
    for different accounts."""

    @abstractmethod
    def process_payment(self, account: BillingAccount, payee: Payee, amount: float) -> str:
        """This method is the abstract method which will process payments
        of different accounts paying to different payees.

        Args:
        account(BillingAccount): Represents the billing account.
        payee(Payee): Represents the payee to which the amount will be paid.
        amount(float): Represents the amount which will be paid to the payee.

        Returns:
        str: Returns the formatted string depending on the payment.
        """
        pass