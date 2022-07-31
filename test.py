# import random


# def shuffle(seq):
#     index1 = random.randrange(len(seq))
#     index2 = random.randrange(len(seq))
#     seq[index1], seq[index2] = seq[index2], seq[index1]


# seq = [1, 2, 3, 7]
# shuffle(seq)
# print(seq)

from cmath import log


def gen_list(n):
    list = [0]*n
    for i in range(n):
        list[i] = log(i,2)+ 1
    return list


print(gen_list(7))