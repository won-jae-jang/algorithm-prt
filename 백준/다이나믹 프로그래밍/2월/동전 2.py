n, k = map(int, input().split())
array = [int(input()) for _ in range(n)]
dp = [1e9] * (100001)

#초기 입력받은 동전은 1개로 만들 수 있음
for coin in array:
    dp[coin] = 1

for coin in array:
    for i in range(1, k + 1):
        #개수를 셀수 있는 경우
        if dp[i] < 1e9 and (i + coin) <= k:
            dp[i + coin] = min(dp[i + coin], dp[i] + 1)
            
if dp[k] != 1e9:
    print(dp[k])
else:
    print(-1)