'''
Write a short recursive Python function that finds the minimum and maximum values
in a sequence without using any loops.
'''


def find_max(seq):
    if len(seq) == 1:
        return seq[0]
    if seq[0] < seq[1]:
        return find_max(seq[1:])
    elif seq[0] > seq[1]:
        seq[1] = seq[0]
        return find_max(seq[1:])


def find_min(seq):
    if len(seq) == 1:
        return seq[0]
    if seq[0] > seq[1]:
        return find_min(seq[1:])
    elif seq[0] < seq[1]:
        seq[1] = seq[0]
        return find_min(seq[1:])


print(find_max([1, 3, 4, 16, 19, 6, 7]))
print(find_min([1, 3, 4, 16, 19, 6, 0, 7]))
