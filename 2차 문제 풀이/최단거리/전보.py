import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline

n, m, start = map(int, input().split()) #도시의 개수, 통로의 개수, 시작 도시
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
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
    if distance[i] != INF and distance[i] != 0:
        count += 1
        time = max(time, distance[i])

print(count, time)