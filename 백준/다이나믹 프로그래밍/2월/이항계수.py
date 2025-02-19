n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]

#nC0, nCn 은 모두 1
for i in range(1, n + 1):
    for j in range(k + 1):
        if j == 0:
            dp[i][j] = 1
        elif i == j:
            dp[i][j] = 1

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if i == j:
            continue
        dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % 10007

print(dp[n][k])