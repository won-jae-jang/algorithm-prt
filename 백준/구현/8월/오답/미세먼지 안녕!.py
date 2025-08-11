R, C, T = map(int, input().split())
graph = []

x1 = x2 = y1 = y2 = 0 #공기 청정기 설치 위치
flag = False
for x in range(R):
    data = list(map(int, input().split()))
    graph.append(data)
    for y in range(C):
        #공기 청정기 위치
        if data[y] == -1 and flag == False:
            x1, y1 = x, y
            flag = True
            x2 = x1 + 1

def spread():
    spread_result = [[0] * C for _ in range(R)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    spread_result[x1][y1], spread_result[x2][y2] = -1, -1 #공기 청정기 위치
    for x in range(R):
        for y in range(C):
            #미세먼지가 있는 구역이라면
            if graph[x][y] > 0:
                spread_result[x][y] += graph[x][y]
                amount = graph[x][y] // 5 #확산되는 양
                #상하좌우로 확산
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    #범위내 & 공기 청정기가 아닌 경우
                    if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] >= 0:
                        spread_result[x][y] -= amount
                        spread_result[nx][ny] += amount

    return spread_result

#위쪽 이동
def up():
    x, y = x1, 1 #이동 시작 위치
    #동 북 서 남
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direction = 0
    prv = 0
    while True:
        #공기청정기 위치 도착
        if x == x1 and y == 0:
            break

        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direction += 1
            continue

        prv, graph[x][y] = graph[x][y], prv #좌표 이동
        x, y = nx, ny

#위쪽 이동
def down():
    x, y = x2, 1 #이동 시작 위치
    #동 남 서 북
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direction = 0
    prv = 0
    while True:
        #공기청정기 위치 도착
        if x == x2 and y == 0:
            break

        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direction += 1
            continue

        prv, graph[x][y] = graph[x][y], prv #좌표 이동
        x, y = nx, ny

for _ in range(T):
    graph = spread()
    up()
    down()

result = 0
for x in range(R):
    for y in range(C):
        if graph[x][y] >= 1:
            result += graph[x][y]

print(result)
