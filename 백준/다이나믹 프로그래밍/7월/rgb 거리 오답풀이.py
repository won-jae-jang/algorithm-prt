n = int(input())
cost = list(list(map(int, input().split())) for _ in range(n))

INF = 1e10
dp = [[INF] * 3 for _ in range(n)]
# print(cost)
dp[0][0], dp[0][1], dp[0][2] = cost[0][0], cost[0][1], cost[0][2]

for i in range(1, n):
    dp[i][0] = cost[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = cost[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = cost[i][2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[-1]))