n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
numbering = 1
def dfs(graph, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1:
                graph[nx][ny] = numbering
                dfs(graph, nx, ny)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            numbering += 1
            dfs(graph, i, j)

result = []
for k in range(2, numbering + 1):
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == k:
                count += 1

    result.append(count)

result.sort()   
print(len(result))
for x in result:
    print(x)