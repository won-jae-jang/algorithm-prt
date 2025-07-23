str1 = input()
str2 = input()
str1_length = len(str1)
str2_length = len(str2)

dp = [[0] * (str1_length + 1) for _ in range(str2_length + 1)]
for i in range(1, str2_length + 1):
    for j in range(1, str1_length + 1):
        if str2[i - 1] == str1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])