from collections import deque

n = int(input())
graph = list(list(input()) for _ in range(n))
# print(graph)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y, color):
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                #현재와 같은 색깔인 경우
                if graph[nx][ny] == color:
                    q.append((nx, ny))
                    visited[nx][ny] = True

normal = 0 #정상인 사람의 영역
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            normal += 1
            bfs(i, j, graph[i][j])


#적록 색약의 사람은 R = G 이므로 R -> G로 변경
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

color = 0 #적록색약에 해당하는 사람
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            color += 1
            bfs(i, j, graph[i][j])

print(normal, color)