import heapq

for tc in range(int(input())):
    n = int(input())
    q = []
    data = list(map(int, input().split()))
    for i in range(n):
        heapq.heappush(q, data[i])

    result = 0
    while len(q) >= 2:
        first = heapq.heappop(q)
        second = heapq.heappop(q)
        sum_value = first + second
        result += sum_value
        heapq.heappush(q, (sum_value))

    print(result)
