"""
Exercise R-2.12 uses the mul method to support multiplying a Vector
by a number, while Exercise R-2.14 uses the mul method to support
computing a dot product of two vectors. Give a single implementation of
Vector. mul that uses run-time type checking to support both syntaxes
u*v and u*k, where u and v designate vector instances and k represents
a number.
"""
# The class Vector is a class that represents a vector in a vector space.
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
            raise ValueError("dimensions must agree")
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
            raise ValueError("dimensions must agree")
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
        if not isinstance(other,(int,float,Vector,list)):
            return ValueError("Factor Must Be A Number or A Vector")
        if isinstance(other,Vector):
            if len(self) != len(other):
                return ValueError("dimensions must agree")
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