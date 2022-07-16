'''
Describe a recursive algorithm for finding the maximum element in a sequence, S, of n elements.
What is your running time and space usage?
'''
def max_recursive(seq, start):
    
    if len(seq) == 1:
        return seq[0]

    if seq[start] <= seq[start + 1]:
        del seq[start]
    
    elif seq[start] > seq[start + 1]:
        del seq[start + 1]
    else:
        return KeyError()
    
    return max_recursive(seq, start)


#running time O(n)
#space usage O(n)