n = int(input())
dp = [[0] * 3 for _ in range(n)]

for i in range(n):
    a, b, c = map(int, input().split())
    dp[i][0], dp[i][1], dp[i][2] = a, b, c

for i in range(1, n):

    dp[i][0] = dp[i][0] + min(dp[i - 1][1], dp[i - 1][2]) #i번째 집에서 R로 색칠할 때 최소값
    dp[i][1] = dp[i][1] + min(dp[i - 1][0], dp[i - 1][2]) #i번째 집에서 G로 색칠할 때 최소값
    dp[i][2] = dp[i][2] + min(dp[i - 1][0], dp[i - 1][1]) #i번째 집에서 B로 색칠할 때 최소값

print(min(dp[n - 1]))       