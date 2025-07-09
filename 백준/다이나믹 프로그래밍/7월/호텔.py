c, n = map(int, input().split())
data = list(list(map(int, input().split())) for _ in range(n))
INF = 1e10
dp = [INF] * (c + 101)
dp[0] = 0

for cost, gain in data:
    for i in range(gain, c + 101):
        dp[i] = min(dp[i], dp[i - gain] + cost)

print(min(dp[c:]))