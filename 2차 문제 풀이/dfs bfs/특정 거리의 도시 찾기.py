from collections import deque
n, m, k, x = map(int, input().split()) #도시, 도로, 거리, 출발 도시
graph = [[] for _ in range(n + 1)]
for i in range(m):
    #a -> b 비용 1
    a, b = map(int, input().split())
    graph[a].append(b)

result = []
def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    cost = 0
    while q:
        v = q.popleft()
        print(v, end=' ')
        if cost == k:
            result.append(v)
            continue
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
        cost += 1

visited = [False] * (n + 1)
bfs(graph, x, visited)
print(result)