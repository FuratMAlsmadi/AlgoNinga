"""
Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . , n − 1.
"""


def dot_product(arr_1,arr_2):
    if len(arr_1) != len(arr_2):
        raise ValueError("Both parameters need to be of the same lenght!")
    for i in range(len(arr_1)):
        yield arr_1[i]*arr_2[i]


print(list(dot_product([2,3,4],[4,2,1])))