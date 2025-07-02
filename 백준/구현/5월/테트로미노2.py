n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt, sum_value):
    global max_value
    if cnt == 4:
        max_value = max(max_value, sum_value)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
            continue

        visited[nx][ny] = True
        dfs(nx, ny, cnt + 1, sum_value + board[nx][ny])
        visited[nx][ny] = False

# ㅗ 모양의 테트로미노를 찾는 함수
def ft(x, y):
    global max_value
    arr = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        arr.append(board[nx][ny])

    if len(arr) == 4:
        result = sum(arr) - min(arr) + board[x][y]
        max_value = max(max_value, result)
    elif len(arr) == 3:
        max_value = max(max_value, sum(arr) + board[x][y])
    else:
        return

max_value = -1
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        ft(i, j)
        visited[i][j] = False

print(max_value)