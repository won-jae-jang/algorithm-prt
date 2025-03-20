import heapq
import sys
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = int(1e9)

for i in range(e):
     a, b, c = map(int, input().split())
     graph[a].append((b, c))
     graph[b].append((a, c))

start = 1
end = n
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

n1, n2 = map(int, input().split()) #반드시 지나야 하는 두 정점점

result1 = 0
#1 -> n1 -> n2 -> n
result1 += dijkstra(1)[n1] #1 -> n1
result1 += dijkstra(n1)[n2] #n1 -> n2
result1 += dijkstra(n2)[n] #n2 -> n

result2 = 0
#1 -> n2 -> n1 -> n
result2 += dijkstra(1)[n2] #1 -> n2
result2 += dijkstra(n2)[n1] #n2 -> n1
result2 += dijkstra(n1)[n] #n1 -> n

if min(result1, result2) >= INF:
     print(-1)
else:
     print(min(result1, result2))