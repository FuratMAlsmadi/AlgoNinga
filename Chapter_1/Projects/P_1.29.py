"""
Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.
"""


def all_possible_strings(data):
    if len(data) == 1:
        return data
    length_data = len(data)
    new_list = []
    for i in range(length_data):
        first = data[i]
        rdata = data[:i]+data[i+1:]
        for p in all_possible_strings(rdata):
            new_list.append("".join(first+p))
    return new_list 
        
        


test = all_possible_strings(['c' , 'a' , 't' , 'd' , 'o' ,'g'])
print(test)
    
    