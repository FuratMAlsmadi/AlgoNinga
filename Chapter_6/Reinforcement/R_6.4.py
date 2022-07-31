'''
Give a recursive method for removing all the elements from a stack.
'''


def remove_all(S):
    if len(S) == 0:
        return
    S.pop()
    remove_all(S)


S = [1, 2, 3, 4, 5]
remove_all(S)
print(S)
