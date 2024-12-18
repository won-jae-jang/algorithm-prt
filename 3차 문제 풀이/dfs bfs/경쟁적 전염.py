from collections import deque

n, k = map(int, input().split())
graph = []
info = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        #바이러스라면
        if data[j] != 0:
            info.append((data[j], i, j, 0)) #type, 좌표, 시간
    graph.append(data)

s, x, y = map(int, input().split()) #s초 후에 x, y 에 위치하는 바이러스
info.sort()
q = deque(info)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
while q:
    virus, vx, vy, time = q.popleft()
    if vx == x - 1 and vy == y - 1:
        if time <= s:
            print(virus)
        else:
            print(0)
        break
    #바이러스 전이
    for i in range(4):
        nx = vx + dx[i]
        ny = vy + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0: 
                graph[nx][ny] = virus #방문처리
                q.append((virus, nx, ny, time + 1))
