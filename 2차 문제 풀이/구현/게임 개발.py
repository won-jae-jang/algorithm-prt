n, m = map(int, input().split())
x, y, direction = map(int, input().split())
d = [[0] * m for _ in range(n)] #방문여부 표시
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북동남서 0123
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 1
turn_time = 0

while True:
    #1단계
    direction -= 1
    if direction < 0:
        direction = 3
    #2단계
    nx = x + dx[direction]
    ny = y + dy[direction]

    #이동한 곳이 육지라면 캐릭터 옮기기
    if array[nx][ny] == 0 and d[nx][ny] == 0:
        x, y = nx, ny
        d[nx][ny] = 1 #방문 표시
        result += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4: #4방향 모두 이동할 수 없다면
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x, y = nx, ny
            turn_time = 0
        else:
            break

print(result)