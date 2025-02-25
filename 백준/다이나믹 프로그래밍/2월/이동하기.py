n , m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]
dp[0][0] = board[0][0]

for i in range(n):
    for j in range(m):
        if i != n - 1:
            dp[i + 1][j] = max(dp[i + 1][j], board[i + 1][j] + dp[i][j])
        if j != m - 1:
            dp[i][j + 1] = max(dp[i][j + 1], board[i][j + 1] + dp[i][j])
        if i != n - 1 and j != m - 1:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], board[i + 1][j + 1] + dp[i][j])

print(dp[n - 1][m - 1])