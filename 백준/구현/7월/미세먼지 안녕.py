import copy
from collections import deque
r, c, t = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(r))
x1 = 0
for i in range(r):
    if graph[i][0] == -1:
        x1 = i
        break
x2 = x1 + 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#미세먼지 확산
def spread():
    spread_graph = copy.deepcopy(graph)
    for x in range(r):
        for y in range(c):
            #미세먼지 위치인 경우
            if graph[x][y] >= 1:
                count = 0 #미세먼지가 퍼진 면의 개수
                amount = int(graph[x][y] / 5) #미세먼지가 확산되는양
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    #미세먼지가 퍼질 수 있는 공간인 경우 (0밖에 없음)
                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] >= 0:
                        spread_graph[nx][ny] += amount
                        count += 1
                spread_graph[x][y] -= amount * count

    return spread_graph

def up_cleaning():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    direction = 0
    prv = 0
    x, y = x1, 1 #초기 이동 좌표
    while True:
        #초기 지점으로 돌아온 경우
        if x == x1 and y == 0:
            break

        nx = x + dx[direction]
        ny = y + dy[direction]
        #방향 전환
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direction += 1
            continue

        prv, graph[x][y] = graph[x][y], prv
        x, y = nx, ny

def down_cleaning():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    direction = 0
    prv = 0
    x, y = x2, 1 #초기 이동 좌표
    while True:
        #초기 지점으로 돌아온 경우
        if x == x2 and y == 0:
            break

        nx = x + dx[direction]
        ny = y + dy[direction]
        #방향 전환
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direction += 1
            continue

        prv, graph[x][y] = graph[x][y], prv
        x, y = nx, ny

for i in range(t):

    graph = spread() #미세먼지 확산 결과
    up_cleaning()
    down_cleaning()

result = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            result += graph[i][j]

print(result)