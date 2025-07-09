# https://beyond-common-sense.tistory.com/4
n, k = map(int, input().split())

weight = [0] * (n + 1)
value = [0] * (n + 1)

for i in range(1, n + 1):
    weight[i], value[i] = map(int, input().split())

# dp[n][w]: n번째 물건을 선택했을때 (혹은 X) 무게 W일때의 최대 가치
dp = [[0] * (k + 1) for _ in range(n + 1)]
for cur_n in range(1, n + 1):
    for limit in range(1, k + 1):
        #현재 물건의 무게가 제한 무게보다 큰 경우
        if weight[cur_n] > limit:
            dp[cur_n][limit] = dp[cur_n - 1][limit]
        #현재 물건의 무게가 제한 무게보다 작은 경우
        else:
            #dp = max(현재 물건 선택X, 현재 물건을 선택할 경우)
            dp[cur_n][limit] = max(dp[cur_n - 1][limit], dp[cur_n - 1][limit - weight[cur_n]] + value[cur_n])

print(dp[-1][-1])