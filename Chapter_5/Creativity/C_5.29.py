'''
useful operation in databases is the natural join. If we view a database
as a list of ordered pairs of objects, then the natural join of databases A
and B is the list of all ordered triples (x, y, z) such that the pair (x, y) is in
A and the pair (y, z) is in B. Describe and analyze an efficient algorithm
for computing the natural join of a list A of n pairs and a list B of m pairs.
'''
from copy import deepcopy


def join(seq_1, seq_2):
    if len(seq_1) > len(seq_2):
        temp = deepcopy(seq_1)
        for i in seq_2:
            if i in seq_1:
                pass
            else:
                temp.append(i)
        return temp
    else:
        if len(seq_1) < len(seq_2):
            temp_2 = deepcopy(seq_2)
            for i in seq_1:
                if i in seq_2:
                    pass
                else:
                    temp_2.append(i)
            return temp_2


seq_1 = [1, 2, 3, 5]
seq_2 = [2, 6]
print(seq_1)
print(join(seq_1, seq_2))
