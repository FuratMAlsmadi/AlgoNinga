'''
Given an unsorted sequence, S, of integers and an integer k, describe a
recursive algorithm for rearranging the elements in S so that all elements
less than or equal to k come before any elements larger than k. What is
the running time of your algorithm on a sequence of n values?
'''


def binary_sort(seq, k, smaller=[], bigger=[]):
    if seq == []:
        return smaller+bigger
    else:
        if seq[0] <= k:
            smaller.append(seq[0])
            return binary_sort(seq[1:], k, smaller, bigger)
        else:
            bigger.append(seq[0])
            return binary_sort(seq[1:], k, smaller, bigger)


seq = [1, 7, 8, 9, 3, 0, 2]
print(binary_sort(seq, 4))
# O(n)
