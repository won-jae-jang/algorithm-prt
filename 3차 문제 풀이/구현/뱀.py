n = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]
k = int(input())
for i in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1 #사과 표시

l = int(input())
info = []
for i in range(l):
    time, dir = input().split()
    info.append((int(time), dir))

def turn(direction, dir_info):
    if dir_info == 'D':
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    return direction

#동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 1, 1
board[x][y] = 2 #뱀의 위치
tail = [(x, y)] #뱀의 꼬리
direction = 0 #처음 바라보는 방향은 동쪽
index = 0 #방향을 전환할 시기에 대한 인덱스
time = 0
while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    #보드 내부이고 자기 자신과 충돌하지 않는 경우
    if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] != 2:
        #이동한 칸에 사과가 있다면
        if board[nx][ny] == 1:
            board[nx][ny] = 2
        #이동한 칸에 사과가 없다면
        else:
            board[nx][ny] = 2
            tx, ty = tail.pop(0) #꼬리 위치한 칸 비우기
            board[tx][ty] = 0 
        tail.append((nx, ny))
        x, y = nx, ny
        time += 1
    #보드 외부이고 자기 자신과 충돌하는 경우
    else:
        time += 1
        break
    # 방향 전환
    if index < l and info[index][0] == time:
        direction = turn(direction, info[index][1])
        index += 1

print(time)