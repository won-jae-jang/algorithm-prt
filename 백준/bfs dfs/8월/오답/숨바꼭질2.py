#9:50
from collections import deque
n, k = map(int, input().split())

q = deque()
q.append(n)
visited = [0] * (100001)
visited[n] = 0
count = 0
while q:
    x = q.popleft()
    if x == k:
        count += 1
        continue

    for next in [x - 1, x + 1, x * 2]:
        #방문하지 않았거나 방문해도 무방한 경우
        if 0 <= next <= 100000 and (not visited[next] or visited[next] == visited[x] + 1):
            q.append(next)
            visited[next] = visited[x] + 1

print(visited[k])
print(count)