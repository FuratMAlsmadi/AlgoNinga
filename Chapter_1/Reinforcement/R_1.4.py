"""Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n."""

def sum_lesspos(n):
    sum = 0
    for i in range(n):
        sum += (i*i)
    return sum 


print(sum_lesspos(5)) #30