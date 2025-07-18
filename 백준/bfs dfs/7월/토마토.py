from collections import deque

n, m, h = map(int, input().split())
graph = []
tomatoes = [] #익은 토마토의 좌표
for floor in range(h):
    data = list(list(map(int, input().split())) for _ in range(m))
    for i in range(m):
        for j in range(n):
            #익은 토마토의 좌표
            if data[i][j] == 1:
                tomatoes.append((floor, i, j))
    graph.append(data)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(tomatoes):
    q = deque(tomatoes)
    next_pos = []
    while q:
        floor, x, y = q.popleft()
        #상하좌우
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[floor][nx][ny] == 0:
                graph[floor][nx][ny] = 1 #방문처리
                next_pos.append((floor, nx, ny))
        #위 아래
        for i in [-1, 1]:
            temp_floor = floor + i
            if 0 <= temp_floor < h and graph[temp_floor][x][y] == 0:
                graph[temp_floor][x][y] = 1 #방문처리
                next_pos.append((temp_floor, x, y))

    return next_pos

#모든 토마토가 다 익었는지 확인
def check(graph):
    for i in range(h):
        for x in range(m):
            for y in range(n):
                if graph[i][x][y] == 0:
                    return False

    return True

result = 0
while True:

    tomatoes = bfs(tomatoes)
    #토마토를 더 이상 익히지 못하는 경우
    if len(tomatoes) == 0:
        if check(graph):
            print(result)
        else:
            print(-1)
        break
    #토마토가 더 익는 경우
    result += 1