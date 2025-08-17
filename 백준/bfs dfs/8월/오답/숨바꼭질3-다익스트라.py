import heapq
n, k = map(int, input().split())
INF = 1e10
distance = [INF] * 100001

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for next_node in [now - 1, now + 1, now * 2]:
            if next_node < 0 or next_node >= 100001:
                continue
            if next_node == now * 2:
                cost = dist
            else:
                cost = dist + 1
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

dijkstra(n)
print(distance[k])
