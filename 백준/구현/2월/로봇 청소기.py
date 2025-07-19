n, m = map(int, input().split())
x, y, direction = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#로봇 청소기가 반시계 방향으로 회전
def rotate(direction):
    direction -= 1 
    return direction if direction >= 0 else 3

width = 0 #청소한 칸의 수
clean = [[False] * m for _ in range(n)] #청소 여부
while True:
    #1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소
    if graph[x][y] == 0 and not clean[x][y]:
        clean[x][y] = True
        width += 1

    cleanable = False #청소할 수 있는 공간이 있는가
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #빈칸이고 청소가 안되어 있는 경우
        if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 0 and not clean[nx][ny]:
            cleanable = True
            break

    #2. 청소할 수 있는 공간이 없는 경우
    if not cleanable:
        #방향을 유지하며 한칸 뒤로 가기
        nx = x - dx[direction]
        ny = y - dy[direction]
        #후진할 수 있는 경우
        if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 0:
            x, y = nx, ny
        #후진할 수 없는 경우
        else:
            break
    #3. 청소할 수 있는 공간이 있는 경우
    else:
        direction = rotate(direction) 
        #바라보는 방향을 기준으로 한 칸 전진
        nx = x + dx[direction]
        ny = y + dy[direction]
        #앞쪽 칸이 청소되지 않은 빈 칸인 경우
        if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 0 and not clean[nx][ny]:
            x, y = nx, ny
        
print(width)