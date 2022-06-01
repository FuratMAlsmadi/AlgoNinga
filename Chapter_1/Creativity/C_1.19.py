"""
Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally.
"""

import string

_list = [i for i in string.ascii_lowercase]
print(_list)

_list_2 = [chr(i) for i in  range(ord('a'),ord('a')+26)]
print(_list_2)
