"""Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing."""
#Define a function called reverse_1(class 'list')
#creat an new empty list 
#loop through the original list from the end [-1] and start filling the new one
#return the new list 
def reverse_l(arr):
    arr2 = list()
    for i in range(1,len(arr)+1):
        i = -i
        arr2.append(arr[i])
    return arr2



list1 = [1,2,3,4,5]
print(reverse_l(list1))
'''
There are three different built-in ways to reverse a list. Which method is best depends on whether you need to:
1.Reverse an existing list in-place (altering the original list variable)
        Best solution is object.reverse() method
2.Create an iterator of the reversed list (because you are going to feed it to a for-loop, a generator, etc.)
        Best solution is reversed(object) which creates the iterator
3.Create a copy of the list, just in the reverse order (to preserve the original list)
        Best solution is using slices with a -1 step size: object[::-1]
'''
    