from collections import deque
n, l, r = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

def open_board(united):
    united_count = 0
    for x, y in united:
        united_count += data[x][y]
    population = united_count // len(united)
    for x, y in united:
        data[x][y] = population

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def process(x, y, index):

    united = [(x, y)] #연합 국가
    q = deque()
    q.append((x, y))
    summary = data[x][y] #현재 연합의 총 인원
    count = 1 #현재 연합의 총 개수
    union[x][y] = index #연합의 표시
    #bfs
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(data[x][y] - data[nx][ny]) <= r:
                    q.append((nx, ny))
                    summary += data[nx][ny]
                    union[nx][ny] = index
                    count += 1
                    united.append((nx, ny))
    #국경선 개방
    for x, y in united:
        data[x][y] = summary // count
    return count

total_count = 0
while True:
    union = [[-1] *n for _ in range(n)]
    index = 0 #연합 번호
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
        
    if index == n * n:
        break
    total_count += 1

print(total_count)