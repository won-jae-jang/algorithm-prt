r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
air_cleaner = []

for i in range(r):
    for j in range(c):
        if room[i][j] == -1:
            air_cleaner.append([i, j])

#공기 청정기의 좌표
x1, y1, x2, y2 = air_cleaner[0][0], air_cleaner[0][1], air_cleaner[1][0], air_cleaner[1][1]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#미세먼지 확산
def spread():
    spread_result = [[0] * c for _ in range(r)]
    spread_result[x1][y1] = -1
    spread_result[x2][y2] = -1    

    for x in range(r):
        for y in range(c):
            #미세먼지가 없으면 확산X
            if room[x][y] <= 0:
                continue
            spread_result[x][y] += room[x][y]
            #동서남북으로 확산
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                #공기 청정기 위치가 아니라면 확산하기
                if (0 <= nx < r) and (0 <= ny < c) and spread_result[nx][ny] != -1:
                    spread_amount = room[x][y] // 5
                    spread_result[nx][ny] += spread_amount
                    spread_result[x][y] -= spread_amount

    return spread_result

#공기 청정기 작동하여 윗쪽 미세먼지 이동
def up_cleaning():
    #동북서남 (미세먼지의 이동 방향)
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    
    direction = 0
    prv = 0
    x, y = x1, 1 #초기 시작 좌표 (위쪽 공기 청정기의 오른쪽 좌표)
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        #처음으로 돌아온 경우
        if x == x1 and y == 0:
            break
        #방향 전환
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direction += 1
            continue
        
        prv, room[x][y] = room[x][y], prv
        x, y = nx, ny

def down_cleaning():
    #동남서북 (미세먼지의 이동방향향)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    direction = 0
    prv = 0
    x, y = x2, 1

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        #처음으로 돌아온 경우
        if x == x2 and y == 0:
            break
        #방향 전환
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direction += 1
            continue
        
        prv, room[x][y] = room[x][y], prv
        x, y = nx, ny

for _ in range(t):
    room = spread()
    up_cleaning()
    down_cleaning()
    room[x1][y1] = -1
    room[x2][y2] = -1

width = 0
for i in range(r):
    for j in range(c):
        if room[i][j] >= 1:
            width += room[i][j]

print(width)