from collections import deque

def bfs(v, visited):
    q = deque()
    visited[v] = 1
    q.append((v, 1))

    while q:
        v, value = q.popleft()
        for n in graph[v]:
            #아직 방문하지 않은 인접한 노드라면
            if visited[n] == 0:
                visited[n] = value * -1
                q.append((n, value * -1))
            #인접한 곳의 값이 같은 경우
            elif visited[n] == value:
                return False

    return True

for tc in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)

    visited = [0] * (v + 1)
    is_binary_graph = True
    for i in range(1, v + 1):
        if visited[i] == 0:
            if bfs(i, visited) == False:
                is_binary_graph = False
                break

    if is_binary_graph:
        print('YES')
    else:
        print('NO')