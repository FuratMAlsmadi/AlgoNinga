"""Give a single command that computes the sum from Exercise R-1.4, rely-
ing on Python’s comprehension syntax and the built-in sum function."""
n = 5 #or int(input())
sum_lesspos = sum([i*i for i in range(n)])

print(sum_lesspos)