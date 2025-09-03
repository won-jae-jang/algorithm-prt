from collections import deque
import copy
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y, id):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    graph[x][y] = id
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 1:
                graph[nx][ny] = id
                visited[nx][ny] = True
                q.append((nx, ny))


def bridge(island):
    dist = [[-1] * n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if graph[i][j] == island:
                dist[i][j] = 0
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                #신대륙을 발견한 경우
                if graph[nx][ny] != island and graph[nx][ny] != 0:
                    return dist[x][y]
                #새로운 다리를 잇는 경우
                if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

visited = [[False] * n for _ in range(n)]
id = 1
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i, j, id)
            id += 1

# for row in graph:
#     print(*row)

result = 1e10
for island in range(1, id):
    result = min(result, bridge(island))

print(result)