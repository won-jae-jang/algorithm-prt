import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):

    dx = [0, 0, -1 ,1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n) and graph[ny][nx] == 1:
            graph[ny][nx] = 0
            dfs(ny, nx)

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split()) #가로(열), 세로(행), 배추 위치
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        X, Y = map(int, input().split())
        graph[Y][X] = 1 #배추

    count = 0
    for a in range(m):
        for b in range(n):
            if graph[b][a] == 1:
                dfs(a, b)
                count += 1

    print(count)