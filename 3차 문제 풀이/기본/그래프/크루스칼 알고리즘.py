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

#노드의 개수와 간선(union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) #부모 테이블 초기화

#모든 간선을 다믈 리스트와 최종 비용을 담을 변수
edges = []
result = 0

#부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

#union 연산을 각각 수행
for i in range(e):
    a, b, cost = map(int, input().split())
    #비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 지정
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    #사이클을 발생시키지 않으면 
    if find_parent(parent, a) !=find_parent(parent, b):
        union_parent(parent, a ,b)
        result += cost

print(result)