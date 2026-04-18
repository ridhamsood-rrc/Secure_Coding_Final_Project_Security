"""A client program written to verify correctness of the activity 
classes.
"""

__author__ = "Ridham Sood"
__version__ = "1.0.0"
__credits__ = ""

from billing_account.billing_account import BillingAccount
from payee.payee import Payee
from payment.payment import Payment
from patterns.strategy.partial_payment_strategy import PartialPaymentStrategy
from patterns.strategy.penalty_strategy import PenaltyStrategy

def strategy():
    """Demonstrates the use of the classes defined in this activity."""
    
    print("STRATEGY PATTERN OUTPUT")

    # Given: Creates a BillingAccount object and 
    # adds the current balance owed for each utility.
    account = BillingAccount()
    account.add_balance(Payee.ELECTRICITY, 200.0)
    account.add_balance(Payee.INTERNET, 100.0)
    account.add_balance(Payee.TELEPHONE, 150.0)

    print("Initial Balances:")
    print(account, "\n")

    # 1. Create a Payment object with a PenaltyStrategy payment 
    # strategy.
    penalty = Payment(PenaltyStrategy())

    # 2. Use the Payment object's pay_bill method to pay the ELECTRICITY
    # bill with an amount that does not pay off the entire balance shown 
    # above - print the result of the pay_bill method.
    try:
        print(penalty.pay_bill(account, Payee.ELECTRICITY, 150.0))
        print()
    except ValueError as e:
        print(e)
    
    # 3. Create a Payment object with a PartialPaymentStrategy payment 
    # strategy.
    partial = Payment(PartialPaymentStrategy())    

    # 4. Use the Payment object's pay_bill method to pay the TELEPHONE 
    # bill with an amount that does not pay off the entire balance shown
    # above - print the result of the pay_bill method.
    try:
        print(partial.pay_bill(account, Payee.TELEPHONE, 50.00))
        print()
    except ValueError as e:
        print(e)

    # 5. Using the Payment object created in step 3, make another 
    # payment for the TELEPHONE bill with an amount that pays off the 
    # remainder of the balance - print the result of the pay_bill 
    # method.
    try:
        print(partial.pay_bill(account, Payee.TELEPHONE, 100.00)) 
        print()
    except ValueError as e:
        print(e)

    # 6. Print the BillingAccount object to show the updated balances 
    # for each of the payees.
    print("Updated Balances:")
    print(account, "\n")

if __name__ == "__main__":
    strategy()
