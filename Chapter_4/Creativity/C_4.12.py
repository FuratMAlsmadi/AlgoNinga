'''
Give a recursive algorithm to compute the product of two positive integers,
m and n, using only addition and subtraction.
'''
def product(n,m,acc=0):
    if m == 0:
        return acc
    else:
        return product(n,m-1,acc+n)
        
        
        
print(product(2,3))