n = int(input())
dp = [0] * (501)
array = [list(map(int, input().split())) for _ in range(n)]
array.sort()

for i in range(n):
    # i번째 전깃줄은 연결 상태
    dp[array[i][0]] = 1 
    for j in range(i):
        #전깃줄이 교차하지 않는 경우
        if array[j][0] < array[i][0] and array[j][1] < array[i][1]:
            dp[array[i][0]] = max(dp[array[i][0]], dp[array[j][0]] + 1)

print(n - max(dp))