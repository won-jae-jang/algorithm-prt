import sys
sys.setrecursionlimit(10000)
V, E = map(int, input().split())
parent = [0] * (V + 1)
edges = []

for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

for i in range(1, V + 1):
    parent[i]= i

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0
edges.sort()
for cost, a, b in edges:

    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a, b)

print(result)