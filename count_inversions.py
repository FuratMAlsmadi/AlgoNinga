def merge(left,right,arr):
    i = 0
    j = 0
    k= 0
    invcount = 0
    while i< len(left) and j<len(right):
        if left[i] <= right[j] :
            arr[k]=left[i]
            i += 1
        elif right[j] <= left[i]:
            arr[k]=right[j] 
            invcount += (len(left)-i) 
            j += 1
        k += 1
    while i< len(left):
        arr[k]=left[i]
        i +=1 
        k += 1
    while j < len(right):
        arr[k]=right[j]
        j += 1
        k += 1 
    return invcount

    


def merge_sort(arr):
    if len(arr) == 1: return 0
    invercount = 0
    n = len(arr)
    left = arr[:n//2]
    right = arr[n//2:]
    invercount += merge_sort(left)
    invercount += merge_sort(right)
    invercount += merge(left,right,arr)
    return invercount



with open("test.txt") as file:
    lines = file.readlines()
    lines = list(map(int, lines))
    print(merge_sort(lines))
    