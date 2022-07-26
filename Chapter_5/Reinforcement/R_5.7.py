'''
Let A be an array of size n ≥ 2 containing integers from 1 to n-1, inclusive,
with exactly one repeated. Describe a fast algorithm for finding the
integer in A that is repeated.
'''


def repeated(seq):
    seq.sort()
    last = None
    for i in seq:
        if i == last:
            return last
        last = i


print(repeated([1, 4, 5, 6, 8, 9, 10, 11, 8, 20]))
