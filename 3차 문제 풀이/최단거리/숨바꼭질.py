import heapq

INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())
    # x -> y cost = 1
    graph[x].append((y, 1))
    graph[y].append((x, 1))

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

dijkstra(1)
hide = INF
dist = max(distance[1:])
count = 0 #same
for i in range(1, n + 1):
    if distance[i] == dist:
        count += 1
        if hide == INF:
            hide = i

print(hide, dist, count)