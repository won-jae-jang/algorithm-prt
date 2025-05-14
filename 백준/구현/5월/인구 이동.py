# 1) bfs: 하나의 좌표를 기준으로 국경선을 공유할 수 있는 나라를 담는다.
# 2) 국경선을 공유할 수 있는 나라가 (좌표 포함) 2개 이상이라면 국경선을 연다.
# 3) 모든 좌표에서 국경선을 1개도 열지 못했다면 중단

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    visited[x][y] = True
    q = deque()
    kingdom = [(x, y)] #국경선을 공유하는 국가들의 모임
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이미 방문했거나 벗어난 좌표인 경우
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]:
                continue
            if L <= abs(board[x][y] - board[nx][ny]) <= R:
                q.append((nx, ny))
                visited[nx][ny] = True
                kingdom.append((nx, ny))

    return kingdom

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

result = 0 #인구 이동이 며칠동안 발생했는지
while True:
    # print(board)
    visited = [[False] * N for _ in range(N)]
    is_open = False #국경선이 한번이라도 열렸는가
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            kingdom = bfs(i, j)
            # 국경선을 공유할 국가가 없는 경우
            if len(kingdom) == 1:
                continue
            # 국경선을 공유할 국가가 있는 경우
            is_open = True
            sum_value = 0
            for x, y in kingdom:
                sum_value += board[x][y]
            # 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)
            population = int(sum_value / len(kingdom))
            # 국경선 열어서 인구 이동
            for x, y in kingdom:
                board[x][y] = population

    if is_open:
        result += 1
    else:
        print(result)
        break

