r, c, t = map(int, input().split())
x1, x2, = 0, 0 #공기 청정기의 위치
graph = []
for i in range(r):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(c):
        if data[j] == -1:
            if x1 == 0:
                x1 = i
            else:
                x2 = i

#미세먼지 확산
def spread():
    spread_result = [[0] * c for _ in range(r)]
    spread_result[x1][0] = -1
    spread_result[x2][0] = -1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for x in range(r):
        for y in range(c):
            #미세먼지가 있는 구역일 경우
            if graph[x][y] > 0:
                spread_result[x][y] += graph[x][y]
                amount = int(graph[x][y] / 5) #확산되는 양
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                        spread_result[nx][ny] += amount
                        spread_result[x][y] -= amount

    return spread_result

#공기 청정기 위쪽
def up():
    #시계방향: 동북서남
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direction = 0
    prv = 0
    x, y = x1, 1 #시작 좌표
    #공기 청정기에 도착할 때까지 반복
    while True:
        if x == x1 and y == 0:
            break

        nx = x + dx[direction]
        ny = y + dy[direction]

        #방향 전환 조건
        if nx >= r or ny >= c or nx < 0 or ny < 0:
            direction += 1
            continue

        graph[x][y], prv = prv, graph[x][y]
        x, y = nx, ny

#공기 청정기 아래쪽
def down():
    #반시계방향: 동남서북
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direction = 0
    prv = 0
    x, y = x2, 1 #시작 좌표
    #공기 청정기에 도착할 때까지 반복
    while True:
        if x == x2 and y == 0:
            break
        nx = x + dx[direction]
        ny = y + dy[direction]
        #방향 전환 조건
        if nx >= r or ny >= c or nx < 0 or ny < 0:
            direction += 1
            continue

        graph[x][y], prv = prv, graph[x][y]
        x, y = nx, ny

for _ in range(t):
    graph = spread()
    up()
    down()

result = 0
for i in range(r):
    result += sum(graph[i])

print(result + 2)














