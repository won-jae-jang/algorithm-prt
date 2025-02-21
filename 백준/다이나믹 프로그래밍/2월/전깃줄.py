n = int(input())
dp = [0] * (11)
array = [list(map(int, input().split())) for _ in range(n)]
array.sort()

for i in range(n):
    #전깃줄이 교차하는 경우
    # if array[i][0] < array[i + 1][0] and array[i][1] > array[i + 1][1]:
    #     dp[array[i + 1][0]] = dp[array[i][0]]
    # else:
    #     dp[array[i + 1][0]] = dp[array[i][0]] + 1

    count = i + 1
    for j in range(i + 1):
        #전깃줄이 교차하는 경우
        if array[i][0] < array[j][0] and array[i][1] > array[j][1]:
            count -= 1

    dp[i] = max(dp[i - 1], count)

print(dp)
print(n - max(dp))