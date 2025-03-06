array = [1,2,3,4,5]

def binary_search1(start, end, target):

    if start > end:
        return None
    
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search1(start, mid - 1, target)
    else:
        return binary_search1(mid + 1, end, target)
    
# print(binary_search1(0, 4, 3))

def binary_search(start, end, target):

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

print(binary_search(0, 4, 3))