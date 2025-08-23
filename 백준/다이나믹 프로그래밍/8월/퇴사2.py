N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)

for i in range(N):
    t, p = data[i][0], data[i][1]
    dp[i + 1] = max(dp[i + 1], dp[i])
    date = i + t #상담이 마감되는 날짜
    #현재 상담을 진행할 수 있는 경우
    if date <= N:
        dp[date] = max(dp[date], dp[i] + p)

print(dp[-1])