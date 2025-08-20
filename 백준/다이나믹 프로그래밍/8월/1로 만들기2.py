import copy
N = int(input())
INF = float('inf')
dp = [INF] * int(N + 1)
process = [[] for _ in range(N + 1)] #연산 진행 과정을 담는 리스트
dp[1] = 0
process[1].append(1)
for i in range(1, N):

    for nx in [i + 1, i * 2, i * 3]:
        if nx <= N and dp[nx] > dp[i] + 1:
            dp[nx] = dp[i] + 1
            process[nx] = process[i] + [nx]

print(dp[N])
process[N].reverse()
print(*process[N])