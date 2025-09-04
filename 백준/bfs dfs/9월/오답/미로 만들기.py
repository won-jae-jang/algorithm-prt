# 1. 흰색방과 검은색방 숫자 바꾸기 (최솟값 탐색을 위해) 1 -> 0, 0 -> 1
# 2. 방문했지만 cost(검은 벽을 통과한 횟수) 가 작으면 방문 허용 & 값 변경

from collections import deque
import copy
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
# 0, 1 뒤집기
for i in range(n):
    for j in range(n):
        graph[i][j] = 0 if graph[i][j] == 1 else 1

q = deque()
q.append((0, 0, 0)) #x, y, cost
visited = [[False] * n for _ in range(n)]
visited[0][0] = True
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
temp = copy.deepcopy(graph)
result = 1e10
while q:
    x, y, cost = q.popleft()
    if x == n - 1 and y == n - 1:
        # print(cost)
        result = min(result, cost)
        continue

    for i in range(4):
        next_cost = cost
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            #검은방인 경우 (흰색 방인 경우 비용 변화 없음)
            if graph[nx][ny] == 1:
                next_cost += 1
            #방문하지 않았을 경우
            if not visited[nx][ny]:
                visited[nx][ny] = True
                temp[nx][ny] = next_cost #방문처리
                q.append((nx, ny, next_cost))
            #방문 했는데 최소 비용인 경우
            elif next_cost < temp[nx][ny]:
                temp[nx][ny] = next_cost #최소값 갱신
                q.append((nx, ny, next_cost))

print(result)
