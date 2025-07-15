from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 3차원으로 구성. 첫번째 층은 벽을 부수지 않은 세계. 두번째 층은 벽을 부순 세계
visited = [[[0] * m for _ in range(n)] for _ in range(2)] #[wall][x][y]
# print(visited)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 1

    while q:
        w, x, y = q.popleft()

        if x == n - 1 and y == m - 1:
            return visited[w][x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m):

                #세계와 상관없이 방문할 수 있으면 방문처리
                if visited[w][nx][ny] == 0 and graph[nx][ny] == 0:
                    visited[w][nx][ny] = visited[w][x][y] + 1
                    q.append((w, nx, ny))

                #벽을 부수지 않은 세계에서 더이상 방문할 수 없는 경우, 벽을 부수고 기록
                elif graph[nx][ny] == 1 and w == 0:
                    visited[w + 1][nx][ny] = visited[w][x][y] + 1
                    q.append((w + 1, nx, ny))

    return -1

print(bfs())