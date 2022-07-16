'''
Isabel has an interesting way of summing up the values in a sequence A of
n integers, where n is a power of two. She creates a new sequence B of half
the size of A and sets B[i] = A[2i] + A[2i + 1], for i = 0, 1, . . . , (n/2) − 1. If
B has size 1, then she outputs B[0]. Otherwise, she replaces A with B, and
repeats the process. What is the running time of her algorithm?
'''
def sum_isabel(nums_list):
    if len(nums_list) == 1:
        return nums_list[0]
    else:
        sum_list = [0]*(len(nums_list)//2)
        for i in range(0,len(nums_list)//2):
            sum_list[i] = nums_list[2*i] + nums_list[2*i+1]
        return sum_isabel(sum_list)   
        
        
        
print(sum_isabel([1,2,3,4,5]))
#the running time of this is O(n^2)