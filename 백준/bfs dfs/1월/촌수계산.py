import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
p1, p2 = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
m = int(input())
for i in range(m):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

#노드, 촌수
def dfs(v, count):
    global result
    visited[v] = True
    if v == p2:
        result = count
        return
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i, count + 1)

result = 0
dfs(p1, 0)
if result == 0:
    print(-1)
else:
    print(result)