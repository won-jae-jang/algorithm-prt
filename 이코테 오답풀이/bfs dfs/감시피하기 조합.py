from itertools import combinations

#dfs
n = int(input())
graph = []
teacher_info = []
empty = []
for i in range(n):
    data = input().split()
    for j in range(n):
        if data[j] == 'T':
            teacher_info.append((i, j))
        elif data[j] == 'X':
            empty.append((i, j))
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
for case in combinations(empty, 3):
    #장애물 설치
    for cx, cy in case:
        graph[cx][cy] = 'O'
    hide = 0
    for tx, ty in teacher_info:
        for dir in range(4):
            if not watch(tx, ty, dir):
                hide += 1
    #모든 경우의 수에서 학생을 발견하지 못한 경우
    if hide == len(teacher_info) * 4:
        result = True
        break
    #장애물 제거
    for cx, cy in case:
        graph[cx][cy] = 'X'

if result:
    print('YES')
else:
    print('NO')