from collections import deque
r, c = map(int, input().split())
graph = []
water = deque()
x = y = 0 #고슴도치 초기 위치
for i in range(r):
    data = list(input())
    graph.append(data)
    for j in range(c):
        if data[j] == 'S':
            x, y = i, j
        elif data[j] == '*':
            water.append((i, j))

visited = [[False] * c for _ in range(r)]
q = deque()
q.append((x, y, 0)) #고슴도치 초기위치
visited[x][y] = True
result = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while q:
    #물 퍼짐
    for _ in range(len(water)):
        wx, wy = water.popleft()
        for i in range(4):
            nx = wx + dx[i]
            ny = wy + dy[i]
            #비어있는 인접한 칸
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.':
                graph[nx][ny] = '*'
                water.append((nx, ny))

    #고슴도치 갈 수 있는 좌표 확인
    for _ in range(len(q)):
        x, y, time = q.popleft()
        # print(x, y)
        #비버집에 도착한 경우
        if graph[x][y] == 'D':
            print(time)
            exit()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 방문 x & 비어있는 인접한 칸이거나 비버집인 경우
            if 0 <= nx < r and 0 <= ny < c and (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, time + 1))

print('KAKTUS')







