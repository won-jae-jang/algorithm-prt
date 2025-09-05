n, s, m = map(int, input().split())
v = list(map(int, input().split()))

dp = [[0] * (1 + m) for _ in range(1 + n)]
dp[0][s] = 1

for i in range(1, n + 1):
    for j in range(m + 1):
        #볼륨 조절 할 수 있다면
        if dp[i - 1][j] == 1:
            left = j - v[i - 1]
            right = j + v[i - 1]
            if 0 <= left <= m:
                dp[i][left] = 1
            if 0 <= right <= m:
                dp[i][right] = 1
    
result = -1
for i in range(m, -1, -1):
    if dp[-1][i] == 1:
        result = i
        break

print(result)