import heapq
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
INF = int(1e9)

length = 100000
distance = [INF] * (length + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for next_pos in [now - 1, now + 1, now * 2]:
            if next_pos < 0 or next_pos > length:
                continue

            if next_pos == now * 2:
                cost = dist
            else:
                cost = dist + 1

            if cost < distance[next_pos]:
                distance[next_pos] = cost
                heapq.heappush(q, (cost, next_pos))
            
dijkstra(n)
print(distance[k])