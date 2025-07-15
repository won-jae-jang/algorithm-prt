def dfs(graph, x, y):
    graph[x][y] = 0 #방문처리
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #이동한 인접한 영역에 배추가 있다면
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1:
            dfs(graph, nx, ny)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for tc in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    result = 0
    #배추 위치 표시
    for i in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    #밭 순회하면서 dfs
    for i in range(m):
        for j in range(n):
            #현재 위치에 배추가 있다면
            if graph[i][j] == 1:
                result += 1
                dfs(graph, i, j)

    print(result)