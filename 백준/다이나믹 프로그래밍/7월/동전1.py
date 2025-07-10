n, k = map(int, input().split())
coins = list(int(input()) for _ in range(n))
dp = [0] * (k + 1)
dp[0] = 1 #0원을 만드는 방법은 1개 (모든 코인을 사용x)

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]

print(dp[k])