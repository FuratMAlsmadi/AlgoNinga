'''
Use standard control structures to compute the sum of all numbers in an
n*n data set, represented as a list of lists.
'''


def matrix_sum(matrix):
    sum = 0
    for i in matrix:
        for j in i:
            sum += j
    return sum


matrix = [[1, 2, 3, 4], [1, 4, 5, 6]]
print(matrix_sum(matrix))
