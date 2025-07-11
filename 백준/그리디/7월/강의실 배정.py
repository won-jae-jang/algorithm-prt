import heapq

n = int(input())
data = list(list(map(int, input().split())) for _ in range(n))

data.sort()
q = [] #현재 사용중인 강의실을 보관
for start, end in data:
    if len(q) == 0:
        heapq.heappush(q, end)
        continue

    if q[0] <= start:
        heapq.heappop(q)
        heapq.heappush(q, end)
    else:
        heapq.heappush(q, end)

print(len(q))