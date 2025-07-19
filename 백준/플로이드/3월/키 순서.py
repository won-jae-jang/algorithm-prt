n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(m):
     a, b = map(int, input().split())
     graph[a][b] = 1

for i in range(1, n + 1):
     for j in range(1, n + 1):
          if i == j:
               graph[i][j] = 0

for k in range(1, n + 1):
     for a in range(1, n + 1):
          for b in range(1, n + 1):
               graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

width = 0
for i in range(1, n + 1):
     temp = 0
     for j in range(1, n + 1):
          if graph[i][j] != INF or graph[j][i] != INF:
               temp += 1

     if temp == n:
          width += 1

print(width)