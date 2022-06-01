"""
Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible.
"""
def change_make(charged,given):
    if charged > given:
        print("insufficient balance")
        return
    else:
        bill = (given-charged)*100
        q = int(bill//25) #quarters
        bill = bill%25
        d = int(bill//10) #dimes
        bill = bill%10
        n = int(bill//5) #neckles
        bill = bill%5
        p = int(bill//1) #pennies
        return f"""
    TOTAL AMOUNT :{charged}
    CASH :{given}
    CHANGE :{q} quarter,{d} dimes,{n} neckles and {p} pennie    
    """
    
    
    
    
print(change_make(1.70,2))