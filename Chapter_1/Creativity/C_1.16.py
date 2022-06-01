"""
In our implementation of the scale function (page 25), the body of the loop
executes the command data[j] = factor. We have discussed that numeric
types are immutable, and that use of the = operator in this context causes
the creation of a new instance (not the mutation of an existing instance).
How is it still possible, then, that our implementation of scale changes the
actual parameter sent by the caller?
"""
def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor

list1 = [1,2,3,4,5]
scale(list1,2)
print(list1)

"""
The formal parameter in not a copy of the actual parameter;
the formal parameter refers to the actual parameter,and because we sent an array(list) to the function
So every particular element in the list is changing as we assign it to a new numeric object.
"""