import sys 
sys.setrecursionlimit(10000) 

N, M  = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

width = 0
for i in range(1, N + 1):
    if not visited[i]:
        width += 1
        dfs(graph, i, visited)
        
print(width)