import sys
import heapq

result = []
INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while True:
     n = int(input())
     if n == 0:
          break

     graph = []
     for i in range(n):
          graph.append(list(map(int, input().split())))

     distance = [[INF] * (n) for _ in range(n)]
     distance[0][0] = graph[0][0]

     q = []
     heapq.heappush(q, (graph[0][0], 0, 0))
     while q:
          dist, x, y = heapq.heappop(q)

          if distance[x][y] < dist:
               continue

          for i in range(4):
               nx = x + dx[i]
               ny = y + dy[i]

               if (0 <= nx < n) and (0 <= ny < n):
                    cost = dist + graph[nx][ny]
                    if cost < distance[nx][ny]:
                         distance[nx][ny] = cost
                         heapq.heappush(q, (cost, nx, ny))

     result.append(distance[n - 1][n - 1])

for i in range(len(result)):
     print(f'Problem {i + 1}: {result[i]}')