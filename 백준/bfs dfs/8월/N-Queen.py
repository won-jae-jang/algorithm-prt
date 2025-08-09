n = int(input())
graph = [[0] * n for _ in range(n)]

#퀸의 공격 경로: 상하좌우, 대각선: 좌상, 우상, 좌하, 우하
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

result = 0
def dfs(count):
    global result
    if count == n:
        result += 1
        return

    for x in range(n):
        for y in range(n):
            #퀸을 배치할 수 있는 공간인 경우
            if graph[x][y] == 0:
                #simulation
                if not attack(x, y):
                    graph[x][y] = 1
                    dfs(count + 1)
                    graph[x][y] = 0

#x, y 위치에 퀸을 설치할 경우 다른 퀸을 공격하는지 여부
def attack(x, y):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        while 0 <= nx < n and 0 <= ny < n:
            #공격 경로에 다른 퀸이 있는 경우
            if graph[nx][ny] != 0:
                return True
            nx += dx[i]
            ny += dy[i]

    return False

dfs(0)
print(result)