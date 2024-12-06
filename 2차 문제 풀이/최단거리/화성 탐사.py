import heapq
t = int(input())

dx = [-1 ,1, 0, 0]
dy = [0, 0, -1, 1]
INF = int(1e9)
for i in range(t):
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    distance = [[INF] * (n) for _ in range(n)]
    q = []
    distance[0][0] = graph[0][0]
    heapq.heappush(q, (graph[0][0], 0, 0)) #dist, (x, y)
    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
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
    