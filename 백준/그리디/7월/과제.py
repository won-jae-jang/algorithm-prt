import heapq
n = int(input())
q = []
assinged = [False] * 1001 #과제가 할당된 일자
result = 0
for i in range(n):
    day, score = map(int, input().split())
    heapq.heappush(q, (-score, day)) #최대 힙 큐로 구성

while q:
    score, day = heapq.heappop(q)
    score *= -1 #양수로 전환
    #과제를 수행할 수 있는지 체크
    for i in range(day, 0, -1):
        #현재 과제를 수행할 수 없는 경우
        if assinged[i] == True:
            continue
        #현재 과제를 수행할 수 있는 경우
        else:
            assinged[i] = True
            result += score
            break

print(result)