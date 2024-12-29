#dfs
n, m = map(int, input().split())
graph = []
temp = [[0] * m for _ in range(n)]
virus_info = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(m):
        if data[j] == 2:
            virus_info.append((i, j))
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
def dfs(count):
    global answer
    for i in range(n):
        for j in range(m):
            #벽이 아직 다 세워지지 않은 경우
            if count != 3:
                if graph[i][j] == 0:
                    graph[i][j] = 1 #벽 설치
                    dfs(count + 1)
                    graph[i][j] = 0
            #벽이 모두 세워진 경우
            elif count == 3:
                #맵 복사
                for i in range(n):
                    for j in range(m):
                        temp[i][j] = graph[i][j]
                for vx, vy in virus_info:
                    virus(vx, vy)
                answer = max(get_score(temp), answer)
                return

dfs(0)
print(answer)