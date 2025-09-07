dp = [0] * 11
dp[1] = dp[2] = dp[3] = 1
for i in range(1, 10):
    for nx in [i + 1, i + 2, i + 3]:
        if nx <= 10:
            dp[nx] += dp[i]

for tc in range(int(input())):
    n = int(input())
    print(dp[n])
