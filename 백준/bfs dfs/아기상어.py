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

def find_shortest_way():
    global x, y #상어의 좌표

    pos = []
    #상어의 크기보다 작은 물고기들의 좌표
    for size in range(1, 7):
        if size < baby_shark:
            for fx, fy in fishes[size]:
                pos.append((fx, fy, size))

    # print('check: ', fishes, baby_shark, eatable)
    time = 401 #가장 짧은 거리를 이동하는데 걸린 시간
    temp = copy.deepcopy(graph)
    shortest = [] #거리가 가장 짧은 물고기들
    bfs(temp)
    # print('pos: ', pos)
    for nx, ny, size in pos:
        #먹을 수 있는 물고기의 시간의 더 짧은 경우
        if temp[nx][ny] < time:
            shortest = []
            time = temp[nx][ny]
            shortest.append((nx, ny, size))

        #걸리는 최소 시간이 동일한 경우
        elif temp[nx][ny] == time:
            shortest.append((nx, ny, size))

    if len(shortest) > 1:
        #정렬 (x, y가 작은 순서대로)
        # shortest.sort(key=lambda x: (x[0], x[1])) 
        shortest.sort() 
    
    print('shortest: ', shortest)
    x, y, size = shortest[0][0], shortest[0][1], shortest[0][2]
    graph[x][y] = 0 #해당 영역의 물고기를 잡아 먹음
    # print('제거전: ', fishes, fishes[baby_shark - 1], x, y)
    fishes[size].remove((x, y)) #먹은 물고기 사라짐
    # print('제거후: ', fishes)
    return time
    
#목적지 
def bfs(graph):
    global x, y
    q = deque([(x, y, 0)]) #상어의 위치
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y, time = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #범위에 부합하고 해당 영역이 아기 상어보다 작은 경우
            if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny] <= baby_shark and not visited[nx][ny]:
                visited[nx][ny] = True #방문처리
                graph[nx][ny] = time + 1 #이동 시간 
                q.append((nx, ny, time + 1))

#상어가 먹을 수 있는 물고기 수
def count_fish():
    count = 0
    for size in range(1, 7):
        if size < baby_shark:
            count += len(fishes[size])

    return count

baby_shark = 2 #아기 상어의 크기
count = 0 #아기 상어가 먹은 물고기 수
eatable = len(fishes[1]) #아기 상어가 먹을 수 있는 물고기 수
time = 0
while True:
    #아기 상어가 크기만큼 물고기를 먹은 경우
    if baby_shark == count:
        baby_shark += 1
        eatable = count_fish()
        count = 0
    #더이상 먹을 물고기가 없는 경우
    if eatable == 0:
        break

    #먹을 수 있는 물고기가 1마리이상
    elif eatable >= 1:
        count += 1 #물고기 섭취
        time += find_shortest_way()
        eatable -= 1 #먹을 수 있는 물고기 수 감소

# print(fishes)
print(time)