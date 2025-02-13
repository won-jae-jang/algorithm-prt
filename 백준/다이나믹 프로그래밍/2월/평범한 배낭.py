n, k = map(int, input().split())
value = [0] * (n + 1)
weight = [0] * (n + 1)
for i in range(1, n + 1):
    weight[i], value[i] = map(int, input().split())

#dp[n][k] : 담은 물건이 n개이고 무게가 k일 때 최대 가치
dp = [[0] * (k + 1) for _ in range(n + 1)] 
for cur_obj in range(1, n + 1):
    for limit in range(1, k + 1):

        if weight[cur_obj] <= limit:
            dp[cur_obj][limit] = max(dp[cur_obj - 1][limit], dp[cur_obj - 1][limit - weight[cur_obj]] + value[cur_obj])
        else:
            dp[cur_obj][limit] = dp[cur_obj - 1][limit]

print(dp[-1][-1])