n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
numbering = 1
def dfs(graph, x, y):
    global width
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    
    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(graph, nx, ny)

width = 0
result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(graph, i, j)
            result.append(width)
            width = 0

print(len(result))
result.sort()
for x in result:
    print(x)