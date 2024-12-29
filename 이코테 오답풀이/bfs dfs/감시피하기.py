#dfs
n = int(input())
graph = []
teacher_info = []

for i in range(n):
    data = input().split()
    for j in range(n):
        if data[j] == 'T':
            teacher_info.append((i, j))
    graph.append(data)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def watch(x, y, direction):
    while 0 <= x < n and 0 <= y < n:
        if graph[x][y] == 'O':
            return False
        elif graph[x][y] == 'S':
            return True
        x += dx[direction] 
        y += dy[direction] 
    return False

result = False
def dfs(count):
    global result
    for i in range(n):
        for j in range(n):
            #벽을 전부 설치하지 않았다면
            if count != 3:
                if graph[i][j] == 'X':
                    graph[i][j] = 'O'
                    dfs(count + 1)
                    graph[i][j] = 'X'
            #벽을 전부 설치했다면
            elif count == 3:
                hide = 0
                for tx, ty in teacher_info:
                    for dir in range(4):
                        if not watch(tx, ty, dir):
                            hide += 1
                #모든 경우의 수에서 학생을 발견하지 못한 경우
                if hide == len(teacher_info) * 4:
                    result = True

dfs(0)
if result:
    print('YES')
else:
    print('NO')