"""
A common punishment for school children is to write out a sentence mul-
tiple times. Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos.
"""
import random
import string

def punishment():
    _list = ["I well never spam my friends again.","I will naver spam my friends again.",
             "I will never spim my friends again.","I will never spam my freinds again.",
             "I will never spam my friends agaen.","I will never spam my friendc again.",
             "I will never spam my firends again.","I will never spem my friends again."]
    for i in range(9,101):
        _list.append("I will never spam my friends again.")
        
    random.shuffle(_list)
    count   = 1
    for i in _list:
        print("{}-{}".format(count,i))
        count += 1
                
        
              
        
        
punishment()
