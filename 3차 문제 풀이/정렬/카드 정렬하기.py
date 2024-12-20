import heapq

q = []
n = int(input())
for i in range(n):
    heapq.heappush(q, int(input()))

result = 0
while len(q) != 1:
    first = heapq.heappop(q)
    second = heapq.heappop(q)
    sum_value = first + second
    heapq.heappush(q, sum_value)
    result += sum_value

print(result)   