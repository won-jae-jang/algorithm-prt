# 지훈이는 행이 0이거나 r - 1 혹은 열이 0 또는 c - 1일 경우 탈출 할 수 있음
# 불 번짐 -> 지훈이 이동 가능 경로 파악 (하나의 bfs 에서 진행)
# - 불은 벽과 불이 난 공간이 아니면 번짐
# 결과는 time + 1 (탈출에 시간 소요)
from collections import deque

R, C = map(int, input().split())
graph = []
fq = deque()
jx = jy = 0
for i in range(R):
    data = list(input())
    graph.append(data)
    for j in range(C):
        #불의 초기 좌표
        if data[j] == 'F':
            fq.append((i, j))
        #지훈이의 초기 좌표
        elif data[j] == 'J':
            jx, jy = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * C for _ in range(R)] #지훈이의 방문 표시
def bfs(fq, jx, jy):
    jq = deque()
    jq.append((0, jx, jy,))
    visited[jx][jy] = True
    while jq:
        fq = fire(fq) #불번짐

        for _ in range(len(jq)):
            time, jx, jy = jq.popleft()
            # 지훈이가 가장자리에 있는 경우 탈출
            if jx == 0 or jx == R - 1 or jy == 0 or jy == C - 1:
                return time + 1
            for i in range(4):
                nx = jx + dx[i]
                ny = jy + dy[i]
                # 지훈이는 방문하지 않았고 지나갈 수 있는 공간인 경우 진입
                if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == '.' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    jq.append((time + 1, nx, ny))

    return -1

# 해당 step의 불번짐
def fire(fq):
    next_fq = deque()
    while fq:
        fx, fy = fq.popleft()
        for i in range(4):
            nx = fx + dx[i]
            ny = fy + dy[i]
            # 다음 좌표가 벽과 다른 불이 아닌 경우 번짐
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != 'F' and graph[nx][ny] != '#':
                graph[nx][ny] = 'F'
                next_fq.append((nx, ny)) #새로운 불의 좌표
    return next_fq

result = bfs(fq, jx, jy)
if result == -1:
    print("IMPOSSIBLE") #큐를 모두 회전할 때까지 탈출구를 못찾은 경우 (불이 다 번짐)
else:
    print(result)

