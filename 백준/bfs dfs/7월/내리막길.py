import sys
sys.setrecursionlimit(100000)
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y):
    #목적지 도달한 경우
    if x == m - 1 and y == n - 1:
        return 1
    #이미 경로가 계산된 경우
    if dp[x][y] != -1:
        return dp[x][y]
    #처음 방문한 경로일 때
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[x][y] > graph[nx][ny]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))