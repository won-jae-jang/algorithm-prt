n = int(input())
t = []
p = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

d = [0] * (n + 1)
max_value = 0
for i in range(n - 1, -1, - 1):
    date = i + t[i]
    if date <= n:
        d[i] = max(p[i] + d[date], max_value)
        max_value = max(max_value, d[i])
    else:
        d[i] = max_value
print(max(d))