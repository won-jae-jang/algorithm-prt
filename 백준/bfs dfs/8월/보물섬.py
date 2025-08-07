from collections import deque

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    global result
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True
    while q:
        x, y, dist = q.popleft()
        if dist > result:
            result = dist
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 'L':
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))

for x in range(N):
    for y in range(M):
        if graph[x][y] == 'L':
            visited = [[False] * M for _ in range(N)]
            bfs(x, y)

print(result)