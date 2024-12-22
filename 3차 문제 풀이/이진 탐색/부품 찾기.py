import sys

input = sys.stdin.readline

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

n = int(input())
stock = list(map(int, input().split()))
m = int(input())
request = list(map(int, input().split()))

stock.sort()
for x in request:
    if binary_search(stock, x, 0, n - 1):
        print('yes', end=' ')
    else:
        print('no', end=' ')