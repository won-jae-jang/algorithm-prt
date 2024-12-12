n, m = map(int, input().split())
x, y, direction = map(int, input().split())
array = []
for i in range(4):
    array.append(list(map(int, input().split())))

#북 동 남 서 (direction[i] * - 1을 하면 해당 방향에서 한칸 뒤로감)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 1
array[x][y] = 1 #현재 위치 방문 처리
while True:
    move = False
    for i in range(4):
        direction -= 1
        if direction < 0:
            direction = 3
        nx = x + dx[direction]
        ny = y + dy[direction]
        if array[nx][ny] == 0:
            array[nx][ny] = 1
            count += 1
            x, y = nx, ny
            move = True
            break
    #모든 방향에 가봤다면
    if not move:
        #방향 유지 & 뒤로 한칸 가기
        nx = x + dx[i] * -1
        ny = y + dy[i] * -1
        # 뒤로 한칸 이동한 곳이 바다면 움직임을 멈춤
        if array[nx][ny] == 1:
            break
        x, y = nx, ny

print(count)
    