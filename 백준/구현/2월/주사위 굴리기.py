import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))

#동서북남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

left, right = 0, 0  #주사위의 좌우 
body = [0, 0, 0, 0] #주사위의 몸통
head_idx = 1 #주사위 윗면
tail_idx = 3 #주사위 바닥

for direction in command:
    nx = x + dx[direction - 1]
    ny = y + dy[direction - 1]
    #범위에 벗어나는 경우
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

    #동쪽인 경우
    if direction == 1:
        prv_left = left
        prv_right = right
        left = body[tail_idx]
        right = body[head_idx]
        body = [body[0], prv_left ,body[2], prv_right]
    #서쪽인 경우
    elif direction == 2:
        prv_left = left
        prv_right = right
        left = body[head_idx]
        right = body[tail_idx]
        body = [body[0], prv_right ,body[2], prv_left]
    #북쪽으로 굴린 경우
    elif direction == 3:
        body = [body[1], body[2], body[3], body[0]]
    #남쪽으로 굴린 경우
    else:
        body = [body[3], body[0], body[1], body[2]]

    x, y = nx, ny
    #이동한 칸의 수가 0인 경우
    if board[x][y] == 0:
        #해당칸이 주사위 바닥면의 값으로 변경됨
        board[x][y] = body[tail_idx]
    #0이 아닌 경우        
    else:
        #이동한 칸의 값이 주사위 바닥면으로 복사됨
        body[tail_idx] = board[x][y]
        #칸에 쓰여진 수는 0이됨
        board[x][y] = 0

    print(body[head_idx])        
    # print(x, y)