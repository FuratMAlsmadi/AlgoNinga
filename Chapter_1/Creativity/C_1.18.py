"""
Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
"""

_list= [i*(i+1) for i in range(0,10)]
print(_list)

