"""
Modify the declaration of the ﬁrst for loop in the CreditCard tests, from
Code Fragment 2.3, so that it will eventually cause exactly one of the three
credit cards to go over its credit limit. Which credit card is it?
Answer: The first one 
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
        

                        
                        
if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCard( "John Bowman" , "California Savings" ,"5391 0375 9387 5309",2500))
    wallet.append(CreditCard("John Bowman" , "California Federal" ,"3485 0399 3395 1954",3500))
    wallet.append(CreditCard("John Bowman" , "California Finance" ,"5391 0375 9387 5309",5000))
    
    for val in range(1,17):
        wallet[0].charge(200*val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
        
    for c in range(3):
        print("Customer = ",wallet[c].get_customer())
        print("Bank = ", wallet[c].get_bank())
        print("Account = ",wallet[c].get_account())
        print("Limit = ", wallet[c].get_limit())
        print("Balance = ", wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print("New Balance = ", wallet[c].get_balance())
        print("########################")
            
        
        