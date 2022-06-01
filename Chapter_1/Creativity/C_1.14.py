"""Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd"""

def is_odd_multiple(seq):
    for i in seq:
        for k in seq:
            if (i*k)%2 != 0:
                return True
            else:
                return False
            
            
            
list1 = [2,4,6,8]
print(is_odd_multiple(list1))  #False 

list2 = [1.2,6,5]
print(is_odd_multiple(list2)) #True