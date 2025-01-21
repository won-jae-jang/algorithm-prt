import sys
input = sys.stdin.readline 

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
 
visited = [False] * (N + 1)
result = [0] * (N + 1)

def dfs(now):
    stack = [now]

    while stack:
        now = stack.pop()
        for i in graph[now]:
            if not visited[i]:
                visited[now] = True
                result[i] = now
                stack.append(i)

visited[1] = True
dfs(1)

for i in range(2, N + 1):
    print(result[i])