v, e = map(int, input().split())
INF = int(1e9)
grpah = [[INF] * (v + 1) for _ in range(v + 1)]

for i in range(e):
     a, b, c = map(int, input().split())
     grpah[a][b] = c

for k in range(1, v + 1):
     for a in range(1, v + 1):
          for b in range(1, v + 1):
               grpah[a][b] = min(grpah[a][b], grpah[a][k] + grpah[k][b])

result = INF
for i in range(1, v + 1):
     for j in range(1, v + 1):
          if i == j:
               result = min(result, grpah[i][j])

if result == INF:
     print(-1)
else:
     print(result)