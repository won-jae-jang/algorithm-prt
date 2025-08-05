import heapq
n = int(input())
visited = [False] * 10001 #1일에서 10000일 사이에 강연을 했는지 여부
q = []
for i in range(n):
    value, date = map(int, input().split())
    heapq.heappush(q, (-value , date))

result = 0
while q:
    value, date = heapq.heappop(q)
    value = -value
    if not visited[date]:
        result += value
        visited[date] = True
        continue

    for i in range(date, 0, -1):
        if not visited[i]:
            visited[i] = True
            result += value
            break

print(result)