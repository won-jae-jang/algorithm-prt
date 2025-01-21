import copy
import sys 
sys.setrecursionlimit(10000) 
n = int(input())

normal = []
for i in range(n):
    normal.append(list(input()))

color = copy.deepcopy(normal)
for i in range(n):
    for j in range(n):
        if color[i][j] == 'R':
            color[i][j] = 'G'

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def dfs(graph, x, y):
    current_color = graph[x][y]
    graph[x][y] = 'V' #방문 처리

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny] == current_color:
            dfs(graph, nx, ny)
    
n_count = 0
for i in range(n):
    for j in range(n):
        #방문하지 않았다면
        if normal[i][j] != 'V':
            n_count += 1
            dfs(normal, i, j)

c_count = 0
for i in range(n):
    for j in range(n):
        #방문하지 않았다면
        if color[i][j] != 'V':
            c_count += 1
            dfs(color, i, j)

print(n_count, c_count)