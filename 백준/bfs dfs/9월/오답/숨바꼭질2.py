from collections import deque

n, k = map(int, input().split()) #n -> k
q = deque()
q.append((0, n)) #time, cur_node
count = 0
result = 0
visited = [0] * 100001

while q:
    time, x = q.popleft()
    if x == k:
        if result == 0 or result == time:
            count += 1
            result = time
            continue

    for nx in [x * 2, x - 1, x + 1]:
        if 0 <= nx <= 100000 and (not visited[nx] or time + 1 == visited[nx]):
            visited[nx] = time + 1
            q.append((time + 1, nx))

print(result)
print(count)