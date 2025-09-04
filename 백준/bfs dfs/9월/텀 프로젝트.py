import sys

sys.setrecursionlimit(100001)

def dfs(x):
    global count
    visited[x] = 1 #현재 방문 중인 노드
    parent = graph[x]
    cycle.append(x)
    #방문 하지 않은 경우
    if not visited[parent]:
        dfs(parent)
    #사이클이 발생한 경우
    elif visited[parent] == 1:
        count += len(cycle[cycle.index(parent):])

    visited[x] = 2 #방문 처리가 완료된 노드

for tc in range(int(input())):
    n = int(input())
    visited = [0] * (n + 1)
    graph = [0] + list(map(int, input().split()))
    result = n
    count = 0
    for i in range(1, n + 1):
        cycle = []
        if not visited[i]:
            dfs(i)


    print(result - count)