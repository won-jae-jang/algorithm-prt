from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cheeze = 0
for i in range(n):
    cheeze += board[i].count(1) #치즈의 개수 세기

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs():
    q = deque([(0, 0)]) #공기의 초기 좌표
    melt_cheeze = [] #녹일 치즈의 좌표
    temp = [[0] * m for _ in range(n)] #치즈가 공기를 접한 개수를 표기
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m) and not visited[nx][ny]:
                #치즈인 경우
                if board[nx][ny] == 1:
                    temp[nx][ny] += 1
                #공기인 경우 큐에 추가
                else:
                    visited[nx][ny] = True #방문처리
                    q.append((nx, ny))

    # print(temp)
    #치즈가 공기를 2개이상 접하면 녹여야 함
    for i in range(n):
        for j in range(m):
            if temp[i][j] >= 2:
                melt_cheeze.append((i, j))
                board[i][j] = 0 #치즈를 녹임

    return len(melt_cheeze) #녹인 치즈의 개수를 리턴    

width = 0 #녹인 치즈의 수
result = 0
while True:
    visited = [[False] * m for _ in range(n)]
    melt = bfs()
    result += 1 #시간 증가
    width += melt #녹인 치즈의 수 증가
    #녹인 치즈의 수가 원래 치즈의 수와 같으면 종료
    if width == cheeze:
        print(result)
        break