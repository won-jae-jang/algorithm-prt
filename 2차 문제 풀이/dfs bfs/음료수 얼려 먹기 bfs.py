from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, row, column):

    if graph[row][column] == 1:
        return 0
    
    q = deque([(row, column)])
    graph[row][column] = 1 #방문 처리
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 1 #방문 처리
                q.append((nx, ny))
    
    return 1

result = 0
for i in range(n):
    for j in range(m):
        result += bfs(graph, i, j)

print(result)