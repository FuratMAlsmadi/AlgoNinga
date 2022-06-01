""" 
Write a Python program that inputs a polynomial in standard algebraic
notation and outputs the first derivative of that polynomial.
"""

# The class polynomial takes a list of tuples as an argument, and has a method derivate that returns
# the derivate of the polynomial
from copy import copy, deepcopy


class polynomial():
    def __init__(self,f):
        self._polynomial = f
        self._derivated = [0]*len(f)
    def derivate(self):
        """
        It takes a polynomial and returns its derivative
        :return: The derivated polynomial
        """
        for index , value in enumerate(self._polynomial):
            a,b = value
            if b != 0:
                self._derivated[index]=(a,b-1)
            else:
                self._derivated[index]=(0,0)
        return self._derivated

    
#[(3,2),(2,1),(2,0)] (coff,degree)
b = polynomial([(3,2),(2,1),(2,0)])
print(b.derivate())
