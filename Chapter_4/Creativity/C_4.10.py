'''
Describe a recursive algorithm to compute the integer part of the base-two
logarithm of n using only addition and integer division.
'''
def log(num,acc=0):
    if num == 1:
        return acc
    else:
        return log(num//2,acc+1)
        
        
        
print(log(10))