dx = [0, 0, 0, 1, 1, 1, -1, -1, -1]
dy = [0, -1, 1, 0, -1, 1, 0, -1, 1]

def dfs(x, y):
    for i in range(9):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
            graph[nx][ny] = 0 #방문처리
            dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    result = 0
    if w == 0 and h == 0:
        break
    graph = list(list(map(int, input().split())) for _ in range(h))
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                result += 1
                #dfs
                dfs(i, j)

    print(result)