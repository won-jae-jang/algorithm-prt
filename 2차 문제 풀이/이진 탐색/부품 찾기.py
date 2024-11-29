import sys

input = sys.stdin.readline
n = int(input())
items = list(map(int, input().split()))
m = int(input())
requests = list(map(int, input().split()))
items.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

for req in requests:
    if binary_search(items, req, 0, n - 1) == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')