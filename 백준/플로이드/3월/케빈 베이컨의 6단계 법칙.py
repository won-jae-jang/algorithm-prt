n, m = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(m):
     a, b = map(int, input().split())
     graph[a][b] = 1
     graph[b][a] = 1

for i in range(1, n + 1):
     for j in range(1, n + 1):
          if i == j:
               graph[i][j] = 0

for k in range(1, n + 1):
     for a in range(1, n + 1):
          for b in range(1, n + 1):
               graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

kevin = []
min_value = INF
for i in range(1, n + 1):
     temp_kevin = 0
     for j in range(1, n + 1):
          if graph[i][j] != INF:
               temp_kevin += graph[i][j]

     if temp_kevin == min_value:
          kevin.append(i)
     elif temp_kevin < min_value:
          min_value = temp_kevin
          kevin = [i]

print(kevin[0])