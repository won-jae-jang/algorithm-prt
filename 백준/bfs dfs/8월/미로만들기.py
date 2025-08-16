import heapq
n = int(input())
graph =[list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    visited = [[False] * n for _ in range(n)]
    q = []
    heapq.heappush(q, (0, 0, 0))
    visited[0][0] = True
    while q:
        cost, x, y = heapq.heappop(q)

        if x == n - 1 and y == n - 1:
            return cost

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                #방문 가능한 흰방인 경우
                if graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    heapq.heappush(q, (cost, nx, ny))
                #방문 가능한 검은 방
                else:
                    visited[nx][ny] = True
                    heapq.heappush(q, (cost + 1, nx, ny))

print(bfs())