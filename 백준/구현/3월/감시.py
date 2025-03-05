import copy

mode = [
    [],
    [[0], [1], [2], [3]],
    [[1, 3], [0, 2]],
    [[2, 1], [1, 0], [3, 2], [3, 0]],
    [[0, 1, 3], [0, 1, 2], [3, 1, 2], [3, 2, 0]],
    [[0, 1, 2, 3]]
]

#북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

cctv = []
for i in range(n):
    for j in range(m):
        if board[i][j] in [1, 2, 3, 4, 5]:
            cctv.append((board[i][j], i, j)) ##cctv_type, x, y

def fill(board, mode, x, y):
    for i in mode:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == 6:
                break

            if board[nx][ny] == 0:
                board[nx][ny] = -1


def dfs(depth, board):
    global min_value
    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += board[i].count(0)
        min_value = min(min_value, count)
        return

    # temp = copy.deepcopy(board)
    temp = [[j for j in board[i]] for i in range(n)]
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        fill(temp, i, x, y)
        dfs(depth + 1, temp)
        # temp = copy.deepcopy(board)
        temp = [[j for j in board[i]] for i in range(n)]

min_value = int(1e9)
dfs(0, board)
print(min_value)