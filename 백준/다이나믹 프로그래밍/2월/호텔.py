c, n = map(int, input().split())
cost_list = [list(map(int, input().split())) for _ in range(n)]    
dp = [1e9] * (c + 100) 
dp[0] = 0

for cost, people in cost_list:
    for i in range(people, c + 100):
        dp[i] = min(dp[i], dp[i - people] + cost)

print(min(dp[c:]))