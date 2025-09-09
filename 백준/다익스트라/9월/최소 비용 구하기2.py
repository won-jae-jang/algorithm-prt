import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
INF = 1e10
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

start, end = map(int, input().split())
path = [-1] * (n + 1) #i 노드의 부모노드는 -1로 초기화
path[start] = start
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue

        for next_node, next_cost in graph[now]:
            cost = dist + next_cost
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
                path[next_node] = now #next node의 부모노드는 now

dijkstra(start)
now = end
result = [now]
while start != now:
    now = path[now]
    result.append(now)

print(distance[end])
print(len(result))
print(*result[::-1])