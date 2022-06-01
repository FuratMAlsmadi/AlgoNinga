"""
Write a Python program that inputs a list of words, separated by white-
space, and outputs how many times each word appears in the list. You
need not worry about efﬁciency at this point, however, as this topic is
something that will be addressed later in this book.
"""

def my_list():
    items = []
    item_input = input("Write your list here-> ")
    items = item_input.split()
    return items


def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def count(list,item):
    count = 0
    for i in list:
        if i == item:
            count +=1
    return count

def how_many():
    _list = my_list()
    second_list = _list.copy()
    for i in second_list:
        if i in _list:
            print("{}-{}".format(count(_list,i),i))
            _list = remove_values_from_list(_list,i)
    
        
        
        
        
        
how_many()
        



        
     