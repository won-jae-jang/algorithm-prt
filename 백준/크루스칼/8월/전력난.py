import heapq

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    edges = []
    parents = [0] * (n + 1)
    for i in range(1, n + 1):
        parents[i] = i

    total = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        total += c
        edges.append((c, a, b))

    power = 0
    edges.sort()
    for cost, a, b in edges:
        if find_parent(parents, a) != find_parent(parents, b):
            union_parent(parents, a, b)
            power += cost

    print(total - power)


