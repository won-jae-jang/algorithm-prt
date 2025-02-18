import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]
    #bottom up
    for i in range(1, n):
        dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] + dp[0][i])
        dp[1][i] = max(dp[1][i - 1], dp[0][i - 1] + dp[1][i])

    print(max(dp[0][n - 1], dp[1][n - 1]))