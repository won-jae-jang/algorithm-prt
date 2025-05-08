import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, cnt, sum_value):
    global result
    if cnt == 4:
        result = max(result, sum_value)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
            continue
        visited[nx][ny] = True
        dfs(nx, ny, cnt + 1, sum_value + paper[nx][ny])
        visited[nx][ny] = False

def fy(x, y):
    global result
    arr = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        arr.append(paper[nx][ny])

    length = len(arr)
    if length == 4:
        arr.sort(reverse=True)
        arr.pop()
        result = max(result, sum(arr) + paper[x][y])
    elif length == 3:
        result = max(result, sum(arr) + paper[x][y])
    else:
        return

visited = [[False] * m for _ in range(n)]
result = -1
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, paper[i][j])
        fy(i, j)
        visited[i][j] = False

print(result)