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

g = int(input())
p = int(input())
parent = [0] * (g + 1)
for i in range(g + 1):
    parent[i] = i

result = 0
for i in range(p):
    info = int(input())
    info_p = find_parent(parent, info)
    if info_p != 0:
        result += 1
        union_parent(parent, info_p, info_p - 1)
    else:
        break

print(result)