v = int(input()) #정점 개수
e = int(input()) #간선 개수

graph = [[] for _ in range(v + 1)]
visited = [False] * (v + 1)
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, visited, v):
    visited[v] = True #감염
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)
            
dfs(graph, visited, 1)
width = 0
for i in range(2, v + 1):
    if visited[i] == True:
        width += 1

print(width)