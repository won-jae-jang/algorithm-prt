import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for i in range(m):
    # x -> y 비용 z
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

#다익스트라
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
count = 0
time = 0
for i in range(1, n + 1):
    if 0 < distance[i] < INF:
        count += 1
        time = max(time, distance[i])

print(count, time)