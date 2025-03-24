import heapq

m, n = map(int, input().split())
board = []
INF = int(1e9)
distance = [[INF] * m for _ in range(n)]
for i in range(n):
     board.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dijsktra(x, y):

     distance[x][y] = 0
     q = []
     heapq.heappush(q, (0, x, y))

     while q:
          dist, x, y = heapq.heappop(q)

          if distance[x][y] < dist:
               continue

          for i in range(4):
               nx = x + dx[i]
               ny = y + dy[i]

               if (0 <= nx < n) and (0 <= ny < m):
                    if board[nx][ny] == 1:
                         cost = dist + 1
                    else:
                         cost = dist

                    if cost < distance[nx][ny]:
                         distance[nx][ny] = cost
                         heapq.heappush(q, (cost, nx, ny))

dijsktra(0, 0)
print(distance[n - 1][m - 1])