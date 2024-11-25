n, m = map(int, input().split()) #row ,col
data = [] #원본 지도
temp = [[0] * m for _ in range(n)] #벽을 설치한 지도
virus = []
for i in range(n):
    data.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def virus(row, col):
    for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]
        #그래프 범주를 벗어나지 않고, 빈칸인 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def safe_space(graph):
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1
    return count

result = -1
def dfs(count):
    global result
    if count == 3:
        #맵 복사
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        #바이러스 전이 시뮬레이션
        for i in range(n):
            for j in range(m):
                if data[i][j] == 2: #바이러스라면
                    virus(i, j)

        result = max(result, safe_space(temp))
        return
    #의자를 설치해야 함
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                count += 1
                data[i][j] = 1
                dfs(count) 
                count -= 1
                data[i][j] = 0

dfs(0)
print(result)