from collections import deque
n, k = map(int, input().split())
visited = [0] * 100001

q = deque()
q.append(n)
visited[n] = 0
shortest_time = 0
count = 0
while q:
    x = q.popleft()
    #최초로 동생을 찾은 경우
    if x == k:
        count += 1
        continue

    for nx in [x - 1, x + 1, x * 2]:
        #방문하지 않았거나 방문해도 무방한 좌표인 경우
        if 0 <= nx < 100001 and (not visited[nx] or visited[nx] == visited[x] + 1):
            visited[nx] = visited[x] + 1
            q.append(nx)

print(visited[k])
print(count)