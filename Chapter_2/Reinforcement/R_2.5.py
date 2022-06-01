"""
Use the techniques of Section 1.7 to revise the charge and make payment
methods of the CreditCard class to ensure that the caller sends a number
as a parameter.
"""


class CritedCard():
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
        
    

furat = CritedCard("Furat","JordanBank",10500,90)
print(furat.charge(50)) #True
# print(furat.make_payment("30")) #TypeErorr



