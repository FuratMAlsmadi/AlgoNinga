import random


def partition(arr,start,end):
    pivot = arr[end]
    p_index = start
    for i in range(start,end):
        if arr[i] <= pivot:
            arr[p_index] , arr[i] = arr[i] , arr[p_index]
            p_index += 1
    arr[p_index] , arr[end] = arr[end] , arr[p_index]
    return p_index 

def randomize_partition(arr,start,end):
    pivot_index = random.randint(start,end)
    arr[-1],arr[pivot_index] = arr[pivot_index],arr[-1]
    return partition(arr,start,end)

def quick_sort(arr,start,end):
    if start < end :
        p_index = randomize_partition(arr,start,end)
        quick_sort(arr,start,p_index-1)
        quick_sort(arr,p_index+1,end)




list = [4,5,1,4,7,8,3,2]
quick_sort(list,0,len(list)-1)
print(list)