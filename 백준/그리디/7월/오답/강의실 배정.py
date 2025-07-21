import heapq
n = int(input())
data = list(list(map(int, input().split())) for _ in range(n))
data.sort()

q = [] #끝나는 시간을 기준으로 정렬
heapq.heappush(q, 0)
room = 1
for start, end in data:
    if q[0] <= start:
        heapq.heappop(q)
        heapq.heappush(q, end)
    else:
        room += 1
        heapq.heappush(q, end)

print(room)