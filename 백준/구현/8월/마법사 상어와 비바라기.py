N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)] #구름 초기 위치
for _ in range(M):
    direction, s = map(int, input().split())
    direction -= 1
    next = []
    #모든 구름이 di 방향으로 si칸 이동한다.
    for x, y in cloud:
        x = (x + dx[direction] * s) % N
        y = (y + dy[direction] * s) % N
        next.append((x, y))
    # print(next)
    # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
    for x, y in next:
        graph[x][y] += 1

    for x, y in next:
        #대각선 방향으로 거리가 1인 칸에 물이 있는 바구니 수만큼 물 추가
        for i in [1, 3, 5, 7]:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] >= 1:
                graph[x][y] += 1

    #바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    cloud = []
    for x in range(N):
        for y in range(N):
            if graph[x][y] >= 2 and (x, y) not in next:
                cloud.append((x, y))
                graph[x][y] -= 2
    # print(cloud)

result = 0
for i in range(N):
    result += sum(graph[i])
print(result)
