n = int(input())
INF = 1e10
dp = [INF] * (n + 1) #dp table
dp[1] = 0

for i in range(1, n):
    if dp[i] == INF:
        continue
    #1을 더하기
    dp[i + 1] = min(dp[i + 1], dp[i] + 1)
    #2를 곱하기
    if i * 2 <= n:
        dp[i * 2] = min(dp[i * 2], dp[i] + 1)
    #3을 곱하기
    if i * 3 <= n:
        dp[i * 3] = min(dp[i * 3], dp[i] + 1)

print(dp[n])