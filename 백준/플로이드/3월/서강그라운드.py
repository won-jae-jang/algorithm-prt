n, m, r = map(int, input().split()) #노드, 수색범위, 간선의 개수
items = list(map(int, input().split()))
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(r):
     a, b, c = map(int, input().split())
     graph[a][b] = c
     graph[b][a] = c

for i in range(1, n + 1):
     for j in range(1, n + 1):
          if i == j:
               graph[i][j] = 0

for k in range(1, n + 1):
     for a in range(1, n + 1):
          for b in range(1, n + 1):
               graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
for i in range(1, n + 1):
     temp = 0
     for j in range(1, n + 1):
          if graph[i][j] <= m:
               temp += items[j - 1]

     result = max(result, temp)

print(result) 