n = int(input())
t = [0]
p = [0]
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

dp = [0] * (n + 1)
for i in range(1, n + 1):
    date = i + t[i] #현재 일자에서 일을 할 경우 다음에 일할 수 있는 날짜
    dp[i] = max(dp[i], dp[i - 1])
    #현재 일자에 일을 할 수 있는 경우
    if date <= n:
        dp[date] = max(dp[date], dp[i] + p[i])

print(dp[n])