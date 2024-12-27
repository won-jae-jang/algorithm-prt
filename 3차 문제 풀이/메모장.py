import heapq

q = []
heapq.heappush(q, 5)
heapq.heappush(q, 1)
heapq.heappush(q, 3)
heapq.heappush(q, 7)
heapq.heappush(q, 6)

print(q)
print(heapq.heappop(q))
print(q)
print(heapq.heappop(q))
print(q)
print(heapq.heappop(q))