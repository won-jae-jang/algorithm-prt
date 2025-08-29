n = int(input())
arr = list(map(int, input().split()))
target = arr[-1]
dp = [[0] * 21 for _ in range(n - 1)]
dp[0][arr[0]] = 1

for i in range(1, n - 1):
    num = arr[i] #더하거나 빼줄 숫자
    for j in range(21):
        # +- 대상이 되는 수인 경우
        if dp[i - 1][j] >= 1:
            plus = j + num
            minus = j - num
            if plus <= 20: dp[i][plus] += dp[i - 1][j]
            if 0 <= minus: dp[i][minus] += dp[i - 1][j]

print(dp[-1][target])