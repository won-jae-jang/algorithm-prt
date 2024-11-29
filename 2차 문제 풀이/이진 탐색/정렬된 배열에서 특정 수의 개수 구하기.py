import sys

input = sys.stdin.readline
n, x = map(int, input().split())
data = list(map(int, input().split()))

def binary_search(data, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        print('start, end, mid: ', start, end, mid)
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

count = 0
while True:
    print(data, x, 0, n)
    result = binary_search(data, x, 0, n)
    if result != None:
        count += 1
        n -= 1
        del data[result]
    else:
        break

if count != 0:
    print(count)
else:
    print(-1)