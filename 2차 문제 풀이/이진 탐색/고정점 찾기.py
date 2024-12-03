import sys

def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return None

input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))

result = binary_search(array, 0, n - 1)
if result == None:
    print(-1)
else:
    print(result)