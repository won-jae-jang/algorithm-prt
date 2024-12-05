n = int(input())
t = []
p = []
d = [0] * (n + 1)
for i in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

max_value = 0
#i는 현재 일짜
for i in range(n - 1, -1, -1):
    time = i + t[i]
    if time <= n:
        d[i] = max(p[i] + d[time], max_value)
        max_value = d[i]
    else:
        d[i] = max_value

print(max_value)