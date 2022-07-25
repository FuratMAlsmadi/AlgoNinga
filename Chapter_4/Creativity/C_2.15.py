'''
Write a recursive function that will output all the subsets of a set of n
elements (without repeating any subsets).
'''


def subset(rest, sofar=[]):
    if rest == []:
        print(sofar)
    else:
        subset(rest[1:], sofar + [rest[0]])
        subset(rest[1:], sofar)


subset([1, 2, 3, 4])
