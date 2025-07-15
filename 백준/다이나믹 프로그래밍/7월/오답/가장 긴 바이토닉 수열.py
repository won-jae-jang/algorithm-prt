n = int(input())
seq = list(map(int, input().split()))

def LIS(seq):
    dp = [0] * n
    for i in range(n):
        dp[i] = 1
        for j in range(0, i):
            if seq[j] < seq[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return dp

left = LIS(seq)
seq.reverse()
right = LIS(seq)
result = 0
# print(left, right)
for i in range(n):
    # print(left[i], right[n - 1 - i])
    result = max(result, left[i] + right[n - 1 - i] - 1)

print(result)