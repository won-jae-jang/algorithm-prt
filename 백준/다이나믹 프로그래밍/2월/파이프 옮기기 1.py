n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
#dp[가로, 대각선, 세로][n][n]
dp = [[[0] * n for _ in range(n)] for _ in range(3)]

#1열은 모두 1
dp[0][0][1] = 1
for i in range(2, n):
    if board[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]

for i in range(1, n):
    for j in range(1, n):

        if board[i][j] == 1:
            continue

        #대각선
        if board[i - 1][j] == 0 and board[i][j - 1] == 0:
            dp[1][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]

        #가로
        dp[0][i][j] = dp[0][i][j - 1] + dp[1][i][j - 1] 
        #세로
        dp[2][i][j] = dp[2][i - 1][j] + dp[1][i - 1][j]

result = 0
for i in range(3):
    result += dp[i][n - 1][n - 1]

print(result)