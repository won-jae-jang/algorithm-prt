from collections import deque
m, n = map(int, input().split())
graph = []
tomatoes = [] #익은 토마토의 좌표
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(m):
        if data[j] == 1:
            tomatoes.append((i, j))
    graph.append(data)

#익지 않은 토마토가 있는지 확인
def is_ripe():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return False
    return True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque(tomatoes)
result = 0
while True:
    tomatoes = [] #새롭게 익은 토마토들

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 0:
                tomatoes.append((nx, ny))
                graph[nx][ny] = 1

    if len(tomatoes) == 0:
        if is_ripe():
            print(result)
        else:
            print(-1)
        break

    else:
        q = deque(tomatoes)
        result += 1










