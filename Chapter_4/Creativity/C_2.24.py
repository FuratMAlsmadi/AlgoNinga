'''
Develop a non-recursive implementation of the version of power from
Code Fragment 4.12 that uses repeated squaring.
'''


def pow(base, exp):
    result = 1
    for i in range(0, exp):
        result = result*base
    return result


print(pow(2, 2))
