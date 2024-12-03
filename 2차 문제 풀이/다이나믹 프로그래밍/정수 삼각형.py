n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(dp[i])):
        #해당층에서 가장 왼쪽에 위치
        if j == 0:
            left = 0
        else:
            left = dp[i - 1][j - 1]
        #해당 층에서 가장 오른쪽에 위치해 있는 경우
        if j == len(dp[i]) - 1:
            right = 0
        else:
            right = dp[i - 1][j]

        dp[i][j] += max(left, right)

print(max(dp[n - 1]))