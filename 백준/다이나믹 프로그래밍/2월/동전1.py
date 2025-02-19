n, k = map(int, input().split())
array = [int(input()) for _ in range(n)]
dp = [0] * (k + 1)
dp[0] = 1 

for i in range(n):
    for j in range(array[i], k + 1):
        dp[j] = dp[j] + dp[j - array[i]]

print(dp[-1])