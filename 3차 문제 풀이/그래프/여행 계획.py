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
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

plan = list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        #i -> j 로 도로가 연결되어 있다면 
        if data[i][j] == 1:
            union_parent(parent, i + 1, j + 1)

result = True
for i in range(len(plan) - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        result = False

if result:
    print('YES')
else:
    print('NO')