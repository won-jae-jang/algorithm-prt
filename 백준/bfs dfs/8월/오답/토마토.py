from collections import deque
M, N = map(int, input().split())
graph = []
pos = [] #초기 익은 토마토의 위치
for i in range(N):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(M):
        #익은 토마토 좌표 추가
        if data[j] == 1:
            pos.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return False
    return True

if len(pos) == 0:
    print(-1)
else:
    q = deque(pos)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    #모든 토마토가 익은 경우
    if check():
        result = 0
        for i in range(N):
            result = max(result, max(*graph[i]))
        print(result - 1)
    # 모든 토마토가 익지 못한 경우
    else:
        print(-1)