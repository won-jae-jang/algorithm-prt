import copy

n, m = map(int, input().split())
graph = []
temp = [[0] * m for _ in range(n)]
virus_pos = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        #바이러스 라면
        if data[j] == 2:
            virus_pos.append((i, j))
    graph.append(data)

#안전 영역의 개수를 카운트트
def check(graph):
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1
    return count

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2 #방문 처리
                virus(nx, ny)

def dfs(count):
    global result
    #벽이 다 세워진 경우
    if count == 3:
        #맵 복사
        for a in range(n):
            for b in range(m):
                temp[a][b] = graph[a][b]
        #바이러스 전이이
        for vx, vy in virus_pos:
            virus(vx, vy)
        result = max(result, check(temp))
        return

    #벽을 3개 설치
    for i in range(n):
        for j in range(m):
            #벽이 다 세워지지 않은 경우
            if count != 3:
                if graph[i][j] == 0:
                    graph[i][j] = 1 #벽을 설치
                    dfs(count + 1)
                    graph[i][j] = 0 #벽을 제거
result = 0
dfs(0)
print(result)