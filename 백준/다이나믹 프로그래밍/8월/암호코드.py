num = [0]
num += list(input())
dp = [0] * (len(num) + 1)
dp[0] = dp[1] = 1
n = len(num)

if num[1] == "0":   # 맨 앞이 0이면 불가
    print(0)
    exit()

for i in range(2, len(num)):
    one = int(num[i])
    ten = int(num[i - 1]) * 10 + one
    # 2자리가 알파벳인 경우
    if 10 <= ten <= 26:
        dp[i] += dp[i - 2]
    # 1자리수가 0이 아닌 경우
    if one > 0:
        dp[i] += dp[i - 1]

print(dp[n - 1] % 1000000)
