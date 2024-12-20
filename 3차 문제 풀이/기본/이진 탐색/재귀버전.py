def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)
    
#원소의 개수, 찾고자하는 값
n, target = 10, 7
#전체 원소
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

result = binary_search(array, target, 0, n - 1)
if result == None:
    print('찾고자하는 원소 존재 X')
else:
    #실행결과: 4 번째 위치
    print(result + 1, '번째 위치')