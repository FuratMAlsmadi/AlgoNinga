"""Give a single command that computes the sum from Exercise R-1.6, rely-
ing on Python’s comprehension syntax and the built-in sum function."""

n = 5 #or int(input())
sum_lessodd = sum([i*i for i in range(n) if i%2 != 0])

print(sum_lessodd)