import heapq

INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for tc in range(int(input())):
    n = int(input())
    graph = []
    distance = [[INF] * n for _ in range(n)]
    for i in range(n):
        graph.append(list(map(int, input().split())))
    
    q = []
    x, y = 0, 0 #시작 위치
    heapq.heappush(q, (graph[x][y], x, y))
    distance[x][y] = graph[x][y]
    while q:
        dist, x, y = heapq.heappop(q)
        if dist > distance[x][y]:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    
    print(distance[n - 1][n - 1])
    # print(distance)