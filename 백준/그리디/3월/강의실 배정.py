import heapq

n = int(input())
data = []

for i in range(n):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x:(x[0], x[1]))
q = [data[0][1]] #강의 종료 시간
for i in range(1, n):
    if data[i][0] >= q[0]:
        heapq.heappop(q)
    heapq.heappush(q, data[i][1])

print(len(q))