'''
Describe how the built-in sum function can be combined with Python's
comprehension syntax to compute the sum of all numbers in an n*n data
set, represented as a list of lists.
'''

matrix = [[1, 2, 3, 4], [1, 4, 5, 6]]
print(sum([sum(i) for i in matrix]))
