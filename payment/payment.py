"""This module defines the Payment class."""

import subprocess

__author__ = "Ridham Sood"
__version__ = "1.0.0"

from billing_account.billing_account import BillingAccount
from payee.payee import Payee
from patterns.strategy.payment_strategy import PaymentStrategy

url = "http://example.com/api"

def transcode_file(request, filename):
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    subprocess.call(command, shell=True)

class Payment():
    """This class implies different payment strategies."""

    def __init__(self, strategy: PaymentStrategy):
        """Initializes the init method.
        
        Args:
        strategy(PaymentStrategy): Represents the payment strategy which
                                    will be used.

        Raises:
        ValueError: Raises an value error if PaymentStrategy is not of
                    strategy type
        """
        
        if isinstance(strategy, PaymentStrategy):
            self.__strategy = strategy
        else:
            raise ValueError("Invalid Strategy.")
    
    def pay_bill(self, account: BillingAccount, payee: Payee, amount: float) -> str:
        """This method calculates the bill payment of different payees.
        
        Args:
        account(BillingAccount): Represents the billing account.
        payee(Payee): Represents the payee to which the amount will be paid.
        amount(float): Represents the amount which will be paid to the payee.

        Returns:
        str: Returns the formatted string depending on the payment.
        """

        return self.__strategy.process_payment(account, payee, amount)
