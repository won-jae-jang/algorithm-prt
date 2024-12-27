n = int(input())
board = [[0] * (n) for _ in range(n)]
k = int(input())
for i in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1 #사과

l = int(input())
info = []
for i in range(l):
    time, direction = input().split()
    info.append((int(time), direction))

#뱀의 회전 (현재 방향, 회전할방향)
def turn(now, rotate):
    #오른쪽으로 회전하는 경우
    if rotate == 'D':
        now += 1
    else:
        now -= 1
    return now % 4

x = y = 0
tail = [(x, y)]
board[x][y] = 2 #뱀의 방문 처리
#동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0 #초기에는 동쪽을 바라봄
result = 0 #게임 진행 시간
index = 0 #회전 정보 인덱스
while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    #보드내에 이동이 가능하고, 자기 자신과 충돌하지 않은 경우
    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in tail:
        #이동한 곳에 사과가 있다면
        if board[nx][ny] == 1:
            tail.append((nx, ny))
            board[nx][ny] = 2
        else:
            tail.append((nx, ny))
            tx, ty = tail.pop(0)
            board[tx][ty] = 0
        result += 1
        x, y = nx, ny
    else:
        result += 1
        break

    if index < l and result == info[index][0]:
        direction = turn(direction, info[index][1])
        index += 1

print(result)