import sys
sys.setrecursionlimit(90000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#빙하 녹이기
def melt(graph):
    melt_graph = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            count = 0
            #해당 구역이 빙산인 경우
            if graph[x][y] != 0:
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    #인접한 바닷물의 개수 파악
                    if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 0:
                        count += 1

                ice = graph[x][y] - count
                if ice > 0:
                    melt_graph[x][y] = ice
                    visited[x][y] = False #dfs 대상으로 인식

    return melt_graph


def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] != 0 and not visited[nx][ny]:
            dfs(nx, ny)

year = 0
seperate = False #빙하가 둘로 분리되었는가
while not seperate:
    visited = [[True] * m for _ in range(n)]
    graph = melt(graph)
    year += 1
    
    group = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                group += 1
                dfs(i, j)

    if group >= 2:
        seperate = True
    #모든 빙하가 다 녹은 경우
    elif group == 0:
        break

if seperate:
    print(year)
else:
    print(0)