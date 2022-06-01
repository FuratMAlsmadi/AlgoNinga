"""
Write a Python class, Flower, that has three instance variables of type str,
int, and ﬂoat, that respectively represent the name of the ﬂower, its num-
ber of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.
"""

class Flower:
    def __init__(self,name,number,price):
        if(isinstance(name,str) and isinstance(number,int) and isinstance(price,float)):
            self._flower_name = name
            self._number_of_petals = number
            self._price = price
        else:
            raise ValueError
    def set_name(self,name):
        self._flower_name = name
    def get_name(self):
        return self._flower_name
    def set_petals_number(self,number):
        self._number_of_petals = number
    def get_petals_number(self):
        return self._number_of_petals
    def set_price(self,price):
        self._price = price
    def get_price(self):
        return self._price
    
    
    
jouri = Flower("Jouri",4,0.30)

print(jouri.get_name(),jouri.get_petals_number())

# yasmin = Flower("Yasmin",2.2,60) #valuerror

yasmin = Flower("Yasmin",2,1.0) 
yasmin.set_petals_number(3)
print(yasmin.get_petals_number())

