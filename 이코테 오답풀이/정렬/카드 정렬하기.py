import heapq

n = int(input())
q = []
for i in range(n):
    heapq.heappush(q, int(input()))

result = 0
while len(q) >= 2:
    first = heapq.heappop(q)
    second = heapq.heappop(q)
    sum_value = first + second
    result += sum_value
    heapq.heappush(q, sum_value)

print(result)