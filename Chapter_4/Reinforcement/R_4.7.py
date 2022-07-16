'''
Describe a recursive function for converting a string of digits into the integer it represents. 
For example, 13531 represents the integer 13,531
'''
def to_int(s,n=0):
    if len(s) == 1:
        return 10**(n) * int(s)
    else:
        return 10**(n) * int(s[len(s)-1]) + to_int(s[:-1],n+1)
        
        
        
        
print(to_int("13531"))
