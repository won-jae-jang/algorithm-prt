from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def melt():
    melt_result = [[0] * M for _ in range(N)]

    for x in range(N):
        for y in range(M):
            #빙하가 있는 구역이라면
            if graph[x][y] > 0:
                count = 0 #인근 바닷물의 개수
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    #상하좌우중 하나가 바닷물인 경우
                    if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                        count += 1

                melt_result[x][y] = graph[x][y] - count if graph[x][y] - count > 0 else 0

    return melt_result

def bfs(x, y):

    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if graph[nx][ny] > 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

result = 0
while True:
    result += 1
    graph = melt() #빙하 녹이기
    visited = [[False] * M for _ in range(N)]
    count = 0 #빙하의 개수
    for x in range(N):
        for y in range(M):
            if graph[x][y] > 0 and not visited[x][y]:
                bfs(x, y)
                count += 1

    #빙산이 두 덩어리 이상으로 분리된 경우
    if count >= 2:
        print(result)
        break
    #빙산이 다 녹은 경우
    elif count == 0:
        print(0)
        break




