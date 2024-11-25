from itertools import combinations

n, m = map(int, input().split()) #row ,col
data = [] #원본 지도
temp = [[0] * m for _ in range(n)] #벽을 설치한 지도
blanks = []
virus = []
for i in range(n):
    info = list(map(int, input().split()))
    for j in range(m):
        if info[j] == 0: #빈칸 좌표
            blanks.append((i, j))
        elif info[j] == 2: #바이러스 좌표
            virus.append((i, j))
    data.append(info)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(row, col):
    for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]
        #그래프 범주를 벗어나지 않고, 빈칸인 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                dfs(nx, ny)


def safe_space(graph):
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1
    return count

result = -1
for case in list(combinations(blanks, 3)):
    #맵 복사
    for i in range(n):
        for j in range(m):
            temp[i][j] = data[i][j]
    #3개의 기둥 설치
    for x, y in case:
        temp[x][y] = 1
    #바이러스 전이 시뮬레이션
    for vx, vy in virus:
        dfs(vx, vy)

    result = max(result, safe_space(temp))

print(result)