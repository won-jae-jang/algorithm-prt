import sys
from itertools import combinations

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)] #(node, weight)
for i in range(n - 1): 
    #parent <-> child 비용이 weight
    parent, child, weight = map(int, input().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))
    
def dfs(v, total):
    visited[v] = total
    
    for node, weight in graph[v]:
        #방문하지 않았다면
        if visited[node] == -1:
            dfs(node, total + weight)

visited = [-1] * (n + 1)
dfs(1, 0)
max_distance = max(visited)
max_node = visited.index(max_distance)

visited = [-1] * (n + 1)
dfs(max_node, 0)
print(max(visited))