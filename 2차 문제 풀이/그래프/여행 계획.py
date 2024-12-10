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

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i, j + 1)

plan = list(map(int, input().split()))
root = find_parent(parent, plan[0])
result = True
for i in range(1, len(plan)):
    if find_parent(parent, parent[i]) != root:
        result = False
        break

if result == True:
    print('YES')
else:
    print('NO')