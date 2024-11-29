import sys

input = sys.stdin.readline
n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = 0
start = 0
end = data[-1]    
while start <= end:
    mid = (start + end) // 2
    total = 0
    for x in data:
        if x > mid: 
            total += x - mid
    
    if total == m:
        result = mid
        break
    elif total > m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)