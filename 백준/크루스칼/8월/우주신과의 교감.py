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

n, m = map(int, input().split())
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

pos = []
for _ in range(n):
    pos.append(list(map(int, input().split())))

edges = []
for i in range(n):
    for j in range(i + 1, n):
        x1, y1, x2, y2 = pos[i][0], pos[i][1], pos[j][0], pos[j][1]
        cost = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        edges.append((cost, i + 1, j + 1))

#이미 연결된 좌표
for _ in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# print(parent)

result = 0
edges.sort()
for cost, a, b in edges:
    #cycle x
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(f"{result:.2f}")

