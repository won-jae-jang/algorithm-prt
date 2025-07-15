from collections import deque
import copy

n = int(input())
fishes = [[] for _ in range(7)] #물고기는 1 ~ 6 크기임
x, y = 0, 0 #아기 상어의 위치
graph = []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        #물고기인 경우
        if (1 <= data[j] <= 6):
            #물고기 크기에 맞춰 좌표 저장
            fishes[data[j]].append((i, j)) 

        #아기 상어인 경우
        elif data[j] == 9:
            x, y = i, j

    graph.append(data)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#목적지 
def bfs(x, y):
    q = deque([(x, y, 0)]) #상어의 위치(x, y), 소요시간
    distance = [[-1] * n for _ in range(n)]
    eatable = [] #먹을 수 있는 물고기
    distance[x][y] = 0
    while q:
        x, y, time = q.popleft()
        #먹을 수 있는 물고기라면
        if (1 <= graph[x][y] < baby_shark):
            eatable.append((x, y, time))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #범위에 부합하고 해당 영역이 아기 상어보다 작은 경우
            if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny] <= baby_shark and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1 #방문처리
                q.append((nx, ny, time + 1))

    return eatable

baby_shark = 2 #아기 상어의 크기
graph[x][y] = 0 
count = 0 #아기 상어가 먹은 물고기 수
time = 0
while True:

    #상어가 자기의 크기수 만큼 물고기를 잡아먹은 경우
    if baby_shark == count:
        baby_shark += 1
        count = 0

    result = bfs(x, y)

    #먹을 수 있는 물고기가 없는 경우
    if len(result) == 0:
        print(time)
        break
    
    result.sort(key=lambda x: (x[2], x[0], x[1])) #거리, x, y 가 짧은 순으로 정렬
    nx, ny, distance = result.pop(0)
    x, y = nx, ny #상어의 위치 변경
    graph[x][y] = 0 #가장 짧은 경로의 물고기를 잡아먹음 
    count += 1 #먹은 물고기 수 증가
    time += distance