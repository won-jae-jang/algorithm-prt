from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y):
    width = 1
    q = deque()
    q.append((x, y))
    graph[x][y] = 0 #방문 처리
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0 #방문 처리
                width += 1
                q.append((nx, ny))

    return width

count = 0 #총 그림의 개수
max_width = 0 #최대 넓이
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = 0 #방문처리
            count += 1
            max_width = max(max_width, bfs(i, j))

print(count)
print(max_width)