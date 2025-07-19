from collections import deque

n = int(input())
graph = []
shark_x = 0
shark_y = 0
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        #아기 상어의 초기 위치
        if data[j] == 9:
            shark_x, shark_y = i, j
            data[j] = 0 #물고기로 오인할 수 있으므로 빈칸 처리
    graph.append(data)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    dist = 0 #이동 거리
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True #초기 상어의 위치 방문 처리
    q.append((x, y, dist))
    eatable_fishes = []
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                #아기 상어보다 크기가 더 큰 물고기는 통과할 수 없음
                if graph[nx][ny] > shark_size:
                    visited[nx][ny] = True
                    continue
                #아기 상어와 크기가 같은 물고기는 통과할 수 있음
                elif graph[nx][ny] == shark_size:
                    q.append((nx, ny, dist + 1))
                    visited[nx][ny] = True
                #아기 상어가 먹을 수 있는 물고기인 경우
                elif 1 <= graph[nx][ny] < shark_size:
                    q.append((nx, ny, dist + 1))
                    visited[nx][ny] = True
                    eatable_fishes.append((dist + 1, nx, ny))
                #빈칸인 경우
                else:
                    q.append((nx, ny, dist + 1))
                    visited[nx][ny] = True

    return eatable_fishes

shark_size = 2 #아기 상어의 크기
width = 0 #아기 상어가 먹은 물고기의 수
time = 0 #아기 상어 이동 시간
while True:
    #bfs: 먹을 수 있는 물고기 들을 반환 (거리, x, y) 순으로
    fishes = bfs(shark_x, shark_y)
    # print(fishes)
    #먹을 수 있는 물고기가 없는 경우
    if len(fishes) == 0:
        print(time)
        break
    #먹을 수 있는 물고기가 1개 이상인 경우
    else:
        fishes.sort()
        dist, fx, fy = fishes.pop(0)
        width += 1 #물고기 먹은 개수 카운팅
        time += dist
        shark_x, shark_y = fx, fy #물고기 먹을 위치로 이동
        graph[fx][fy] = 0 #물고기 먹어 치우기

    #아기 상어 크기 커지는 조건
    if width == shark_size:
        shark_size += 1
        width = 0






