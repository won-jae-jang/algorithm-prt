import copy
board = []
pos = []
for i in range(9):
    data = list(map(int, input()))
    board.append(data)
    for j in range(9):
        if data[j] == 0:
            pos.append((i, j))

def row(x, target):
    for i in range(9):
        if board[x][i] == target:
            return False
    return True

def column(y, target):
    for i in range(9):
        if board[i][y] == target:
            return False
    return True

def rect(x, y, target):
    x = x // 3 * 3
    y = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[x + i][y + j] == target:
                return False
    return True

result = []
def dfs(n):
    if n == len(pos):
        result.append(copy.deepcopy(board))
        for i in range(9):
            for j in range(9):
                print(board[i][j], end='')
            print()
        exit()

    x, y = pos[n]
    for i in range(1, 10):
        if row(x, i) and column(y, i) and rect(x, y, i):
            board[x][y] = i
            dfs(n + 1)
            board[x][y] = 0

dfs(0)










