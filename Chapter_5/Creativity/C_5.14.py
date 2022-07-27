'''
The shuffle method, supported by the random module, takes a Python
list and rearranges it so that every possible ordering is equally likely.
Implement your own version of such a function. You may rely on the
randrange(n) function of the random module, which returns a random
number between 0 and n-1 inclusive.
'''

import random


def shuffle(seq):
    index1 = random.randrange(len(seq))
    index2 = random.randrange(len(seq))
    seq[index1], seq[index2] = seq[index2], seq[index1]


seq = [1, 2, 3, 7]
for _ in range(len(seq)):
    shuffle(seq)
    print(seq)
