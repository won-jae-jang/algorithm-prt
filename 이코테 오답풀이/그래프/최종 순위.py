from collections import deque

for tc in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    indegree = [0] * (n + 1)
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n):
            indegree[array[j]] += 1
            graph[array[i]][array[j]] = True

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    result = []
    cycle = False
    certain = True
    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            certain = False
            break
        now = q.popleft()
        result.append(now)
        for j in range(1, n + 1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print('IMPOSSIBLE')
    elif not certain:
        print('?')
    else:
        for x in result:
            print(x, end=' ')
        print()