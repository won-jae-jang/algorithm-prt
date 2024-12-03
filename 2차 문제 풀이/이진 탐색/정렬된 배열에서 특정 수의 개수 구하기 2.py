import sys

def count_by_range(array, x):
    n = len(array)
    a = first(array, x, 0, n - 1)
    if a == None:
        return 0
    
    b = last(array, x, 0, n - 1)
    return b - a + 1

def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    #찾는 값중에서 가장 왼쪽에 있는 경우
    if (mid == 0 or array[mid - 1] < target) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    else:
        return first(array, target, mid + 1, end)
    
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    #찾는 값이 가장 오른쪽에 위치한 경우
    if (mid == n - 1 or array[mid + 1] > target) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    else:
        return last(array, target, mid + 1, end)

input = sys.stdin.readline
n, x = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = count_by_range(data, x)
if result == 0:
    print(-1)
else:
    print(result)