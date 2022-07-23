'''
Suppose you are given an n-element sequence, S, containing distinct integers 
that are listed in increasing order. Given a number k, describe a
recursive algorithm to ﬁnd two integers in S that sum to k, if such a pair
exists. What is the running time of your algorithm?
'''


def sum_equal(seq, k):
    if seq == []:
        return None
    else:
        for i in range(1, len(seq)):
            if seq[0] + seq[i] == k:
                return (seq[0], seq[i])
        return sum_equal(seq[1:], k)


print(sum_equal([1, 6, 8, 9, 4, 0, 4], 19))
# O(n^2)
