n = int(input())
graph = []
teachers = []
students = []
for i in range(n):
    data = list(input().split())
    for j in range(n):
        if data[j] == 'T':
            teachers.append((i, j))
        elif data[j] == 'S':
            students.append((i, j))
    graph.append(data)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def watch(x, y, dir):
    while 0 <= x < n and 0 <= y < n:
        if graph[x][y] == 'O':
            return False
        elif graph[x][y] == 'S':
            return True
        x += dx[dir]
        y += dy[dir]
    return False

avoid = 0
def dfs(count):
    global avoid
    #장애물을 3개 설치한 경우
    if count == 3:
        for tx, ty in teachers:
            #4방향으로 감시
            for i in range(4):
                if watch(tx, ty, i):
                    return
        #모든 선생님의 감시를 피한 경우
        avoid += 1 
    #장애물이 3개가 아닌 경우
    else:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'X':
                    graph[i][j] = 'O' #장애물 설치
                    dfs(count + 1)
                    graph[i][j] = 'X'

dfs(0)
if avoid == 0:
    print('NO')
else:
    print('YES')