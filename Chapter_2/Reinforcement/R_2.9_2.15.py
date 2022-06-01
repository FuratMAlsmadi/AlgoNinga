"""
Implement the sub method for the Vector class of Section 2.3.3, so
that the expression u−v returns a new vector instance representing the
difference between two vectors.

Implement the neg method for the Vector class of Section 2.3.3, so
that the expression −v returns a new vector instance whose coordinates
are all the negated values of the respective coordinates of v.

In Section 2.3.3, we note that our Vector class supports a syntax such as
v = u + [5, 3, 10, −2, 1], in which the sum of a vector and list returns
a new vector. However, the syntax v = [5, 3, 10, −2, 1] + u is illegal.
Explain how the Vector class deﬁnition can be revised so that this syntax
generates a new vector. 
a + b = a.__add__(b)
b + a = b.__add__(a)
so we use __radd__

Implement the mul method for the Vector class of Section 2.3.3, so
that the expression v*3 returns a new vector with coordinates that are 3
times the respective coordinates of v.

Exercise R-2.12 asks for an implementation of mul , for the Vector
class of Section 2.3.3, to provide support for the syntax v 3. Implement
the rmul method, to provide additional support for syntax 3 v.


Implement the mul method for the Vector class of Section 2.3.3, so
that the expression u*v returns a scalar that represents the dot product of
the vectors.

The Vector class of Section 2.3.3 provides a constructor that takes an in-
teger d, and produces a d-dimensional vector with all coordinates equal to
0. Another convenient form for creating a new vector would be to send the
constructor a parameter that is some iterable type representing a sequence
of numbers, and to create a vector with dimension equal to the length of
that sequence and coordinates equal to the sequence values. For example,
Vector([4, 7, 5]) would produce a three-dimensional vector with coordi-
nates <4, 7, 5>. Modify the constructor so that either of these forms is
acceptable; that is, if a single integer is sent, it produces a vector of that
dimension with all zeros, but if a sequence of numbers is provided, it pro-
duces a vector with coordinates based on that sequence.
"""

class Vector():
    def __init__(self,d):
        if isinstance(d,list):
            self._coords = d
        else:
            self._coords = [0]*d
    def __len__(self):
        return len(self._coords)
    def __getitem__(self,j):
        return self._coords[j]
    def __setitem__(self,j,val):
        self._coords[j] = val
    def __add__(self,other):
        if len(self) != len(other):
            raise ValueError("Dimentions must agree")
        result  = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self,other):
        return self._coords == other._coords
    def __ne__(self,other):
        return not self == other
    def __str__(self):
        return '<' +str(self._coords)[1:-1]+'>'
    def __sub__(self,other):
        if len(self) != len(other):
            raise ValueError("Dimentions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result
    def __radd__(self,other):
        return self+other
    def __mul__(self,other):
        if isinstance(other,Vector) and len(self) == len(other):
            sum = 0 #to sum all the products 
            for i in range(len(self)):
                sum += (self[i]*other[i])
            return sum 
        else:
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i]*other
            return result
    def __rmul__(self,other):
        return self*other
    
    
v = Vector(3)
v[0] = 59
v[1] = 32
v[2] = 11
v2 = Vector(3)
v2[0] = 5
v2[1] = 31
v2[2] = 18
v3 = v-v2
print(v3)
print(-v)

print(Vector([2,3,4])+v)
        
        
    
        