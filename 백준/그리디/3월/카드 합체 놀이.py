import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
q = []

for card in cards:
    heapq.heappush(q, card)

for i in range(m):
    first = heapq.heappop(q)
    second = heapq.heappop(q)
    sum_value = first + second
    heapq.heappush(q, sum_value)
    heapq.heappush(q, sum_value)

print(sum(q))