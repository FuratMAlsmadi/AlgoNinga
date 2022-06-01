"""Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n."""

def sum_lessodd(n):
    sum = 0
    for i in range(n):
        if i%2 != 0:
            sum += (i*i)
    return sum 


print(sum_lessodd(5)) #10