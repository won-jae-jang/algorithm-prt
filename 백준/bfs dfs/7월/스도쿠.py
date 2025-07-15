
#x 번째 행에 n 값을 삽입할 수 있는가
def row(x, n):
    for i in range(9):
        #이미 스도쿠내에 n값이 존재한다면 삽입할 수 없음
        if graph[x][i] == n:
            return False
    return True
#y 번째 열에 n 값을 삽입할 수 있는가
def column(y, n):
    for i in range(9):
        # 이미 스도쿠내에 n값이 존재한다면 삽입할 수 없음
        if graph[i][y] == n:
            return False
    return True
#3X3 정사각형
def square(x, y, n):
    for i in range(3):
        for j in range(3):
            #3 * 3 영역 내에 삽입할 수가 없는 경우
            if graph[x // 3 * 3 + i][y // 3 * 3 + j] == n:
                return False
    return True

graph = []
pos = [] #채워야 하는 부분
for i in range(9):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        #처리해야 되는 부분
        if data[j] == 0:
            pos.append((i, j))
    graph.append(data)

def dfs(n):
    if n == len(pos):
        for i in graph:
            print(*i)
        exit()

    x, y = pos[n][0], pos[n][1]
    #blank 좌표에서 1~9값중 어느 값이 들어갈 수 있는지 확인
    for i in range(1, 10):
        if row(x, i) and column(y, i) and square(x, y, i):
            graph[x][y] = i
            dfs(n + 1)
            graph[x][y] = 0

dfs(0)