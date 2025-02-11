n = int(input())
data = [0]

for i in range(n):
    data.append(int(input()))

dp = [0] * (n + 1)

#계단이 2층 이하인 경우
if n <= 2:
    print(sum(data))
#계단이 3층 이상인 경우
else:
    dp[1] = data[1]
    dp[2] = data[2] + data[1]

    for i in range(3, n + 1):
        dp[i] = max(data[i - 1] + dp[i - 3], dp[i - 2]) + data[i]

    print(dp[n])
      