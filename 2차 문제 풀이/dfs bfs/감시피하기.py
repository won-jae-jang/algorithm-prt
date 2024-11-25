from itertools import combinations

n = int(input())
array = [['X'] * n for _ in range(n)] #바꾸지 않을 원본 맵
data = [['X'] * n for _ in range(n)] #장애물을 설치해 나가면서 바뀌는 맵

blocks = []
teachers = []
for i in range(n):
    temp = list(input().split())
    for j in range(n):
        #학생 위치 표기
        if temp[j] == 'S':
            array[i][j] = 'S'
        #선생님 위치 표기
        elif temp[j] == 'T':
            array[i][j] = 'T'
            teachers.append((i, j))
        #장애물을 설치할 수 있는 좌표
        else:
            blocks.append((i, j))

#상 하 좌 우
def watch(x, y, direction):
    #위쪽 방향으로 감시
    if direction == 0:
        while x >= 0:
            if array[x][y] == 'S':
                return True
            if array[x][y] == 'O':
                return False
            x -= 1
    
    #아래쪽 방향으로 감시
    if direction == 1:
        while x < n:
            if array[x][y] == 'S':
                return True
            if array[x][y] == 'O':
                return False
            x += 1

    #왼쪽 방향으로 감시
    if direction == 2:
        while y >= 0:
            if array[x][y] == 'S':
                return True
            if array[x][y] == 'O':
                return False
            y -= 1            
    
    #오른쪽 방향으로 감시
    if direction == 3:
        while y < n:
            if array[x][y] == 'S':
                return True
            if array[x][y] == 'O':
                return False
            y += 1            

    return False
    
def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False
for case in list(combinations(blocks, 3)):
    #장애물 설치
    for cx, cy in case:
        array[cx][cy] = 'O' 
    #선생님이 학생을 발견하지 못한 경우
    if not process():
        find = True
        break
    #장애물 제거
    for cx, cy in case:
        array[cx][cy] = 'X' 

if find:
    print('YES')
else:
    print('NO')