def roll(direction):
    #동쪽
    if direction == 1:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[4], dice[2], dice[1], dice[6], dice[5], dice[3],
    #서쪽
    elif direction == 2:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[3], dice[2], dice[6], dice[1], dice[5], dice[4],
    #북쪽
    elif direction == 3:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[5], dice[1], dice[3], dice[4], dice[6], dice[2],
    #남쪽
    else:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[2], dice[6], dice[3], dice[4], dice[1], dice[5],

dice = [0] * 7 #1이 윗면, 6이 아랫면
n, m, x, y, k = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n))
move = list(map(int, input().split()))
#동서북남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for direction in move:
    nx = x + dx[direction - 1]
    ny = y + dy[direction - 1]
    if 0 <= nx < n and 0 <= ny < m:
        roll(direction)
        #이동한 칸의 수가 0인 경우
        if board[nx][ny] == 0:
            #주사위의 바닥면에 쓰여 있는 수가 칸에 복사
            board[nx][ny] = dice[6]
        #0이 아닌 경우
        else:
            #칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다
            board[nx][ny], dice[6] = 0, board[nx][ny]
        x, y = nx, ny
        print(dice[1])
