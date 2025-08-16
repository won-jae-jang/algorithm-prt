import math

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
parents = [0] * N
pos = []
for i in range(N):
    pos.append(list(map(float, input().split())))
    parents[i] = i #자신의 부모를 자기 자신으로 초기화

edges = []
for i in range(N):
    x1, y1 = pos[i]
    for j in range(i + 1, N):
        x2, y2 = pos[j]
        cost = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        edges.append((cost, i, j))

result = 0
edges.sort()
for cost, a, b in edges:
    if find_parent(parents, a) != find_parent(parents, b):
        result += cost
        union_parent(parents, a, b)

print(result)