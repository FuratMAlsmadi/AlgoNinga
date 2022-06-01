"""
Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.
"""



def log_two(num):
    count = 0
    dividend = num
    while dividend >= 2:
        count += 1
        dividend = dividend//2
    return count
    
    


test = log_two(16)
print(test)