from sys import stdin
from collections import deque

N, M, R = map(int, stdin.readline().split())

matrix = []
answer = [[0]*M for _ in range(N)]
deq = deque()

for i in range(N):
    matrix.append(list(stdin.readline().split()))

loops = min(N, M) // 2
for i in range(loops):
    deq.clear()
    deq.extend(matrix[i][i : M - i]) #위쪽
    deq.extend(row[M - 1 - i] for row in matrix[i + 1 : N - i - 1]) #오른쪽
    deq.extend(matrix[N - 1 - i][i : M - i][::-1]) #아래쪽
    deq.extend(row[i] for row in matrix[i + 1 : N - 1 - i][::-1]) #왼쪽

    deq.rotate(-R)
    #위쪽
    for j in range(i, M - i):
        answer[i][j] = deq.popleft()
    #오른쪽
    for j in range(i + 1, N - i - 1):
        answer[j][M - 1 - i] = deq.popleft()
    #아래쪽
    for j in range(M - i - 1, i - 1, -1):
        answer[N - 1 - i][j] = deq.popleft()
    #왼쪽
    for j in range(N - 2 - i, i, -1):
        answer[j][i] = deq.popleft()

for line in answer:
    print(*line)