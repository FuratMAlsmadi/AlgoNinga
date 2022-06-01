"""Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct)."""

def is_duplicate_free(seq):
    len1 = len(seq)
    len2 = len(list(set(seq)))
    if len1 == len2 :
        return True
    else:
        return False


str1 = "Fuurat"
print(is_duplicate_free(str1)) #False

list1 = [1,2,3,4,5,6]
print(is_duplicate_free(list1)) #True

tuple1 = (1,4,4,6,7)

