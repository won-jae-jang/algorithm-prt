n, k = map(int, input().split())
data = list(list(map(int, input().split())) for _ in range(n))

dp = [[0] * (k + 1) for _ in range(n + 1)]
for cur_obj in range(1, n + 1):
    cur_weight = data[cur_obj - 1][0] #현재 물건의 무게
    cur_value = data[cur_obj - 1][1] #현재 물건의 가치
    for limit in range(1, k + 1):
        #현재 물건의 무게가 제한 무게보다 무거운 경우
        if cur_weight > limit:
            dp[cur_obj][limit] = dp[cur_obj - 1][limit]
        #현재의 물건을 포함할 수 있는 경우
        else:
            dp[cur_obj][limit] = max(dp[cur_obj - 1][limit], dp[cur_obj - 1][limit - cur_weight] + cur_value)

print(dp[n][k])