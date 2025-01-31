from collections import deque
import sys
input = sys.stdin.readline

move = [
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2), (1, 2),
    (2, -1), (2, 1)
]

for tc in range(int(input())):
    n = int(input())
    graph = [[0] * n for _ in range(n)]
    x, y = map(int, input().split()) #시작 위치
    tx, ty = map(int, input().split()) #도착 위치

    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        if x == tx and y == ty:
            break

        for i in range(8):
            nx = x + move[i][0]
            ny = y + move[i][1]
            if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

    print(graph[tx][ty])