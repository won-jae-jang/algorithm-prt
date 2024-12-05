n = int(input())
array = list(map(int ,input().split()))
array.reverse()

d = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if array[i] > array[j]:
            d[i] = max(d[i], d[j] + 1)

print(n - max(d))