from collections import deque

#노드의 개수와 간선(union 연산)의 개수 입력 받기
v, e = map(int, input().split())
#모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
#그래프 초기화
graph = [[] for _ in range(v + 1)]

#모든 간선 정보 입력받기
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) #정점 a 에서 b로 이동 가능
    indegree[b] += 1


def topology_sort():
    result = [] #알고리즘 수행 결과를 담을 리스트
    q = deque()

    #처음 시작할 때 진입차수가 0인 노드를 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    #위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()