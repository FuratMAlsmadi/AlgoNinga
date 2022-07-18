'''
Describe an efficient recursive function for solving the element unique-
ness problem, which runs in time that is at most O(n 2 ) in the worst case
without using sorting.
'''
def is_unique(seq):
    if len(seq) == 0:
        return True
    else:
        for i in range(1,len(seq)):
            if seq[0] == seq[i]:
                return False
        return is_unique(seq[1:])
        
        
        
print(is_unique([1,2,3,1,5]))