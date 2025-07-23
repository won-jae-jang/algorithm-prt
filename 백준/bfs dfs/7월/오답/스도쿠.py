graph = []
pos = []
for i in range(9):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(9):
        #채워 줘야 하는 스도쿠 인경우
        if data[j] == 0:
            pos.append((i, j))

#가로 행에 들어갈 수 있는 숫자인가
def row(x, number):
    for i in range(9):
        if graph[x][i] == number:
            return False
    return True

#세로 열에 들어갈 수 있는 숫자인가
def column(y, number):
    for i in range(9):
        if graph[i][y] == number:
            return False
    return True

# 3 * 3 에 들어갈 수 있는 숫자 인가
def rect(x, y, number):
    # row = row % 3 * 3
    # col = col % 3 * 3
    for i in range(3):
        for j in range(3):
            if graph[x // 3 * 3 + i][y // 3 * 3 + j] == number:
                return False
    return True

def dfs(n):
    if n == len(pos):
        for i in graph:
            print(*i)
        exit()

    x, y = pos[n][0], pos[n][1]
    for num in range(1, 10):
        if row(x, num) and column(y, num) and rect(x, y, num):
            graph[x][y] = num
            dfs(n + 1)
            graph[x][y] = 0

dfs(0)