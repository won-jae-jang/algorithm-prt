import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = []
tomatoes = [] #익은 토마토의 좌표
for height in range(h):
    temp = []
    for i in range(n):
        data = list(map(int, input().split()))
        temp.append(data)
        for j in range(m):
            #익은 토마토의 위치 추가
            if data[j] == 1:
                tomatoes.append((i, j, height))

    graph.append(temp)

#모든 구역에 토마토가 익었는지 확인
def check(graph):
    for height in range(h):
        for i in range(n):
            for j in range(m):
                if graph[height][i][j] == 0:
                    return False
    return True

day = 0
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
q = deque(tomatoes)
#bfs
while True:

    tomatoes = [] #1일뒤에 익은 토마토를 새롭게 담기 위해서 빈 배열로 만듬

    while q:
        pos = q.popleft()
        x, y, z = pos[0], pos[1], pos[2]
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if (0 <= nx < n) and (0 <= ny < m) and (0 <= nz < h) and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = 1
                tomatoes.append((nx, ny, nz))

    #하루가 지나도 익은 토마토가 없으면 반복문 탈출
    if len(tomatoes) == 0:
        break

    else:
        q = deque(tomatoes)
        day += 1

if check(graph):
    print(day)
else:
    print(-1)