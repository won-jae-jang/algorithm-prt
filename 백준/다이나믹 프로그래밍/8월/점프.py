n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]
#방향은 오른쪽과 아래만 있음
dx = [1, 0]
dy = [0, 1]

x, y = 0, 0
result = 0
def dfs(x, y):
    global result

    if x == n - 1 and y == n - 1:
        return 1
    #이전에 방문한 적이 있는 경우
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for i in range(2):
        nx = x + dx[i] * graph[x][y]
        ny = y + dy[i] * graph[x][y]
        if 0 <= nx < n and 0 <= ny < n:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

dfs(0, 0)
print(dp[0][0])