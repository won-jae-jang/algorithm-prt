import sys
input = sys.stdin.readline
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

edges = []
result = 0
sum_value = 0
for i in range(m):
    x, y, z = map(int, input().split())
    sum_value += z
    edges.append((z, x, y))

edges.sort()
for edge in edges:
    cost, x, y = edge
    #사이클이 발생하지 않으면
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost

print(sum_value - result)