from collections import deque
N, M = map(int, input().split())
ladder = dict()
snake = dict()
for i in range(N):
    x, y = map(int, input().split())
    ladder[x] = y

for i in range(M):
    x, y = map(int, input().split())
    snake[x] = y

q = deque()
q.append((1, 0)) #x, 주사위 굴린 횟수
visited = [False] * (101)
while q:
    x, count = q.popleft()
    if x == 100:
        print(count)
        break

    for dice in range(1, 7):
        nx = x + dice
        if nx > 100 or visited[nx]:
            continue

        if nx in ladder.keys():
            nx = ladder[nx]

        if nx in snake.keys():
            nx = snake[nx]

        if nx <= 100 and not visited[nx]:
            visited[nx] = True
            q.append((nx, count + 1))