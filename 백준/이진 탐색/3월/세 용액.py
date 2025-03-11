import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()
result = abs(data[0] + data[n - 1] + data[(n - 1) // 2])
feature = [data[0], data[(n - 1) // 2], data[n - 1]]

for mid in range(1, n - 1):
    start = 0
    end = n - 1

    while start < mid < end:

        sum_value = data[start] + data[mid] + data[end]
        if abs(sum_value) < result:
            result = abs(sum_value)
            feature = [data[start], data[mid], data[end]]
            if result == 0:
                break

        if sum_value < 0:
            start += 1
        else:
            end -= 1

print(feature[0], feature[1], feature[2])