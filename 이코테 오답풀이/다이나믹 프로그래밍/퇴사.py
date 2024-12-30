n = int(input())
t = []
p = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

dp = [0] * (n + 1)
max_value = 0
for i in range(n - 1, -1, -1):
    date = i + t[i]
    if date > n:
        dp[i] = max_value
    else:
        dp[i] = max(p[i] + dp[date], max_value)
        max_value = max(max_value, dp[i])

print(max_value)