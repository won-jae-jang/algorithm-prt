# 1. 방향 변환 정보
# 상-우-하-좌 / +1 = 오른쪽 회전, -1 = 왼쪽 회전
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def rotate(dir):
    global direction
    if dir == 'L':
        return direction - 1 if direction - 1 >= 0 else 3
    else:
        return (direction + 1) % 4

n = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]
k = int(input()) #사과 개수
for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1 #사과 표시

l = int(input())
rotate_info = []
for _ in range(l):
    time, dir = input().split()
    rotate_info.append((int(time), dir))

time = 0
direction = 1 #초기에는 뱀은 오른쪽을 향한다.
x, y = 1, 1 #뱀의 초기 좌표
snake = [(x, y)] #뱀이 차지하고 있는 영역
while True:
    time += 1
    nx = x + dx[direction]
    ny = y + dy[direction]
    # print(snake)
    # 벽에 부딪힌 경우
    if nx <= 0 or nx > n or ny <= 0 or ny > n:
        print(time)
        break
    # 자기 자신의 몸과 부딪힌 경우
    elif (nx, ny) in snake:
        print(time)
        break

    snake.append((nx, ny))
    x = nx
    y = ny
    # 사과가 있다면
    if board[nx][ny] == 1:
        board[nx][ny] = 0 #사과 없애고 몸길이는 변하지 않음
    else:
        snake.pop(0) #몸길이를 줄인다.
        
    if rotate_info and time == rotate_info[0][0]:
        # print('before:', direction)
        direction = rotate(rotate_info[0][1])
        # print('after:', direction)
        rotate_info.pop(0)