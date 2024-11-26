from collections import deque

n, k = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split()) #s초가 지난 후에 x, y에 존재하는 바이러스 종류

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
#바이러스 크기가 작은 순서대로 큐에 삽입 -> (type, (x, y), time) sort 
def bfs(graph):
    temp = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                temp.append((graph[i][j], (i, j), 0))
    temp.sort() #초기의 바이러스 전염 순서
    q = deque(temp) # [(type, (1, 2), time), (type, (2, 3), time) ..]
    # print('q: ',q)
        
    while q:
        type, pos, time = q.popleft()
        # print('pop: ', type, pos, time)
        vx, vy = pos[0], pos[1] #현재 바이러스 위치
        # print(x, y, vx, vy, time, s)
        if x == vx + 1 and y == vy + 1:
            if time <= s:
                return type
            else:
                return 0
        #바이러스 전이
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = type
                    q.append((type, (nx, ny), time + 1))
                    # print('input: ', (type, (nx, ny), time + 1))

print(bfs(graph))