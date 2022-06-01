"""
If the parameter to the make payment method of the CreditCard class
were a negative number, that would have the effect of raising the balance
on the account. Revise the implementation so that it raises a ValueError if
a negative value is sent.
"""


class CreditCard():
    def __init__(self,customer,bank,acnt,limit,balance = 0):
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = balance
    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_account(self):
        return self._acnt
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance
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
            if amount < 0:
                raise ValueError("The payment amount must be positive")
            else:
               self._balance -= amount
        else:
            raise TypeError("The payment amount must be a number")
        
    

furat = CreditCard("Furat","JordanBank",10500,90)
print(furat.charge(50)) #True
# print(furat.make_payment("30")) #TypeErorr
# print(furat.make_payment(-10)) #ValueErorr




