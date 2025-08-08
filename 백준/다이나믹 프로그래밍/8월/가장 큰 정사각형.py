n, m = map(int, input().split())
data = []
dp = [[0] * m for _ in range(n)]
for i in range(n):
    temp = list(input())
    data.append(temp)
    for j in range(m):
        if temp[j] == '1':
            dp[i][j] = 1

for i in range(1, n):
    for j in range(1, m):
        if dp[i][j] == 1:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

row = 0
for i in range(n):
    row = max(row, max(dp[i]))

print(row ** 2)
