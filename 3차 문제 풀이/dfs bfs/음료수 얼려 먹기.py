from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

count = 0
dx = [0, 0, 1, -1] #동서남북
dy = [1, -1, 0, 0]
for i in range(n):
    for j in range(m):
        #구멍이 뚫려 있는 부분이라면
        if graph[i][j] == 0:
            count += 1
            q = deque([(i, j)])
            graph[i][j] = 1 #방문 처리
            #bfs
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if graph[nx][ny] == 0:
                            q.append((nx, ny))
                            graph[nx][ny] = 1 #방문 처리
                    
print(count)