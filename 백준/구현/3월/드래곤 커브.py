import sys
input = sys.stdin.readline

board = [[0] * 101 for _ in range(101)]
n = int(input())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for _ in range(n):
    x, y, d, g = map(int, input().split())
    curb = [d] #초기 드래곤 커브
    board[x][y] = 1 #방문처리

    for _ in range(g):
        for i in range(len(curb) - 1, -1, -1):
            curb.append((curb[i] + 1) % 4) #90도 회전시킴

    for i in curb:
        x += dx[i]
        y += dy[i]
        board[x][y] = 1

result = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]:
            result += 1

print(result)