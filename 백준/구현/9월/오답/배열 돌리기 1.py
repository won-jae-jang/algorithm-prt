# 6: 42
from collections import deque
n, m, r = map(int, input().split()) #r은 음의 방향으로
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(min(n, m) // 2):
    q = deque()
    #위쪽
    q.extend(arr[i][i : m - i])
    #오른쪽
    q.extend(arr[j][m - 1 - i] for j in range(i + 1, n - i - 1))
    #아래쪽
    q.extend(arr[n - 1 - i][i : m - i][::-1])
    #왼쪽
    q.extend(arr[j][i] for j in range(n - i - 2, i, -1))

    q.rotate(-r)
    #위쪽
    for j in range(i, m - i):
        arr[i][j] = q.popleft()
    #오른쪽
    for j in range(i + 1, n - i - 1):
        arr[j][m - 1 - i] = q.popleft()
    #아래쪽
    for j in range(m - i - 1, i - 1, -1):
        arr[n - 1 - i][j] = q.popleft()
    #왼쪽
    for j in range(n - i - 2, i, -1):
        arr[j][i] = q.popleft()

for row in arr:
    print(*row)
