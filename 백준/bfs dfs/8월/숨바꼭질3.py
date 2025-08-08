from collections import deque
n, k = map(int, input().split())
visited = [0] * 100001

q = deque()
q.append(n)
visited[n] = 1
while q:
    x = q.popleft()
    #동생을 찾은 경우
    if x == k:
        print(visited[k] - 1)
        break
    for nx in [x * 2, x - 1, x + 1]:
        if 0 <= nx < 100001 and not visited[nx]:
            if nx == x * 2:
                visited[nx] = visited[x]
            else:
                visited[nx] = visited[x] + 1

            q.append(nx)