import heapq

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort()
q = []
room = 1
heapq.heappush(q, 0)

for start, end in arr:
    if q[0] <= start:
        heapq.heappop(q)
        heapq.heappush(q, end)
    else:
        room += 1
        heapq.heappush(q, end)

print(room)