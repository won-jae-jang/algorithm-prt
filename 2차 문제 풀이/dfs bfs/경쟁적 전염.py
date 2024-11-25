from collections import deque

n, k = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split()) #s초가 지난 후에 x, y에 존재하는 바이러스 종류

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
#todo 
#바이러스 크기가 작은 순서대로 큐에 삽입 -> (type, (x, y)) sort 
#시간 측정 ? -> 큐에 함께 삽입
def bfs(graph):
    temp = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                temp.append([graph[i][j], [i, j]])
    temp.sort() #초기의 바이러스 전염 순서
    q = deque(temp) # [(1, 2), (2, 3) ..]
    print('q: ',q)
    time = 0
    while True:
        if time == s:
            print(graph[x - 1][y - 1])
            break
        
        temp = []
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < n and ny >= 0 and ny < n:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y]
                        temp.append([nx, ny])
        time += 1
        q.append(temp)

bfs(graph)