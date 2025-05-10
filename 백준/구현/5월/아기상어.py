from collections import deque

# 1. 초기의 아기상어의 크기는 2 이다.
# 2. 아기 상어는 자신의 크기 보다 작은 물고기만 먹을 수 있다.
# 2-1. 물고기 먹으면 사라짐
# 3. 아기 상어는 자신의 크기보다 작거나 같은 물고기가 있는 칸을 지날 수 있다.
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

x, y = 0, 0 #아기 상어의 초기 위치
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            x, y = i, j
            board[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# x, y는 초기 아기상어의 좌표
def bfs(x, y):
    global size #아기 상어의 크기
    fish = [] #먹을 수 있는 물고기
    visited[x][y] = True
    q = deque()
    q.append((x, y, 0))
    while q:
        x, y, distance = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 3. 아기 상어는 자기보다 크기가 작거나 같은 물고기들은 지나갈 수 있다
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] <= size:
                # 만약 먹을 수 있는 물고기라면
                if 1 <= board[nx][ny] < size:
                    # 정렬을 윌해 아래 순서대로 삽입
                    fish.append((distance + 1, nx, ny))
                q.append((nx, ny, distance + 1))
                visited[nx][ny] = True

    return fish

size = 2 #아기상어 크기
eat = 0 #아기상어가 먹은 물고기
time = 0
while True:
    visited = [[False] * n for _ in range(n)]
    fish = bfs(x, y)
    # 먹을 수 있는 물고기가 없는 경우
    if not fish:
        print(time)
        break

    fish.sort()
    dist, x, y = fish.pop(0)
    # print(dist, x, y)
    time += dist
    # 물고기 먹기
    board[x][y] = 0
    eat += 1
    # 자신의 크기와 같은 수의 물고기를 먹을때 마다 크기가 1 증가
    if size == eat:
        size += 1
        eat = 0
