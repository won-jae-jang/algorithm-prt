N = int(input())
INF = 1e10
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(N + 1):
    for j in range(N + 1):
        if i == j:
            graph[i][j] = 0

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

lst = [] #회장 후보
score = INF #회장 점수
#회장 점수 얻기
for i in range(1, N + 1):
    score = min(score, max(graph[i][1:]))

#회장 후보 체크
for i in range(1, N + 1):
    if max(graph[i][1:]) == score:
        lst.append(i)

print(score, len(lst))
print(' '.join(map(str, lst)))