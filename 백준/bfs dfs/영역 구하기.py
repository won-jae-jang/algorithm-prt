import sys
sys.setrecursionlimit(10**5)

m, n, k = map(int, input().split())
graph = [[1] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    width = x2 - x1
    height = y2 - y1
    #시작 좌표
    x = m - y1 - height
    y = x1
    for i in range(height):
        for j in range(width):
            graph[x + i][y + j] = 0 #방문처리

# print(graph)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def dfs(x, y):
    global dim
    graph[x][y] = 0 #방문처리

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < m) and (0 <= ny < n) and graph[nx][ny] == 1:
            dim += 1
            dfs(nx, ny)

result = []
count = 0 #영역의 개수

for i in range(m):
    for j in range(n):
        #아직 방문하지 않았다면
        if graph[i][j] == 1:
            count += 1 
            dim = 1 #넓이
            dfs(i, j)
            result.append(dim)
            dim = 0

print(count)
result.sort()
for x in result:
    print(x, end=' ')