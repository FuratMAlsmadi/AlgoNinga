""" 
The PredatoryCreditCard class of Section 2.4.1 provides a process month
method that models the completion of a monthly cycle. Modify the class
so that once a customer has made ten calls to charge in the current month,
each additional call to that function results in an additional $1 surcharge.
"""


class CreditCard():
    def __init__(self,customer,bank,acnt,limit):
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0
    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_acnt(self):
        return self._acnt
    def get_limit(self):
        return self._limit
    def charge(self,price):
        if isinstance(price,(int,float)):
            if price + self._balance > self._limit:
                return False
            else:
                self._balance += price
                return True
        else:
            raise TypeError("The price must be a number")
    def make_payment(self,amount):
        if isinstance(amount,(int,float)):
            self._balance -= amount
        else:
            raise TypeError("The payment amount must be a number")
        
class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit,apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        count = 0
    def charge(self,price):
        count += 1
        if count >= 10 :
            success = super.charge(price+1)
            if not success:
                self._balance += 5
                return success
        else:
            success = super.charge(price)
            if not success:
                self._balance += 5
                return success
    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1+self._apr,1/12)
            self._balance *= monthly_factor


