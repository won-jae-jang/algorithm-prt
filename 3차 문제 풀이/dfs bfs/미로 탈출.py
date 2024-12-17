from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1] #동서남북
dy = [1, -1, 0, 0] 
q = deque([(0, 0, 1)]) #x, y, count
graph[0][0] = 0 #방문처리
while q:
    x, y, count = q.popleft()
    if x == n - 1 and y == m - 1:
        print(count)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                q.append((nx, ny, count + 1))
                graph[nx][ny] = 0 #방문처리
