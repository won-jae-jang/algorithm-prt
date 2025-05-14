def roll(direction):
    #동쪽으로 주사위 굴리기
    if direction == 1:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]
    #서쪽
    elif direction == 2:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]
    #북쪽
    elif direction == 3:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]
    #남쪽
    else:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dice = [0] * 7
orders = list(map(int, input().split()))

#동 서 북 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for order in orders:
    nx = x + dx[order - 1]
    ny = y + dy[order - 1]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
    #주사위 굴리기
    roll(order)
    print(dice[1])  # 윗면에 쓰여 있는 수를 출력한다.
    #이동한 지도의 칸이 0인 경우, 해당 칸에 주사위 바닥면을 복사한다.
    if board[nx][ny] == 0:
        board[nx][ny] = dice[-1]
    #주사위 바닥면의 수를 지도칸의 수로 바꾼다.
    else:
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0

    x, y = nx, ny
