from collections import deque

n, m = map(int, input().split())
board = []
count = 0 #치즈의 개수
for i in range(n):
    data = list(map(int, input().split()))
    board.append(data)
    count += data.count(1) #치즈의 개수 카운트

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs():
    q = deque([(0, 0)])
    melt_cheeze = []

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #방문하지 않은 곳인 경우
            if (0 <= nx < n) and (0 <= ny < m) and not visited[nx][ny]:
                visited[nx][ny] = True
                #빈칸이라면 추가하기
                if board[nx][ny] == 0:
                    q.append((nx, ny))
                #치즈인 경우
                else:
                    melt_cheeze.append((nx, ny))

    for x, y in melt_cheeze:
        #치즈 녹이기
        board[x][y] = 0

    return len(melt_cheeze) #녹인 치즈수 리턴턴

melt_count = 0 #녹은 치즈의 총 개수
time = 0
while True:

    visited = [[False] * m for _ in range(n)]
    melt = bfs() #치즈 녹이기
    time += 1
    melt_count += melt 
    #녹은 치즈수와 초기 치즈수가 같으면 탈출
    if melt_count == count:
        print(time)
        print(melt)
        break