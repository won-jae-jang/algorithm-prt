from collections import deque
import copy

n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
time = [0] * (n + 1)
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0] #강의 수강 시간
    for j in range(1, len(data)):
        #i를 수강하려면 j가 선수과목임 (j -> i)
        if data[j] != -1:
            indegree[i] += 1
            graph[data[j]].append(i)

def topology_sort():
    q = deque()
    result = copy.deepcopy(time)
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