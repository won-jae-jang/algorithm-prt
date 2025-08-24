import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for next_node, next_cost in graph[now]:
            cost = dist + next_cost
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

for tc in range(int(input())):
    n, e, start = map(int, input().split())
    INF = int(1e10)
    distance = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for _ in range(e):
        a, b, s = map(int, input().split())
        # graph[a].append((b, s))
        graph[b].append((a, s))

    dijkstra(start)
    count = dist = 0
    for x in distance:
        if x == INF:
            continue
        count += 1
        dist = max(dist, x)

    print(count, dist)

