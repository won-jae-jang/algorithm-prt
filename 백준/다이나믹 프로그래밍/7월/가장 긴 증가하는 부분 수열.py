n = int(input())
dp = [0] * n
seq = list(map(int, input().split()))

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))