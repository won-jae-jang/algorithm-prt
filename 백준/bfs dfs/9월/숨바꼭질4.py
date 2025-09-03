from collections import deque

n, k = map(int, input().split()) #n -> k
q = deque()
q.append((0, n)) #time, cur_node

move = [0] * 100001 # move[i] = k: i번째 노드의 부모 노드는 k이다.
dist = [0] * 100001 # dist[i] = k: i번째 노드의 소요시간

while q:
    time, x = q.popleft()
    if x == k:
        break

    for nx in [x * 2, x - 1, x + 1]:
        if 0 <= nx <= 100000 and not dist[nx]:
            move[nx] = x #nx의 부모는 x
            dist[nx] = time + 1
            q.append((time + 1, nx))

print(dist[k])
path = []
idx = k
for _ in range(dist[k] + 1):
    path.append(idx)
    idx = move[idx]

print(*path[::-1])