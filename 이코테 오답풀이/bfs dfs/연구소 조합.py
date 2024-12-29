from itertools import combinations

#dfs
n, m = map(int, input().split())
graph = []
temp = [[0] * m for _ in range(n)]
virus_info = []
empty = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(m):
        if data[j] == 2:
            virus_info.append((i, j))
        elif data[j] == 0:
            empty.append((i, j))
    graph.append(data)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def virus(x, y):
    #상하좌우로 전이
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #범위 내에 있다면
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2 #바이러스 전이
                virus(nx, ny)

def get_score(graph):
    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                result += 1
    return result

answer = 0
for case in combinations(empty, 3):
    #기둥 설치
    for cx, cy in case:
        graph[cx][cy] = 1
    #맵 복사
    for i in range(n):
        for j in range(m):
            temp[i][j] = graph[i][j]
    #dfs 
    for vx, vy in virus_info:
        virus(vx, vy)
    answer = max(get_score(temp), answer)
    #기둥 제거
    for cx, cy in case:
        graph[cx][cy] = 0
    
print(answer)