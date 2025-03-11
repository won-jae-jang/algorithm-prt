import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

start = 0
end = n - 1
result = abs(data[start] + data[end])
feature = [data[start], data[end]]

while start < end:

    sum_value = data[start] + data[end]

    if abs(sum_value) <= result:
        result = abs(sum_value)
        feature = [data[start], data[end]]

    if sum_value < 0:
        start += 1
    else:
        end -= 1

print(feature[0], feature[1])