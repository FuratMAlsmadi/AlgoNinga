'''
Let B be an array of size n ≥ 6 containing integers from 1 to n-5, inclusive, 
with exactly ﬁve repeated. Describe a good algorithm for finding the ﬁve 
integers in B that are repeated.
'''

def is_repeated(seq):
    temp = [0]*len(seq)
    for i in range(len(seq)):
        temp[seq[i]] += 1
    repeated = []
    for i in range(len(seq)):
        if temp[seq[i]] > 1:
            repeated.append(seq[i])
    return repeated
               

seq = [1,1,4,5,4,2,3,2,6,7,6,7]
print(set(is_repeated(seq)))
#Running time O(n)
#space O(n)