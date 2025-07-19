import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

def dfs(x, y):
    graph[x][y] = 0 #방문처리

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < b) and (0 <= ny < a) and graph[nx][ny] == 1:
            dfs(nx, ny)


while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    graph = []
    for i in range(b):
        graph.append(list(map(int, input().split())))

    width = 0
    for i in range(b):
        for j in range(a):
            #해당 위치가 섬이라면
            if graph[i][j] == 1:
                #dfs
                dfs(i, j)
                width += 1
    
    print(width)