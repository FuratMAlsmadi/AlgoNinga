
def binary_search(data, target, low, high):
    if low > high:
        print("Not Found")
    else:
        median = (low+high)//2
        if data[median] == target:
            print("found")
        elif target > data[median]:
            binary_search(data, target, median+1, high)
        elif target < data[median]:
            binary_search(data, target, low, median-1)


# A = [1, 2, 3, 4, 5, 8, 9, 10, 15, 20]
# binary_search(A, 16, 0, len(A))
# binary_search(A, 0, 0, len(A))
# binary_search(A, 5, 0, len(A))
# binary_search(A, 15, 0, len(A))


def binary_find(arr,target,low,high):
    if low > high:
        return False
    else:
        med  = (low+high)//2
        if arr[med] == target:
            return True 
        elif arr[med] > target:
            return binary_find(arr,target,low,med-1)
        elif arr[med] < target:
            return binary_find(arr,target,med-1,high)
        
        
        
A = [1, 2, 3, 4, 5, 8, 9, 10, 15, 20]
binary_search(A, 16, 0, len(A))
print(binary_find(A, 0, 0, len(A)))
binary_search(A, 5, 0, len(A))
print(binary_find(A, 15, 0, len(A)))