import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

start = int(input()) #출발 노드
#간선 정보 입력 받기
for i in range(m):
     a, b, cost = map(int, input().split())
     graph[a].append((b, cost)) #a -> b 비용 cost

def dijkstra(start):
     q = []
     heapq.heappush(q, (0, start))
     distance[start] = 0

     while q:
          dist, now = heapq.heappop(q)

          if distance[now] < dist:
               continue

          for i in graph[now]:
               cost = dist + i[1] #now -> adj_node
               if cost < distance[i[0]]:
                    heapq.heappush(q, (cost, i[0]))
                    distance[i[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
     if distance[i] == INF:
          print('INF')
     else:
          print(distance[i])