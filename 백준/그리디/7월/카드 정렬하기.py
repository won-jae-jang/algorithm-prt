import heapq

n = int(input())
q = []
for i in range(n):
    heapq.heappush(q, int(input()))

# print(len(q))
result = 0

while len(q) >= 2:
    first = heapq.heappop(q)
    second = heapq.heappop(q)
    result += first + second
    heapq.heappush(q, first + second)

print(result)