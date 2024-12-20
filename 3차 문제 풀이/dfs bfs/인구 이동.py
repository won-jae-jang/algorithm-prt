from collections import deque

n, l, r = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
#bfs
def move(visited, graph, x, y):
    q = deque([])
    q.append((x, y))
    count = 1 #연합을 이루고 있는 나라 개수
    sum_value = graph[x][y] #연합의 인구수
    united = [(x, y)] #연합 국가
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #국경을 공유하는 나라 검사
            if 0 <= nx < n and 0 <= ny < n:
                #두 나라의 인구 차이가 L 이상, R 이하라면 연합 추가
                if not visited[nx][ny] and l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    count += 1
                    sum_value += graph[nx][ny]
                    united.append((nx, ny))
                    q.append((nx, ny))
                    visited[nx][ny] = True #방문처리
    
    if count >= 2:
        population = sum_value // count
        #인구 이동
        for a, b in united:
            graph[a][b] = population 
        return True
    else:
        return False

result = 0
while True:
    visited = [[False] * (n) for _ in range(n)]
    moving = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True #방문처리
                if move(visited, graph, i, j):
                    moving = True

    if moving:
        result += 1
    else:
        break

print(result)