'''
The syntax data.remove(value) for Python list data removes only the first
occurrence of element value from the list. Give an implementation of a
function, with signature remove all(data, value), that removes all occurrences 
of value from the given list, such that the worst-case running time
of the function is O(n) on a list with n elements. Not that it is not efficient
enough in general to rely on repeated calls to remove
'''


# def remove_all(seq,target):
#     try:
#         while True:
#             seq.remove(target)
#     except:
#         pass

def remove_all(seq, target):
    return [i for i in seq if i != target]


seq = [1, 3, 6, 7, 9, 1, 5, 9]
seq = remove_all(seq, 1)
print(seq)
