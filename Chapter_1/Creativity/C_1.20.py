"""
Python’s random module includes a function shuﬄe(data) that accepts a
list of elements and randomly reorders the elements so that each possi-
ble order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuﬄe function.
"""

from random import randint


def my_shuffle(data):
    length_data =len(data)
    list_shuffled = []
    while True :
        if len(list_shuffled) == len(data):
            break
        _index = randint(0,(length_data-1))
        if data[_index] in list_shuffled:
            _index = randint(0,(length_data-1))
            continue
        else:
            list_shuffled.append(data[_index])
            
    return list_shuffled
        
        

_list= [1,2,3,4,5,6]
print(my_shuffle(_list))
