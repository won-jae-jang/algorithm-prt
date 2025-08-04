import sys
sys.setrecursionlimit(100000)
N, M = map(int, input().split())
dp = [[-1] * M for _ in range(N)]
graph = list(list(map(int, input().split())) for _ in range(N))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x == N - 1 and y == M - 1:
        return 1
    #x, y를 경유하여 목적지까지 도착할 수 있는 경우
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and (graph[x][y] > graph[nx][ny]):
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

dfs(0, 0)
print(dp[0][0])