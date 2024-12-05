import sys
input = sys.stdin.readline
INF = int(1e9)

#노드, 간선의 개수
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

#간선 정보 입력받기
for _ in range(m):
    # a -> b 비용 c
    a, b, c = map(int, input().split()) 
    graph[a].append((b, c))

def get_smallest_node():
    index = 0
    min_value = INF
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print('inf')
    else:
        print(distance[i])