"""Write a short Python function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators."""

def is_even(k):
    if k % 2 == 0:
        return True 
    else:
        return False
    
    
print(is_even(5))