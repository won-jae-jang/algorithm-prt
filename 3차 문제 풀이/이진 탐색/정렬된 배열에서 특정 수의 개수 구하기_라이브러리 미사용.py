import sys

def left(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        #target 값과 동일하고 맨 왼쪽에 있는 경우
        if array[mid] == target and ((array[mid] > array[mid - 1]) or mid == 0):
            return mid
        elif array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return None

def right(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        #target 값과 동일하고 맨 오른쪽에 있는 경우
        if array[mid] == target and ((array[mid] < array[mid + 1]) or mid == n - 1):
            return mid
        elif array[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1            

    return None

input = sys.stdin.readline
n, x = map(int, input().split())
array = list(map(int, input().split()))

left_index = left(array, x, 0, n - 1)
right_index = right(array, x, 0, n - 1)

if left_index == None or right_index == None:
    print(-1)
else:
    print(right_index - left_index + 1)