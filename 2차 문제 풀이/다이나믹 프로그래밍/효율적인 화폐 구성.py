n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0
for k in array:
    for i in range(k, m + 1):
        d[i] = min(d[i], d[i - k] + 1)

if d[m] >= 10001:
    print(-1)
else:
    print(d[m])