import heapq

n = int(input())
m = int(input())
INF = 1e10
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # a->b cost c

start, end = map(int, input().split())
route = [-1] * (n + 1) #출발 -> 도착 경로를 기재
route[start] = start

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for adj_node, adj_weight in graph[now]:
            cost = dist + adj_weight
            if cost < distance[adj_node]:
                distance[adj_node] = cost
                route[adj_node] = now #현재 노드가 최단 거리로 이동하기 위해 선택하는 다음 노드
                heapq.heappush(q, (cost, adj_node))

dijkstra(start)
print(distance[end])

path = [end]
now = end
while start != now:
    now = route[now]
    path.append(now)

path.reverse()
print(len(path))
print(' '.join(map(str, path)))