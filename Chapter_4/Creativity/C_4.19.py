'''
Write a short recursive Python function that rearranges a sequence of integer 
values so that all the even values appear before all the odd values.
'''


def even_before_odd(seq, even=[], odd=[]):
    if seq == []:
        return even+odd
    else:
        if seq[0] % 2 == 0:
            even = even + [seq[0]]
            return even_before_odd(seq[1:], even, odd)
        else:
            odd = odd + [seq[0]]
            return even_before_odd(seq[1:], even, odd)


print(even_before_odd([1, 2, 5, 6, 8, 3]))
