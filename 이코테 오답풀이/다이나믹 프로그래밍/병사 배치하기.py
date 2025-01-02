n = int(input())
array = list(map(int, input().split()))

array.reverse()
d = [1] * (n + 1)
for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            d[i] = max(d[i], d[j] + 1)

print(n - max(d))