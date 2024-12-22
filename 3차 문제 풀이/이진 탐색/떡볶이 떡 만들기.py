import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

start = 0
end = int(1e10)
result = 0
#binary search
while start <= end:
    height = (start + end) // 2
    sum_value = 0
    #특정 높이로 잘랐을 때, 잘린 떡의 길이의 총합
    for i in range(n):
        if height < data[i]:
            sum_value += (data[i] - height)
    #떡의 높이 조정정
    if sum_value >= m:
        result = height
        start = height + 1
    else:
        end = height - 1

print(result)
