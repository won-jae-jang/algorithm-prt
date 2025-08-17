from collections import deque
n, k = map(int, input().split())

q = deque()
q.append((n, 0))
visited = [False] * 100001
visited[n] = True
while q:
    x, cost = q.popleft()
    if x == k:
        print(cost)
        break

    for next in [x - 1, x + 1, x * 2]:
        if 0 <= next <= 100000 and not visited[next]:
            visited[next] = True
            q.append((next, cost + 1))