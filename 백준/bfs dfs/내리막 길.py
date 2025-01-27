import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[-1] * n for _ in range(m)]
def dfs(x, y):

    if x == m - 1 and y == n - 1:
        return 1
    
    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0 #방문처리

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < m) and (0 <= ny < n) and (graph[nx][ny] < graph[x][y]):
            visited[x][y] += dfs(nx, ny)

    return visited[x][y]

print(dfs(0, 0))