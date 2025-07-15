import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline

def dfs(v, group):
    global result

    if result == False:
        return

    visited[v] = group
    for i in graph[v]:
        if not visited[i]:
            dfs(i, -group)
        #인접한 노드가 같은 그룹에 속한 경우
        elif visited[i] == visited[v]:
            result = False
            return

for tc in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [False] * (v + 1) 
    result = True

    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        if not visited[i]:
            dfs(i, 1)
            if result == False:
                break

    if result:
        print('YES')
    else:
        print('NO')