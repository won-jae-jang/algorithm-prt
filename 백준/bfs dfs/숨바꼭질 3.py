from collections import deque
import sys

input = sys.stdin.readline
n, k = map(int, input().split())

length = 100000
visited = [0] * (length + 1)

def bfs(i, j):
    q = deque([i])
    visited[i] = 1
    
    while q:
        x = q.popleft()
        if x == j:
            return
        
        for nx in (2 * x, x - 1, x + 1):
            if nx < 0 or nx > length:
                continue
            if visited[nx]:
                continue

            if nx == 2 * x:
                visited[nx] = visited[x] 
            else:
                visited[nx] = visited[x] + 1

            q.append(nx)

bfs(n, k)
print(visited[k] - 1)