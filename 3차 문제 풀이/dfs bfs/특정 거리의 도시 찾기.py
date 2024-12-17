from collections import deque

n, m, k, x = map(int, input().split()) #도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


result = []
q = deque([(x, 0)]) #도시 번호, 거리
visited[x] = True
while q:
    now, dist = q.popleft()
    if dist == k:
        result.append(now)
    for v in graph[now]:
        if not visited[v]:
            q.append((v, dist + 1))
            visited[v] = True

result.sort()
if len(result) != 0:
    for x in result:
        print(x)
else:
    print(-1)