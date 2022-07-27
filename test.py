import random


def shuffle(seq):
    index1 = random.randrange(len(seq))
    index2 = random.randrange(len(seq))
    seq[index1], seq[index2] = seq[index2], seq[index1]


seq = [1, 2, 3, 7]
shuffle(seq)
print(seq)
