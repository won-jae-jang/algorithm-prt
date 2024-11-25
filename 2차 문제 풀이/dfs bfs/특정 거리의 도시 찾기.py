from collections import deque
n, m, k, x = map(int, input().split()) #도시, 도로, 거리, 출발 도시
graph = [[] for _ in range(n + 1)]
dist = [-1] * (n + 1)
for i in range(m):
    #a -> b 비용 1
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(graph, start):
    q = deque([start])
    dist[start] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if dist[i] == -1:
                q.append(i)
                dist[i] = dist[now] + 1

bfs(graph, x)
result = []
for i in range(1, n + 1):
    if dist[i] == k:
        result.append(i)

result.sort()
if len(result) == 0:
    print(-1)
else:
    for r in result:
        print(r)