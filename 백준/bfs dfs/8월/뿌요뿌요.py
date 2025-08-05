#1. 연쇄할 공간을 확인 후 체크
#2. 연쇄가 발생했다면 열 방향으로 옮겨주기
from collections import deque

graph = [list(input()) for _ in range(12)]
result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y, color):
    count = 1 #인접한 같은 색의 뿌요의 개수
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #색이 같은 경우
            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] and graph[nx][ny] == color:
                count += 1
                visited[nx][ny] = True
                q.append((nx, ny))
    return count

#인접한 색상의 푸요를 부수기
def break_puyo(x, y, color):
    visited = [[False] * 6 for _ in range(12)]
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    graph[x][y] = 'break' #부서야 하는 푸요임을 표기
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #색이 같은 경우
            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] and graph[nx][ny] == color:
                visited[nx][ny] = True
                graph[nx][ny] = 'break'
                q.append((nx, ny))

#푸요를 부순후에 열 옮기기
def move_column():
    new_graph = [[0] * 6 for _ in range(12)]
    for y in range(6):
        col = [] #내려가야 하는 칸
        for x in range(12):
            if graph[x][y] != 'break':
                col.append(graph[x][y])
        col = ['.'] * (12 - len(col)) + col #푸요를 부수고 난 빈칸 채우기
        for x in range(12):
            new_graph[x][y] = col[x]

    return new_graph

result = 0
while True:
    visited = [[False] * 6 for _ in range(12)]
    is_break = False #타요가 부서졌는지 여부
    for x in range(12):
        for y in range(6):
            if not visited[x][y] and graph[x][y] != '.':
                count = bfs(x, y, graph[x][y])
                if count >= 4:
                    break_puyo(x, y, graph[x][y])
                    is_break = True
    #더이상 연쇄가 일어나지 않으면
    if not is_break:
        print(result)
        break
    #연쇄가 필요한 경우
    else:
        result += 1
        graph = move_column()
