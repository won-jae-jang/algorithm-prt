from collections import deque
n, k = map(int, input().split())
visited = [False] * 100001

q = deque()
q.append((n, 0))
visited[n] = True
while q:
    x, time = q.popleft()
    #동생을 찾은 경우
    if x == k:
        print(time)
        break
    for idx in [x - 1, x + 1, x * 2]:
        if 0 <= idx < 100001 and not visited[idx]:
            visited[idx] = True
            q.append((idx, time + 1))

