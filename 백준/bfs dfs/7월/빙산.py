from collections import deque
import copy
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

#1. 0의 값을 기준으로 bfs -> 빙하 녹이기
#2. 0이 아닌 값을 bfs -> 빙하 덩어리 개수 파악

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

#melt_graph: 녹인후의 결과(복사본), graph: 현재 그래프
def melt():
    melt_graph = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            count = 0 #주위 바닷물의 개수
            #위치가 빙산인 경우
            if graph[x][y] != 0:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                        count += 1
                ice = graph[x][y] - count

                if ice > 0:
                    melt_graph[x][y] = ice
                    #방문처리

    return melt_graph

def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True #방문 처리
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] >= 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True

def ice():
    count = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 1 and not visited[i][j]:
                count += 1
                bfs(i, j, visited)
    return count

result = 0
while True:
    result += 1
    visited = [[False] * m for _ in range(n)]
    #얼음 녹이기
    graph = melt()

    # print(graph)
    count = ice()
    # print(count)
    if count >= 2:
        print(result)
        break
    elif count == 0:
        print(0)
        break