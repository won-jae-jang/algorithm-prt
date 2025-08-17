from collections import deque
N, M = map(int, input().split())
INF = int(1e10)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def bfs(weight):
    q = deque()
    q.append(one)
    visited = [False] * (N + 1)
    visited[one] = True

    while q:
        now = q.popleft()
        for next_node, cost in graph[now]:
            if not visited[next_node] and cost >= weight:
                q.append(next_node)
                visited[next_node] = True

    if visited[two]:
        return True
    return False

one, two = map(int, input().split()) #출발, 목적지
start = 1
end = 1000000000
result = 0
while start <= end:

    mid = (start + end) // 2 #찾고자 하는 최대 중량

    if bfs(mid):
        result = mid
        start = mid + 1 #현재 중량으로 운행 가능하면 더 무겁게
    else:
        end = mid - 1 #현재 중량으로 운행 못하면 더 가볍게

print(result)