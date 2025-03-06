import sys
input = sys.stdin.readline

k, n = map(int, input().split())
data = [int(input()) for _ in range(k)]
data.sort()

start = 0
end = int(3e9) #30억 > 2^31 - 1
result = 0
while start <= end:
    length = (start + end) // 2 #자를 렌선의 길이
    total = 0

    for x in data:
        total += x // length
    
    if total >= n:
        result = length
        start = length  + 1
    else:
        end = length - 1

print(result)