#https://data-flower.tistory.com/82
from collections import deque

board = [0] * 101
visited = [False] * 101
N, M = map(int, input().split())
ladders = dict()
snakes = dict()

for i in range(N):
    x, y = map(int, input().split())
    ladders[x] = y

for i in range(M):
    x, y = map(int, input().split())
    snakes[x] = y

q = deque()
q.append(1) #초기 좌표

while q:
    x = q.popleft()
    if x == 100:
        print(board[100])
        break
    for dice in range(1, 7):
        nx = x + dice
        if nx <= 100 and not visited[nx]:
            if nx in ladders.keys():
                nx = ladders[nx]

            if nx in snakes.keys():
                nx = snakes[nx]
            #사다리나 뱀을 타고 올라가는 경우가 있을 수 있기 때문에 방문 확인을 2중으로 시행
            if not visited[nx]:
                visited[nx] = True
                board[nx] = board[x] + 1
                q.append(nx)
