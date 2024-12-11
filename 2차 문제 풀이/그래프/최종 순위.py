from collections import deque

for tc in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    indegree = [0] * (n + 1)
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    #차수 초기화
    for i in range(n - 1): #n
        for j in range(i + 1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1


    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        # a -> b 즉, a 의 순위가 b 의 순위보다 높은 경우
        if graph[a][b]:
            graph[b][a] = True
            graph[a][b] = False
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[b][a] = False
            graph[a][b] = True
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    certain = False #위상 정렬 결과가 오로지 하나인가 -> print(?)
    cycle = False #그래프 내 사이클 존재하는가 -> print(impossible)
    
    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        
        if len(q) >= 2:
            certain = True
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
    elif certain:
        print('?')
    else:
        for i in result:
            print(i, end=' ')
        print()