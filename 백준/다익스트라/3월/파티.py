import heapq
import sys
input = sys.stdin.readline

n, m, x = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
     a, b, c = map(int, input().split())
     graph[a].append((b, c))

def dijkstra(start):

     distance = [INF] * (n + 1)
     q = []
     distance[start] = 0
     heapq.heappush(q, (0, start))

     while q:
          dist, now = heapq.heappop(q)

          if distance[now] < dist:
               continue

          for i in graph[now]:
               cost = dist + i[1]
               if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

     return distance

back_result = [] #x에서 각각의 집으로 돌아가는 최단 시간
go_result = [0] * (n + 1) #각각의 도시에서 x로 가는 최단 시간
for start in range(1, n + 1):
     temp = dijkstra(start)
     if start == x:
          back_result = [temp[i] for i in range(n + 1)]
     else:
          go_result[start] = temp[x]

result = []
for i in range(n + 1):
     result.append(go_result[i] + back_result[i])

print(max(result[1:]))