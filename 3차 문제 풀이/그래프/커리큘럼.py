from collections import deque
import copy

n = int(input())
indegree = [0] * (n + 1)
time = [0] * (n + 1) #각 과목별 수강시간
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    info = list(map(int, input().split()))
    time[i] = info[0]
    #선수과목 기록
    for j in range(1, len(info) - 1):
        graph[info[j]].append(i) 
        indegree[i] += 1

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], time[i] + result[now])
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])

topology_sort()